# store-smart-shelayne-smith
# Smart Store BI Project – Shelayne Smith
# store-smart-shelayne-smith

# Smart Store BI Project – Shelayne Smith

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
* ![](data/dw/images/P6.%20Power%20BI%20image.PNG)

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



      ![Alt text](data/dw/images/CUSTOMERDW.PNG)
      ![Alt text](data/dw/images/PRODUCTSDW-1.PNG)
      ![Alt text](data/dw/images/SALESDW.PNG)
P5. Cross-Platform Reporting with Power BI and Spark
   1.	Download Power BI 
   2.	Install SqLite ODBC
   3.	Configure ODBC Data Source Name (DSN)
      a.	Open ODBC Data Source 64-bit from Start Menu
      b.	Click the system DSN tab
      c.	Click add: choose SQLite3 ODBC Driver: click Finish
      d.	Click Browse add select your database file smart_sales.db
      e.	Click Ok to save
   4.	Load Tables
      a.	Open Power BI
      b.	Get Data > Select ODBC from list
      c.	Choose SmartSalesDSN
      d.	Click OK
      e.	Select tables:
         i.	Customer table
         ii.	Product table
         iii.	Sales table
      f.	Click load and switch to model view
   5.	SQL Query Editor
      a.	Home Tab > Transform Data to open Power Query Editor
      b.	Top menu select advanced editor
         i.	Delete code and replace with your SQL query using your own DSN name, table names, and column names.
      c.	Click Done
      d.	Rename query Top Customers or whatever your focus is on
      e.	Click Close and Apply to return to report view
      f.	Use tables to visualize the data set
   6.	Slicing, dicing, and Drilldown for Visualization
      a.	Slicing: filter the data to view a single layer based on one dimension
         i.	Create slicers for total sales amount per region for each product.  Slicers allow for filtering down to sales amount for a single product per region, and a single region with totals for each product.
      b.	Dicing: Similar to slicing, but on multiple dimensions, creates a subcube from the larger dataset.
         i.	Creating a report that joins sales with customers and products tables (dimensions tables) which produces data showing the top performs.
      c.	Drilldown: Moving from a summary view to more detailed data, while drill-up is the reverse.
         i.	Create drilldown by implementing year.  Our data is for one specific date, so we will not be able to drill down to a quarterly/monthly/weekly/daily basis.
   7.	Dashboard Design
      a.	Implemented drilldown to allow for data to be aggregated view sales trends.
      b.	Created chart with product category, and region for axis; applied sales amount to compare which region is selling the most of each product.
      c.	Allow drilldown from region to store level for additional insight.
      ![Alt text](data/dw/images/Top%20Customer.PNG)
      ![Alt text](data/dw/images/Total%20Sales.PNG)
      ![Alt text](data/dw/images/Slicer.PNG)
      ![Alt text](data/dw/images/Product%20Sales%20by%20region.PNG)
P6. BI Insights & Storytelling
   1.	The Business Goal: What is the most profitable product by region for last year? What is the most profitable store in each region and what product is the most profitable?
      •	Descriptive Dimensions: Product, Region, StoreID
      •	Numeric Metric: Total Sales
      •	Aggregation: SUM
      •	Slicing: Total sales by product
      • Dicing: Product by region
      •	Drill-down: Total sales by product by region by store
   2.	Data Source:
      •	What information did you start with?  Prepared data
      •	Clearly indicate which column of which tables were used.
         o	Tables: Sales, Product, Customers
         o	Columns: product_category, region, sale_amount, store_id
      •	Workflow:
         o	Aggregate: Product Category
         o	Calculate total sales for the year per product per region per store
         o	Drilldown data to store id
   3.	Tell us what tools you used and why: OLAP cub script to generate CSV with required columns. Power BI, to provide data visualization and slicing, dicing, and drilldown/rollup.  Images and Power BI file with tables and drilldown attached below.
   4.	Workflow & Logic
      •	Create olap_cubing.py script to generate multidimensional_olap_cube.csv file with all required columns.
      •	Create data/olap_cubing_outputs folder for multidimensional_olap_cube.csv to populate in for correct pathway present in olap_cubing.py script.
      •	Pulled csv file into Power BI and created applicable slice, dice, and drilldown features within the matrix (pivot) table.
         o	Matrix table:
            	X-axis: product
            	Y-axis: region (drilldown: store)
            	Value: total sales
         o	Create Bar chart to show product, region, and total sales for visualization.
