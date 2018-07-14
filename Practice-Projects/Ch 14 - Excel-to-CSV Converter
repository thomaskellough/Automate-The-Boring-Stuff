#! python3
# excel_to_csv.py - Converts all Excel files in a working directory into CSV files
# (Includes every sheet in a single Excel file)

import openpyxl
import csv
import os
import re
import shutil
"""
This first block is for setting up. The idea is to create two new directories so you are working with
clean areas. However, you can just edit these settings to your personal preference
"""
# Set your working directory. I created a new one with using selective_copy.py and imported
# a bunch of excel spreadsheets. (Look, we are already using the programs we've written!)
os.chdir(r'C:\Users\tomal\Desktop\excel')
# Create a variable of this directory for use later with shutil
path = os.getcwd()
# Create a new directory inside the previously created directory. This is where we will store our
# new csv files. Once again, this is all arbitrary and you can do as you please
os.makedirs('csv_files', exist_ok=True)
# Create a variable of this directory to use later with shutil (in conjuction with path)
new_path = path + '\\' + 'csv_files'


"""
This next block is reading the excel file, creating new csv files, then copying the excel
files into the new csv files.
"""
for excel_file in os.listdir('.'):
    # Skip the non-xlsx files, load the workbook object
    if not excel_file.endswith('xlsx'):
        continue
    workbook = openpyxl.load_workbook(excel_file)
    # Loop through every sheet in the workbook
    for sheets in workbook.sheetnames:  # Notice, this syntax is different than in the book
        wb_name = re.sub('.xlsx', '', excel_file)   # remove the extension to clean up the name
        csv_name = wb_name + '_' + sheets + '.csv'  # This is the name of the newly created csv file
        # Open your csv file and create your writer object
        csv_file = open(csv_name, 'w', newline='')
        csv_writer = csv.writer(csv_file)
        sheet = workbook.active
        # The first part of the loop. It creates a new list for each row in each sheet
        for row_num in range(1, sheet.max_row + 1):
            row_data = []
            # You want to use the list created above to append each cell value through each column
            for col_num in range(1, sheet.max_column + 1):
                cell_data = sheet.cell(row=row_num, column=col_num).value
                row_data.append(cell_data)
            # This is the write step, it will only write once the entire row is completed
            csv_writer.writerow(row_data)  # Watch the indent!
        # Close and move your csv file to the new directory. Then the loop will start over with the next excel sheet
        csv_file.close()  # Watch the indent!
        shutil.move(os.path.join(path, csv_name), os.path.join(new_path, csv_name))

print('Finished')
