import pandas as pd
import sqlite3
import pathlib
import sys

# For local imports, temporarily add project root to sys.path
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Constants
DW_DIR = pathlib.Path("data") / "dw"
DB_PATH = DW_DIR / "smart_sales.db"
PREPARED_DATA_DIR = pathlib.Path("data") / "prepared"

def create_schema(cursor: sqlite3.Cursor) -> None:
    cursor.execute("DROP TABLE IF EXISTS customer")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customer (
        customer_id INTEGER PRIMARY KEY,
        name TEXT,
        region TEXT,
        join_date TEXT,
        loyalty_points INTEGER,
        age INTEGER
    )
    """)

    cursor.execute("DROP TABLE IF EXISTS product")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        category TEXT,
        unitprice FLOAT,
        stock_quantity INTEGER,
        supplier TEXT
    )
    """)

    cursor.execute("DROP TABLE IF EXISTS sale")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sale (
        transaction_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product_id INTEGER,
        sale_amount FLOAT,
        sale_date TEXT,
        bonus_points INTEGER,
        payment_type TEXT,
        store_id INTEGER,
        campaign_id INTEGER,
        FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
        FOREIGN KEY (product_id) REFERENCES product (product_id)
    )
    """)

def delete_existing_records(cursor: sqlite3.Cursor) -> None:
    cursor.execute("DELETE FROM customer")
    cursor.execute("DELETE FROM product")
    cursor.execute("DELETE FROM sale")

def insert_customers(customers_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    customers_df.to_sql("customer", cursor.connection, if_exists="append", index=False)

def insert_products(products_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    products_df.to_sql("product", cursor.connection, if_exists="append", index=False)

def insert_sales(sales_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    sales_df.to_sql("sale", cursor.connection, if_exists="append", index=False)

def load_data_to_db() -> None:
    DW_DIR.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        create_schema(cursor)
        delete_existing_records(cursor)

        # Load and normalize data
        customers_df = pd.read_csv(PREPARED_DATA_DIR / "customers_prepared.csv")
        products_df = pd.read_csv(PREPARED_DATA_DIR / "products_prepared.csv")
        sales_df = pd.read_csv(PREPARED_DATA_DIR / "sales_prepared.csv")

        def normalize_columns(df: pd.DataFrame, rename_map: dict) -> pd.DataFrame:
            df.columns = [col.lower() for col in df.columns]
            return df.rename(columns=rename_map)

        customers_df = normalize_columns(customers_df, {
            "customerid": "customer_id",
            "name": "name",
            "region": "region",
            "joindate": "join_date",
            "loyaltypoints": "loyalty_points",
            "age": "age"
        })

        products_df = normalize_columns(products_df, {
            "productid": "product_id",
            "productname": "product_name", 
            "category": "category",
            "unitprice": "unitprice",
            "stockquantity": "stock_quantity",
            "supplier": "supplier"
        })

        sales_df = normalize_columns(sales_df, {
            "transactionid": "transaction_id",
            "customerid": "customer_id",
            "productid": "product_id",
            "saleamount": "sale_amount",
            "saledate": "sale_date",
            "bonuspoints": "bonus_points",
            "paymenttype": "payment_type",
            "storeid": "store_id",
            "campaignid": "campaign_id"
        })

        insert_customers(customers_df, cursor)
        insert_products(products_df, cursor)
        insert_sales(sales_df, cursor)

        conn.commit()

if __name__ == "__main__":
    load_data_to_db()