* ![Alt text](data/dw/images/P6.%20Power%20BI%20image.PNG)
   5.	Results
      a.	Low performing region – central; high performing region- east
      b.	Low selling product- Office (marginally); High selling product- Home
      c.	REFERENCE and pull Power BI file.pbix to use interactive data in Power BI.  Located in smart-store-shelayne-smith Repo.
   6.	Suggested Business Action
      a.	Determine what marketing strategies or specific electronics, home, office, and clothing items are the biggest sellers for the Eastern region, and implement those marketing strategies in other regions to increase total sales.
      b.	Evaluate inventory for office supplies to determine which products are underperforming and bring in inventory that is selling or alternative products to increase sales in office products.
      c.	Create complimentary products between office/home and electronics.  To increase sales for complimentary products.
      d.	Evaluate region specific clothing items that are relevant to the region to increase sales of clothing products.
   7.	Challenges
      a.	Removing inconsistencies with duplicated data
      b.	Getting the correct script formate to successfully run olap_cube.py
         i.	Used ChatGPT to help clean up script to pull correct information and generate olaps output
COMMANDS
   1.	 To Commit Changes
      a.	Go to Source > click the + icon next to the file you want to commit changes
      b.	Add a description of the changes made to file
      c.	Commit
      d.	When all changes have been committed sync with GitHub
   2.	Push/Pull to GitHub
      a.	Three commands to utilize after each small change
         i.	Git add .  : Any new files to source control (so the new files will be tracked)
         ii.	Git commit -m “Update README.md with command” – set of changes to the git project repository with a message telling what you did.
         iii.	Git push – that named set of changes (called a commit) up to GitHub for safe keeping
      1.	Source Control Panel > Click on … Select Push OR open a *terminal and run: git push origin main
         iv.	Git Pull – pull information into local from GitHub
      1.	Source Control Panel > … > Select Pull or open a terminal and run: Git pull origin main
   3.	Activate .venv: .venv/scripts/activate
         a.	External Dependencies: Libraries, packages, and modules beyond the standard library and include common packages (ex.pandas).
            i.	These must be installed in our local project virtual environment to use in our code.
               1.	Activate .venv
               2.	Update key packages
               3.	Install dependencies from the requirements.txt file
               4.	Run Commands
                  a.	.venv/scripts/activate
                  b.	Py -m pip install –upgrade pip setuptools wheel
                  c.	Py -m pip install -r requirements.txt
   4.	P.3 Scripts
      a.	py scripts/data_preparation/prepare_customers_data.py
      b.	py scripts/data_preparation/prepare_products_data.py
      c.	py scripts/data_preparation/prepare_sales_data.py
   5.	P.4 Scripts
      a.	Python scripts/etl_to_dw.py
NOTE: 
P1. BI Python
   1.	File Extensions overview
      a.	Comma-Separated Values (csv): stores tabular data, each row is a record, each column is separated by a comma.
      b.	Markdown (.md): Used for documentation; renders nicely online with headings and formatting. 
         i.	Markdown cells turn your input into clean, readable text like you’d see in a report.  It’s helpful for adding notes, explanations, or even formatting your notebook like a guide.
      c.	Text (txt): Lists required external packages for the project.
         i.	Requirements.txt: Lists all the packages the project needs
            1.	Lines starting with a hash are ignored when installing packages using this file.
      d.	Hidden/System Files (.): Project management files that help keep unneeded files out of version control.
         i.	.gitignore: File lists content that doesn’t need to be tracked in the project history
   2.	All scripts are for Windows users only
   3.	Double check spacing on folder and files: ran into an issue with phython script because there was a space in logger.py which nade it so the system couldn’t find the pathway to run the scripts.
   4.	Double check file names against script entries for correct pathway logic.  Follow existing naming conventions- use the pattern already provided in your data tables.
   5.	Fake Data
      a.	When you fake data, you can be creative-missing information, values that are outside acceptable ranges, and/or perfectly clean data.  It is best to start with simple, clean data, and AFTER everything is working, go back and modify the fake data to make your analysis more challenging.
P3. Prepare Data for ETL
   1.	Ran test script py tests/test_data_scrubber.py, received error No module names ‘utils’.  It means Python cannot find the utils folder in your project when trying to import something like: from utils.logger import logger.
   2.	Fixes:
      a.	Option 1: Adde the project root to sys.path
         i.	At the top of your Python script or test file, add:
            1.	Import sys
            2.	Import pathlib
         ii.	Add the root directory of your project to the system path
         iii.	Sys.path.append(str(pathlib.path(file).resolve().parent.parent))
         iv.	If your test file is in tests/test_data_scrubber.py, this goes at the top of that file.
      b.	Option 2:
         i.	Run the script from the project root (this is what I used to run test successfully).
         ii.	Instead of phython tests/test_data_scrubber.py, do python -m tests.test_data_scrubber
            1.	Note: Make sure you are in your project root folder when running this.
P4. Create and Populate DW
   1.	Double check spelling of column names 
      a.	Issues: incorrect column name titles caused errors when creating dw. Verify and review all column names and make corrections.
      b.	Issue: conn: did not have the correct pathway and was causing sqlite3.OperationalError.  Unable to open database file.  Put code into ChatGPT to get the conn: to the right pathway.


