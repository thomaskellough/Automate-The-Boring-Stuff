#! python3
# text to spreadsheet.py - turns txt into a spreadsheet
"""
Write a program to read in the contents of several text files (you can make the text files yourself)
and insert those contents into a spreadsheet, with one line of text per row. The lines of the first
text file will be in the cells of column A, the lines of the second text file will be in the cells
of column B, and so on.

Use the readlines() File object method to return a list of strings, one string per line in the file.
For the first file, output the first line to column 1, row 1. The second line should be written to
column 1, row 2, and so on. The next file that is read with readlines() will be written to column 2,
the next file to column 3, and so on.
"""
import openpyxl
import os
from openpyxl.utils import get_column_letter


wb = openpyxl.Workbook()
sheet = wb.active

# Create an empty list that will contain a list of lists of the txt documents. Then loop
# through the directory and search for any .txt file, open it, with readlines() and append
# it to the list
text_list = []
for text in os.listdir('.'):
    if text.endswith('.txt'):
        text = open(text)
        text_list.append(text.readlines())


# Initialize the column outside the for loop, but the row inside the for loops
col = 1
for text in text_list:
    row = 1
    list_length = []
    for sentence in text:
        # Add the sentence to the cell
        sheet.cell(row=row, column=col).value = sentence
        row += 1
        # These next few lines are optional, but it makes it so the column is
        # adjusted automatically to the longest string. This way you can easily read it in the file.
        # Obtain the length of each string (sentence) and append it to the empty list_length. Set the max
        # length to max(list_length) so it will only overwrite itself if the new string is longer than
        # the current max. Then adjust the dimensions to the max_length. Note: the list length needs to
        # be reset after reading each text file. So put it inside the first loop, but not the second.
        length = len(sentence)
        list_length.append(length)
        max_length = max(list_length)
        col_letter = get_column_letter(col)
        sheet.column_dimensions[col_letter].width = max_length
    # Adding 1 to the column will allow the next text file to be written on the next column
    col += 1

# Save new worksheet
os.chdir(r'c:\users\tomal\desktop')
wb.save('text_to_spreadsheet.xlsx')
