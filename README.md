🧹 Task 1: Data Cleaning and Preprocessing
📁 Dataset Used:
marketing_campaign.csv
Source: Kaggle Customer Personality Analysis Dataset

✅ Objective:
Clean and prepare a raw marketing dataset for further analysis by addressing issues like:

Missing values

Duplicates

Inconsistent formats

Improper column naming

Incorrect data types

🔧 Tools Used:
Python 3.x

Pandas Library

🔄 Steps Performed:
1. Loaded the Dataset
Read the dataset using pandas.read_csv().

Identified sep='\t' due to tab-separated file structure.

2. Handled Missing Values
Used df.isnull().sum() to identify missing values.

Dropped or imputed missing values using:

Mean/median for numerical columns.

Mode for categorical columns.

Dropped rows where essential fields were missing.

3. Removed Duplicate Rows
Found and removed duplicates using df.drop_duplicates().

4. Standardized Text Values
Cleaned columns like Gender, Education, Marital_Status by:

Removing extra spaces.

Converting all to lowercase/uppercase consistently.

5. Date Format Fix
Converted Dt_Customer column to datetime using pd.to_datetime().

6. Column Name Cleaning
Renamed all columns to lowercase with underscores:

Example: Year_Birth → year_birth

7. Fixed Data Types
Converted appropriate columns:

year_birth to int

income to float

dt_customer to datetime

🧼 Output:
✅ Cleaned Dataset File: cleaned_marketing_campaign.csv

Ready for further EDA, modeling, or visualization.

