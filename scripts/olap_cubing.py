"""
Module 6: OLAP and Cubing Script
File: scripts/olap_cubing.py

This script handles OLAP cubing with Python.
It ingests data from a data warehouse, performs aggregations for multiple dimensions,
and creates OLAP cubes. The cubes are saved as CSV files for further analysis.

Input Tables (from SQLite DW):
- Fact table (`sale`): product_id, store_id, customer_id, sale_amount, sale_date
- Dimension tables:
    - `product` (product_id, category, ...)
    - `customer` (customer_id, region, ...)

Output Cube:
- Grouped by category, store_id, region
- Includes sum and count of sale_amount

Example output:
category, store_id, region, sale_amount_sum, sale_amount_count
"""

import pandas as pd
import sqlite3
import pathlib
import sys

# Add project root to path for local imports
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from utils.logger import logger  # make sure this logger is properly configured

# Constants
DW_DIR = pathlib.Path("data") / "dw"
DB_PATH = DW_DIR / "smart_sales.db"
OLAP_OUTPUT_DIR = pathlib.Path("data") / "olap_cubing_outputs"
OLAP_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def create_olap_cube(sales_df: pd.DataFrame, dimensions: list, metrics: dict) -> pd.DataFrame:
    """
    Create OLAP cube by aggregating data on given dimensions.
    Handles nulls and type safety.
    """
    try:
        logger.info(f"Columns available: {sales_df.columns.tolist()}")

        # Check and clean dimensions
        for dim in dimensions:
            if dim not in sales_df.columns:
                raise KeyError(f"Missing expected dimension: {dim}")
            sales_df[dim] = sales_df[dim].fillna("Unknown").astype(str)

        # Ensure numeric metrics
        for metric_col in metrics.keys():
            if metric_col not in sales_df.columns:
                raise KeyError(f"Missing expected metric: {metric_col}")
            sales_df[metric_col] = pd.to_numeric(sales_df[metric_col], errors='coerce').fillna(0.0)

        grouped = sales_df.groupby(dimensions)
        cube = grouped.agg(metrics).reset_index()

        # Flatten MultiIndex columns
        if isinstance(cube.columns, pd.MultiIndex):
            cube.columns = ['_'.join(col).strip('_') for col in cube.columns.values]

        logger.info(f"OLAP cube created with shape {cube.shape}")
        return cube

    except Exception as e:
        logger.error(f"Failed to create OLAP cube: {e}")
        raise


def write_cube_to_csv(cube: pd.DataFrame, filename: str) -> None:
    """Save the OLAP cube to CSV."""
    try:
        path = OLAP_OUTPUT_DIR / filename
        cube.to_csv(path, index=False)
        logger.info(f"OLAP cube saved to: {path}")
    except Exception as e:
        logger.error(f"Failed to save OLAP cube: {e}")
        raise


def main():
    logger.info("Starting OLAP Cubing process...")

    try:
        conn = sqlite3.connect(DB_PATH)

        query = """
        SELECT 
            s.sale_amount,
            s.store_id,
            p.category,
            c.region
        FROM sale s
        LEFT JOIN product p ON s.product_id = p.product_id
        LEFT JOIN customer c ON s.customer_id = c.customer_id
        """

        df = pd.read_sql_query(query, conn)
        conn.close()
        logger.info("Sales data with joins loaded.")
        logger.debug(f"Sample data:\n{df.head()}")

        dimensions = ["category", "store_id", "region"]
        metrics = {"sale_amount": ["sum", "count"]}

        cube = create_olap_cube(df, dimensions, metrics)
        write_cube_to_csv(cube, "multidimensional_olap_cube.csv")

        logger.info("OLAP cubing complete.")

    except Exception as e:
        logger.error(f"OLAP Cubing failed: {e}")
        raise


if __name__ == "__main__":
    main()
