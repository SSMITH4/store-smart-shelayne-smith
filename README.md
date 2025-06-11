# Smart Store BI Project – Shelayne Smith
# store-smart-shelayne-smith

This Business Intelligence (BI) project showcases the full pipeline from environment setup, data preparation, OLAP cube generation, to visualization using Power BI. The goal is to identify top-performing products and stores by region and generate actionable insights.

---

## 📁 Project Repository

**Repo Name:** `smart-store-shelayne-smith`

---

## 🔧 P1. BI Python Setup & Project Initialization

### 1. Environment & Tooling Setup

* **Install**:

  * Python
  * GitHub CLI/Desktop
  * Visual Studio Code (VS Code)

* **Configure GitHub**:

  * Create new repo on GitHub: `smart-store-shelayne-smith`
  * Clone repo locally

* **VS Code Extensions**:

  * Python
  * GitLens
  * Jupyter
  * SQLite Viewer

### 2. Folder Setup

* Create project folder locally on `C:` and sync with GitHub
* Navigate to repo via: file > Open Folder > Navigate to smart-store-shelayne-smith

### 3. Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

> `.venv` contains a self-contained Python environment with its own pip, interpreter, and dependencies.

### Project Structure

```
smart-store-shelayne-smith/
├── data/
│   ├── raw/
│   │   ├── customer_data.csv
│   │   ├── products_data.csv
│   │   └── sales_data.csv
│   ├── prepared/
│   │   ├── customers_prepared.csv
│   │   ├── products_prepared.csv
│   │   └── sales_prepared.csv
│   ├── dw/
│   │   └── smart_sales.db
│   ├── logs/
│   │   └── project_log.log
│   └── olap_cubing_outputs/
│       └── multidimensional_olap_cube.csv
│
├── scripts/
│   ├── data_prep.py
│   ├── data_scrubber.py
│   ├── etl_to_dw.py
│   ├── olap_cubing.py
│   └── data_preparation/
│       ├── prepare_customers_data.py
│       ├── prepare_products_data.py
│       └── prepare_sales_data.py
│
├── tests/
│   └── test_data_scrubber.py
│
├── utils/
│   └── logger.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔧 P2. Data Preparation and Exploration

### Logger Setup

* `utils/logger.py`: handles logging
* Output: `data/logs/project_log.log`

### Execute Scripts

```bash
py scripts/data_prep.py
```

### Version Control

```bash
git add .
git commit -m "Add data preparation script"
git push origin main
```

---

## 🔧 P3. Prepare Data for ETL

### Data Cleaning & Tests

* Script: `scripts/data_scrubber.py`
* Test:

```bash
python -m tests.test_data_scrubber
```

### Data Preparation Scripts

```bash
py scripts/data_preparation/prepare_customers_data.py
py scripts/data_preparation/prepare_products_data.py
py scripts/data_preparation/prepare_sales_data.py
```

---

## 🔧 P4. Create & Populate DW

### ETL Script

* File: `scripts/etl_to_dw.py`
* Output: `data/dw/smart_sales.db`
* Run:

```bash
python scripts/etl_to_dw.py
```
* ![](data/dw/images/CUSTOMERDW.PNG)
* ![](data/dw/images/PRODUCTSDW-1.PNG)
* ![](data/dw/images/SALESDW.PNG)
---

## 🔧 P5. Power BI + OLAP Visualization

### Setup

1. Download Power BI
2. Install SQLite ODBC Driver
3. Configure ODBC DSN:

   * Open ODBC Data Source (64-bit)
   * System DSN > Add > SQLite3 ODBC Driver
   * Browse to `smart_sales.db`
4. Load Tables into Power BI
5. Use Advanced Editor in Power Query Editor to enter SQL
6. Create Slicer, Drilldown, and Dicing visualizations
7. Dashboard design with filters, bar charts, and matrix tables

Images:
* ![](data/dw/images/Top%20Customer.PNG)
* ![](data/dw/images/Total%20Sales.PNG)
* ![](data/dw/images/Slicer.PNG)
* ![](data/dw/images/Product%20Sales%20by%20region.PNG)


---

## 📈 P6. BI Insights & Storytelling

### 1. Business Goal

* **Key Questions**:

  * What is the most profitable product by region for last year?
  * Which store performs best in each region?
* **Dimensions**: Product, Region, StoreID
* **Metric**: Total Sales
* **Techniques**: Slicing, Dicing, Drilldown

### 2. Data Source

* Tables: Sales, Product, Customers
* Columns: product\_category, region, sale\_amount, store\_id

### 3. Tools Used

* `olap_cubing.py` for generating `multidimensional_olap_cube.csv`
* Power BI for visualization

### 4. Workflow & Logic

* Create `olap_cubing.py`
* Place output in `data/olap_cubing_outputs/`
* Use Power BI matrix & chart visuals

### 5. Results

* High Sales: East Region, Home Product
* Low Sales: Central Region, Office Product
* Use interactive Power BI `.pbix` file in repo

![](data/dw/images/P6.%20Power%20BI%20image.PNG)

### 6. Suggested Business Actions

* Expand East Region strategy to others
* Optimize Office product offerings
* Bundle Office/Home with Electronics
* Tailor Clothing inventory to region

### 7. Challenges

* Data inconsistencies
* Troubleshooting `olap_cubing.py`

---

## 📂 Commands & Tips

### Commit Changes

* VS Code: Source > `+` icon > Commit > Sync

### Git Commands

```bash
git add .
git commit -m "Update README.md with command"
git push origin main
git pull origin main
```

### Activate Environment

```bash
.venv/scripts/activate
```

### Install Requirements

```bash
py -m pip install --upgrade pip setuptools wheel
py -m pip install -r requirements.txt
```

### Script Execution

```bash
py scripts/data_preparation/prepare_customers_data.py
py scripts/data_preparation/prepare_products_data.py
py scripts/data_preparation/prepare_sales_data.py
python scripts/etl_to_dw.py
```

---

## 💡 Notes

* `.csv`: Tabular data format
* `.md`: Markdown for documentation
* `.txt`: Plain text files (e.g. requirements)
* `.gitignore`: Prevent tracking of unnecessary files
* Windows only scripts
* Watch for spacing in filenames
* Start with clean fake data, then add imperfections for testing

---

## 📕 Troubleshooting

### `No module named 'utils'`

#### Fix:

```python
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))
```

Or run with:

```bash
python -m tests.test_data_scrubber
```

### SQLite Error: `unable to open database file`

* Double-check DB path in your script
* Use absolute path with `pathlib`

---