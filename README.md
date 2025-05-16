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
   
3.  NOTES
   *  All information is for Windows users only
   * Ran into an issue with python script because there was a space in logger.py which made it so the system couldn't find the pathway to run the scripts
     *  NOTE: Double check file names
     *  FAKE DATA
        *  When you fake data, you can be creative- missing information, values that are outside acceptable ranges, and/or perfectly clean data. It is best to start with simple, clean data, and AFTER everything is working, go back and modify the fake data to make your analysis more challenging.
         *  Avoid spacing in new column titles
         *  Follow existing naming conventions - use the pattern already provided in your data tables.
   
4.  USEFUL TOOLS
   1. ChatGPT - helpful tool to understanding processes & visualizing steps required.  Provides additional commands for troubleshooting
