# store-smart-shelayne-smith
P1. BI Python (Machine Set-up, Initialize Project, and Organize Collaborate)
   1.	Install Python, GitHub, and Visual Studio Code	
a.	Configure GitHub
b.	Install extensions in VS Code
c.	Create Project Folder (Repo) 
i.	GitHub
ii.	Locally on C: drive
   2.	Create Repo: smart-store-shelayne-smith
      a.	Open repo in VS Code 
      b.	Change pathway from Repo folder to store-smart-shelayne-smith
         i.	File > Open Folder > Navigate to store-smart-shelayne-smith within File Explorer and select.
         ii.	You can use cd and file name to sync in terminal for correct folder pathway
   3.	Create a virtual environment
      a.	Run .venv/scripts/activate
      b.	Make sure a .venv folder exists 
         *.venv- virtual environment in Python: self-containing environment that includes its own Python interpreter, pip, and libraries.  Helps manage dependencies per project, so they don’t interfere with other projects or system-wide Python.
   4.	Folder Structure configuration 
   5.	smart-store-yourname/   
      │
      ├── data/                
      │   ├── raw/                          
      │
      ├── scripts/                            
      │
      ├── utils/                     
      │   └── logger.py             
      │
      ├── .gitignore                 
      ├── README.md                  
      └── requirements.txt  
   6.	Create data folder: data/raw:
      a.	Add sample data
         i.	Customer_data.csv
         ii.	Products_data.csv
         iii.	Sales_data.csv
P.2 BI Tools Setup, Data Exploration, & Mining
   1.	Create utils/logger.py and apply script
      a.	This script provides logging functions for a project.  Essential way to track events and issues during execution.
   2.	Create logs Folder:
      a.	data/logs/project_log.log and apply script
   3.	Create scripts/data_prep.py and apply script
   4.	Execute Python Script
      a.	py scripts/data_prep.py
   5.	Git-add-commit-push to GitHub
P.3 Prepare Data for ETL
   1.	Create file: scripts/data_scrubber.py and apply script to file
   2.	Create file: tests/test_data_scrubber.py and apply script to file
      a.	Run test script: py tests/test_data_scrubber.py
   3.	Create file scripts/data_preparation
      a.	Files
         i.	Scripts/data_preparation/prepare_customers_data.py
         ii.	Scripts/data_preparation\prepare_products_data.py
         iii.	Scripts/data_preparation\prepare_sales_data.py
   4.	Create data/prepared folders:
      a.	Customer_prepared.csv
      b.	Products_prepared.csv
      c.	Sales_prepared.csv
P4. Create and Populate DW
   1.	Create new file names etl_to_dw.py and apply script (change to fit your data setup)
   2.	Create folder data/dw
a.	This is where your smart_sales.db will need to be stored 
   3.	Run script to populate data set
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


