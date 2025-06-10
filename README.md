# store-smart-shelayne-smith

1. UNDERSTANDING & SET-UP FOLDERS/FILES
   * .gitignore: File lists content that doesn't need to be tracked in the project history
   * requirements.txt: lists all the packages the project needs
     * Lines starting with a hash are ignored when installing packages using this file
   * .venv -virtual environment in Python: self-containing environent that includes its own Python interpreter,   pip, and libraries. Helps manage dependencies per project, so they don't interfere with other projects or system-wide Python.
   * demo_notebook.ipynb: demonstrates how your project works using an interactive, easy-to-follow format (typically in Jupyter Notebook)
   * demo_script.py: A very simple Python script to demonstrate basic features
   * utils_logger.py: This script provides logging functions for a project.  Essential way to track events and issues during execution.
   * Markdown cells: turn your input into clean, readable text like you'd see in a report.  It's helpful for adding notes, explanations, or even formatting your notebook like a guide. 
    
2. COMMANDS
   * Change pathway from Repo Folder to store-smart-shelayne-smith
     1. File - Open Folder - Navigate to store-smart-shelayne-smith within File Explorer and select
   * Use cd - enter file you want to be in to sync in terminal for correct folder pathway
   * To Commit Changes
      *  Go to Source Control
      * Click the + icon next to the files you want to commit
      * Commit
      * Type a message in the message box : ex. add updates to README.mD
   * Push/Pull to GitHub
   * Three commands to utilize after each small change
    1.  git add . -Any new files to source control (so the new files will be tracked)
    2.  git commit -m "Update README.md with command"-set of changes to the git project repository with a message telling what you did.
    3.  git push -that named set of changes (called a commit) up to GitHub for safe keeping.
      * Source Control Panel
      * click on ... select push
      * OR open a* terminal and run: git push origin main
   * git pull -pull information into local from GitHub
     * Source Control Panel 
     * click on ... select pull
     * OR open a terminal and run :git pull origin main
   * Activate .venv - .venv\Scripts\activate
   * External Dependencies - Libraries, packages,and modules beyond the standard library & include common packages (ex. pandas).  These must be istalled in our local project vitual environment to use the in our code.
     * Activate .venv
     * Update key packages
     * Install dependencies from the requirements.txt file
     * run commands
       * .\.venv\Scripts\activate
       * py -m pip install --upgrade pip setuptools wheel
       * py -m pip install -r requirements.txt
   * Module 3 scripts (update to run correctly)
     * py scripts/data_preparation/prepare_customers_data.py
     * py scripts/data_preparation/prepare_products_data.py
     * py scripts/data_preparation/prepare_sales_data.py
   * Module 4 script
     * python scripts/etl_to_dw.py (successful)
   * Module 5 Command 
     * ![Alt text](data/dw/images/selectanimage): This is the correct pathway to add actual images to README.md to have images display
   
