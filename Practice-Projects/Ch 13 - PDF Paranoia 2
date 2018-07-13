#! python3
# PDF_paranoia.py - walks through a set of folders and will find all PDFs then create
# copies that will add encryptions into a new folder
"""
Using the os.walk() function from Chapter 9, write a script that will go through every
PDF in a folder (and its subfolders) and encrypt the PDFs using a password provided on
the command line. Save each encrypted PDF with an _encrypted.pdf suffix added to the
original filename. Before deleting the original file, have the program attempt to read
and decrypt the file to ensure that it was encrypted correctly. (see PDF_paranoia.py)

Then, write a program that finds all encrypted PDFs in a folder (and its subfolders)
and creates a decrypted copy of the PDF using a provided password. If the password
is incorrect, the program should print a message to the user and continue to the next
PDF.
"""
import os
import PyPDF2
import re
import pprint

os.chdir(r'C:\Users\tomal\Desktop\pdfs')
path = os.getcwd()

# I created an empty list here just for the purpose of having a pprint at the end of the program
# It's not necessary for the program to run successfully
pdf_list = []

# This one is a bit tricky, we need to put a try and except statement INSIDE another try
# and except statement. The problem states we need to find all encrypted pdfs. So we first
# want to try and open a pdf (like in PDF_paranoia.py). If we can open it, it's not encrypted,
# so we are finished with the first try. If we cannot open it, it's encryptd. So the rest of our
# program will go inside the except statement.
# Start another try statement
# Let's try to decrypt the pdf with a password (you can use a sys.argv if you want, this program
# just has one typed in).
# Use pdf_reader.decrypt() with the password as the argument. Then try to use pdf_reader.getPage(0)
# If we can't get it, the password is wrong. In the new except statement, print a message saying
# that the file can't be decrypted.
# If we are successful in using get.Page(0), continue the rest of the program with creating a decrypted
# file. See PDF_paranoia.py for an explanation of this.
# If you used the pdf_list, you will need to append the file at after closing the documents,
# then print it out at the end showing which files were decrypted.
for folder, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith(('.pdf', '.PDF')):
            try:
                pdf = open(os.path.join(folder, file), 'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf)
                pdf_reader.getPage(0)
            except PyPDF2.utils.PdfReadError:
                try:
                    pdf = open(os.path.join(folder, file), 'rb')
                    print(os.path.join(folder, file))
                    pdf_reader = PyPDF2.PdfFileReader(pdf)
                    pdf_reader.decrypt('rosebud')
                    pdf_reader.getPage(0)
                    print('Decrypting %s...' % file)
                    pdf_writer = PyPDF2.PdfFileWriter()
                    for page_num in range(0, pdf_reader.numPages):
                        page_obj = pdf_reader.getPage(page_num)
                        pdf_writer.addPage(page_obj)
                    new_name = re.sub('_encrypted', '_decrypted', file)
                    new_pdf = open(os.path.join(folder, new_name), 'wb')
                    pdf_writer.write(new_pdf)
                    pdf.close()
                    new_pdf.close()
                    pdf_list.append(file)
                except PyPDF2.utils.PdfReadError:
                    print('Could not decrypt %s' % file)

print('Successfully decrypted the following:')
pprint.pprint(pdf_list)
