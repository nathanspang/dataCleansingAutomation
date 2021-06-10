# creating an automation system for basic CSV file data cleansing

import pandas as pd
from classes import DataSheet

print("--------------- Data Cleansing Automation Script ---------------")
print()
print("Welcome to the Data Cleansing Automation Script 1.0")
print()
file_placed = input("Have you placed the pre-cleansed CSV into the parent folder? (Y/N) ")
print()

if file_placed.upper() == "Y":
    file_name = input("Please enter the file name including .csv: ")
else:
    print("Please place the file into the parent folder and restart the script!")

orig_data = pd.read_csv(file_name)
sheet = DataSheet(orig_data)
sheet.get_cols()
