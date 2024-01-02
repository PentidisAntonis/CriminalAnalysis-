# Criminal Analysis Project

Welcome to the Criminal Analysis project! This project aims to make an interactive app for statistical analysis in regards to the Mother John shootings in USA.

## Prerequisites

Before you can run this project, you need to have Python, pandas, and openpyxl installed on your machine.

### 1. Install Python

If you don't have Python installed, you can download and install it from the official Python website: [Python Downloads](https://www.python.org/downloads/)

Ensure that you check the option to add Python to your system PATH during the installation process.

### 2. Install pandas

Once Python is installed, you can install the pandas library using pip, the Python package installer. Open a terminal or command prompt and run the following command:

>pip install pandas

### 3. Install openpyxl

>pip install openpyxl


### 4. Download from the venv file the Mother Jones - Mass Shootings Database, 1982 - 2019.xlsx


### 5. CriminalMain.py

The CriminalMain.py script is the initial component of this project. It performs the following tasks:

Reads data from an Excel file containing information on mass shootings.
Creates a new Excel workbook and removes unnecessary columns from the original dataset.
Saves the modified data to a new Excel file named modified_file.xlsx.
Reads the modified data into a new DataFrame for further analysis.

To run the CriminalMain.py script, navigate to the project directory and execute the following command in your terminal or command prompt:

>python CriminalMain.py

This script sets up the data for analysis in the subsequent criminalsecond.py script.

### 6. criminalsecond.py

The criminalsecond.py script continues the analysis by:

Standardizing categorical columns.
Transforming categorical column values for better understanding.
Calculating descriptive statistics for numerical columns.
Providing user interaction to explore statistics for specific columns.

To run the criminalsecond.py script, ensure you have already executed CriminalMain.py. Then, execute the following command:

>python criminalsecond.py
