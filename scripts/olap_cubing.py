"""
Module 6: OLAP and Cubing Script
File: scripts/olap_cubing.py

This script handles OLAP cubing with Python. 
It ingests data from a data warehouse, performs aggregations for multiple dimensions, 
and creates OLAP cubes. The cubes are saved as CSV files for further analysis.

Purpose:
- Allows fast querying and analysis across multiple dimensions
- Reduces need for computing aggregations on the fly
- Useful for BI tools like Power BI, Snowflake, or Looker

Input Tables (from SQLite DW):
- Fact table (`sale`): sale_id, product_id, store_id, customer_id, sale_amount, sale_date
- Dimension tables: 
    - `product` (product_id, category, ...)
    - `customer` (customer_id, region, ...)

Output Cube:
- Grouped by category, store_id, region
- Includes sum and count of sale_amount, plus list of sale_ids

Example output columns:
category,store_id,region,sale_amount_sum,sale_amount_count,sale_ids
"""

import pandas as pd
import sqlite3
import pathlib
import sys

# Add project root to path for local imports
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from utils.logger import logger  # noqa: E402

# Constants
DW_DIR = pathlib.Path("data") / "dw"
DB_PATH = DW_DIR / "smart_sales.db"
OLAP_OUTPUT_DIR = pathlib.Path("data") / "olap_cubing_outputs"
OLAP_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def create_olap_cube(sales_df: pd.DataFrame, dimensions: list, metrics: dict) -> pd.DataFrame:
    """
    Create OLAP cube by aggregating data on given dimensions.

    Args:
        sales_df (pd.DataFrame): Input sales data
        dimensions (list): Grouping dimensions
        metrics (dict): Aggregation functions

    Returns:
        pd.DataFrame: Aggregated OLAP cube
    """
    try:
        grouped = sales_df.groupby(dimensions)
        cube = grouped.agg(metrics).reset_index()
        cube["sale_ids"] = grouped["sale_id"].apply(list).reset_index(drop=True)

        columns = generate_column_names(dimensions, metrics)
        columns.append("sale_ids")
        cube.columns = columns

        logger.info(f"OLAP cube created using dimensions: {dimensions}")
        return cube
    except Exception as e:
        logger.error(f"Failed to create OLAP cube: {e}")
        raise


def generate_column_names(dimensions: list, metrics: dict) -> list:
    """Generate flat column names from dimensions and metrics."""
    names = dimensions.copy()
    for col, funcs in metrics.items():
        if isinstance(funcs, list):
            names += [f"{col}_{func}" for func in funcs]
        else:
            names.append(f"{col}_{funcs}")
    return [n.rstrip("_") for n in names]


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
            s.sale_id,
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

        dimensions = ["category", "store_id", "region"]
        metrics = {"sale_amount": ["sum", "count"]}

        cube = create_olap_cube(df, dimensions, metrics)
        write_cube_to_csv(cube, "multidimensional_olap_cube.csv")

        logger.info("OLAP cubing complete.")
        logger.info(f"Output saved to {OLAP_OUTPUT_DIR}")

    except Exception as e:
        logger.error(f"OLAP Cubing failed: {e}")
        raise


if __name__ == "__main__":
    main()
