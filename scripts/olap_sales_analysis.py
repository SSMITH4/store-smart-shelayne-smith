import pandas as pd
import matplotlib.pyplot as plt
import pathlib
import sys

# For local imports, temporarily add project root to Python sys.path
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from utils.logger import logger  # noqa: E402

# Constants
OLAP_OUTPUT_DIR: pathlib.Path = pathlib.Path("data").joinpath("olap_cubing_outputs")
CUBED_FILE: pathlib.Path = OLAP_OUTPUT_DIR.joinpath("multidimensional_olap_cube.csv")
RESULTS_OUTPUT_DIR: pathlib.Path = pathlib.Path("data").joinpath("results")

# Create output directory for results if it doesn't exist
RESULTS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_olap_cube(file_path: pathlib.Path) -> pd.DataFrame:
    """Load the precomputed OLAP cube data."""
    try:
        cube_df = pd.read_csv(file_path)
        logger.info(f"OLAP cube data successfully loaded from {file_path}.")
        return cube_df
    except Exception as e:
        logger.error(f"Error loading OLAP cube data: {e}")
        raise


def analyze_sales_by_product_region(cube_df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total sales by Product and Region."""
    try:
        sales_by_product_region = (
            cube_df.groupby(["category", "Region"])["sale_amount_usd_sum"]
            .sum()
            .reset_index()
            .rename(columns={"sale_amount_usd_sum": "TotalSales"})
        )
        logger.info("Sales aggregated by Product and Region successfully.")
        return sales_by_product_region
    except Exception as e:
        logger.error(f"Error analyzing sales by Product and Region: {e}")
        raise


def save_sales_by_product_region(sales_df: pd.DataFrame) -> None:
    """Save aggregated sales data to CSV."""
    try:
        output_path = RESULTS_OUTPUT_DIR.joinpath("sales_by_product_region.csv")
        sales_df.to_csv(output_path, index=False)
        logger.info(f"Sales by product and region saved to {output_path}.")
    except Exception as e:
        logger.error(f"Error saving sales by product and region: {e}")
        raise


def analyze_sales_by_product_region_store(cube_df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total sales by Product, Region, and Store."""
    try:
        sales_by_product_region_store = (
            cube_df.groupby(["category", "Region", "StoreID"])["sale_amount_usd_sum"]
            .sum()
            .reset_index()
            .rename(columns={"sale_amount_usd_sum": "TotalSales"})
        )
        logger.info("Sales aggregated by Product, Region, and Store successfully.")
        return sales_by_product_region_store
    except Exception as e:
        logger.error(f"Error analyzing sales by Product, Region, and Store: {e}")
        raise


def save_sales_by_product_region_store(sales_df: pd.DataFrame) -> None:
    """Save detailed store-level sales data to CSV."""
    try:
        output_path = RESULTS_OUTPUT_DIR.joinpath("sales_by_product_region_store.csv")
        sales_df.to_csv(output_path, index=False)
        logger.info(f"Drill-down sales data saved to {output_path}.")
    except Exception as e:
        logger.error(f"Error saving sales data: {e}")
        raise


def main():
    logger.info("Starting SALES ANALYSIS...")

    # Load the cube
    cube_df = load_olap_cube(CUBED_FILE)

    # Product + Region
    sales_by_product_region = analyze_sales_by_product_region(cube_df)
    save_sales_by_product_region(sales_by_product_region)

    # Product + Region + Store
    store_sales_df = analyze_sales_by_product_region_store(cube_df)
    save_sales_by_product_region_store(store_sales_df)


if __name__ == "__main__":
    main()
