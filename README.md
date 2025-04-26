
Online Store Data Analysis
This repository contains a Python script that processes and analyzes data from an online store. The dataset includes information about various products such as product_name, price, quantity_sold, category, and more.

The script performs several data cleaning and transformation steps, followed by analysis to generate insights such as the highest and lowest revenue-generating products in specific categories.

Requirements
Make sure you have the following libraries installed:

pandas,
numpy

You can install them using:

pip install pandas numpy

Steps Performed in the Script

Data Import and Initial Overview:

The script starts by reading the dataset from a CSV file named online_store_data.csv.

The shape of the DataFrame (number of rows and columns) is printed for a quick overview.

Data Transformation:

Column Conversion:

Converts quantity_sold and num_of_ratings columns to integer type (Int32).

Converts quantity_in_stock to numeric values, handling cases like 'out_of_stock' using pd.to_numeric().

Date Parsing:

Converts the date_added column to a proper datetime format for easier analysis.

Handling Ratings:

A custom function parse_rating() is defined to clean the rating column, converting it to numeric values (floating-point numbers) or NaN if there are invalid or missing ratings.

Missing Data Handling:

Rows with missing product_name values are identified and dropped.

Rows with more than 4 missing columns are also removed to keep the dataset clean.

Removing Duplicates:

Duplicates in the dataset are removed based on the product_name, keeping only the first occurrence.

Revenue Calculation:

A new column revenue is created by multiplying price with quantity_sold for each product.

Product Analysis:

The script identifies the Top 10 revenue-generating keyboards by filtering products in the Keyboards category and sorting them by the revenue.

Similarly, it identifies the Top 10 low-revenue TVs by filtering products in the TVs category and sorting them by the revenue in ascending order.

Example Outputs
1. Tastaturile cu cel mai mare venit:
Displays the 10 products from the Keyboards category with the highest revenue.

2. Televizoarele cu cel mai mic venit:
Displays the 10 products from the TVs category with the lowest revenue.

Conclusion
This project demonstrates a straightforward approach to data cleaning, transformation, and analysis using Python and pandas. It helps in deriving useful insights from an online store dataset, focusing on product performance based on sales and revenue.

How to Use
Clone this repository.

Place your CSV file (online_store_data.csv) in the same directory as the script.

Run the script using Python:

python online_store_data_analysis.py