3.  NOTES
   *  All information is for Windows users only
   * Ran into an issue with python script because there was a space in logger.py which made it so the system couldn't find the pathway to run the scripts
     *  NOTE: Double check file names
     *  FAKE DATA
        *  When you fake data, you can be creative- missing information, values that are outside acceptable ranges, and/or perfectly clean data. It is best to start with simple, clean data, and AFTER everything is working, go back and modify the fake data to make your analysis more challenging.
         *  Avoid spacing in new column titles
         *  Follow existing naming conventions - use the pattern already provided in your data tables.
   *  D3-Notes
      *  Ran test script py tests\test_data_scrubber.py, received error No module names 'utils'.  It means Python cannot find the utils folder in your project when trying to import something like: from utils.logger import logger.  
      *  Fixes:
         *  Option 1: Add the project root to sys.path
            *  At the top of your Python script or test file, add:
               *  imports sys
               *  import pathlib
               *  # Add the root directory of your project to the system path
               *  sys.path.append(str(pathlib.path(__file__).resolve().parent.parent))
               *  If your test file is in tests/test_data_scrubber.py, this goes at the top of that file.
         *  Option 2
            *  Run the script from the project root (this is what I used to run test successfully)
               *  Instead of python tests/test_data_scrubber.py, do python -m tests.test_data_scrubber
                  *  Note: Make sure you are in your project root folder when running this.
   *  P4. Create and Populate DW
      *  Double check spelling of column names
         *  Issue: incorrect column name titles caused errors when creating dw. verify and review all column names and make corrections.
         *  Issue: conn: did not have the correct pathway and was causing sqlite3.OperationalError: unable to open database file.  Put code into ChatGPT to get the conn: to the right pathway.  
            *  Additional details on entering information into ChatGPT provided below in USEFUL TOOLS.
   *  P5. Cross-Platform Reporting with Power BI & Spark
      *  SQL Queries and Reporting using Power BI
         *  Slicing: Filter the data to view a single layer based on one dimension
            *  Created slicer for total sales amount per region for each product.  Slicer allows for filtering down to sales amount for a single product per region, and a single region with totals for each product.
         *  Dicing: Similar to slicing, but on multiple dimensions, creates a subcube from the larger dataset.
            *  Creating a report that joins sales with customers and products tables (dimensions tables) which produces data showing the top performs.
         *  Drilldown: Moving from a summary view to more detailed data, while drill-up is the reverse.
            *  Create drilldown by implementing year.  Our data is for one specific date, so we will not be able to drill down to a quarterly/monthly/weekly/daily basis.
      *  Dashboard Design
         *  Implemented drilldown to allow for data to be aggregated view sales trends.
         *  Created chart with product category, and region for axis; applied sales amount to compare which region had the highest total  sales ($). Provided slicer to filter data down to a single product to determine which region is selling the most of each product.
         *  Allow drilldown from region to store level for additional insight.
   *  P6. BI Insights & Storytelling
            1. The Business Goal: Clearly state the exact question being addressed and why it matters
               * What is the most profitable product by region for the last year? Which is the most profitable store in each region?
                 * Descriptive dimensions: Product, Region, StoreID
                 * Numeric metric: Total Sales
                 * Aggregation: SUM
                 * Slicing: Total sales by product
                 * Dicing: Product by region
                 * Drill-down: total sales by product by region by store
            2. Data Source:
               * What information did you start with? Prepared Data
               * Clearly indicate which column of which tables were used.
                 * Tables: Sales, Products, region, sales
                 * Columns: product_category, region, sale_amount, store_id  
                 * Workflow: 
                   * Aggregate: Product Category
                   * Calculate total sales for the year per product by region
                   * Drilldown data to store id
            3. Tell us what tools you used and why: OLAP cube script to generate CSV with required columns. Power BI, to provide data visualization and slicing, dicing, and drilldown/rollup.Images and Power BI file with tables and drilldown attached below
            4. Workflow & Logic
               *First, created and ran olap_cubing.py script to generate multidimensional_olap_cube.csv file with all required columns
               * Used Power BI to slice,dice, and drill down to determine total sales per product per region per store. 
                 * Matrix table shows sales per product for each region and total sales. Legends to allow filtering down to specific product and/or region for indepth analysis specific to product(s) and/or region(s)
                 * Create drill down at a product and/or region level for data analysis for each store within a region.
                 * Incorporated Stacked column chart to visualized total sales per product per region to determine which products on a percentage ratio accounted for the most sales in each region.   
               * ![Alt text](data/dw/images/P6.%20Power%20BI%20image.PNG)
            5.Results

               *Low performing region- Central / High performing region- East 
               *Low selling product- office (marginally) / High selling product- Home 
               * REFERENCE and pull Power BI file.pbix to use interactive data in Power BI.  Located in the smart-store-shelayne-smith Repo.

            5. Suggested Business Action
               * Determine what marketing strategies or specific electronic, home, office, and clothing items are the biggest sellers for the Eastern region, and implement those marketing strategies in other regions to increase total sales.  
               * Evaluate inventory for office supplies to determine which products are underperforming and bring in inventory that is selling or alternative products to increase sales in office products.
               * Create complimentary products between office/home and electronics.  To increase sales for complimentary products.
               * Evaluate region specific clothing items that are relevant to the region to increase sales of clothing products.
             
            6. Challenges
               * Removing inconsistent duplicated data correctly.
               * Getting the correct script format to successfully run olap_cube.py
                 * Used ChatGPT to help clean up script to pull correct information and generate olaps outputs 
4.   USEFUL TOOLS
   * ChatGPT - helpful tool to understanding processes & visualizing steps required.  Provides additional commands for troubleshooting
      * P4. Create and Populate DW
         * Provide ChatGPT with error message, then provide entire code within etl_to_dw.py
         * Follow instructions carefully to resolve issues within code. Insert below def load_data_to_db() -> None:
            * X conn is not defined inside the with block
               * with sqlite3.connect(DB_PATH):
               * cursor = conn.cursor()
            * Fix
               * with sqlite3.connect(DB_PATH) as conn:
               * cursor = conn.cursor()
               * add DW_DIR.mkdir(parent=True, exist_ok=True) before with sqlite3.connect(DB_PATH) as conn:
5. SCREENSHOTS
      ![Alt text](data/dw/images/CUSTOMERDW.PNG)
      ![Alt text](data/dw/images/PRODUCTSDW-1.PNG)
      ![Alt text](data/dw/images/SALESDW.PNG)
   P.5 Screenshots
      ![Alt text](data/dw/images/Top%20Customer.PNG)
      ![Alt text](data/dw/images/Total%20Sales.PNG)
      ![Alt text](data/dw/images/Slicer.PNG)
      ![Alt text](data/dw/images/Product%20Sales%20by%20region.PNG)