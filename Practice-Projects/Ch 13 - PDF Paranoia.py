#! python3
# PDF_paranoia.py - walks through a set of folders and will find all PDFs then create
# copies that will add encryptions into a new folder
"""
Using the os.walk() function from Chapter 9, write a script that will go through every
PDF in a folder (and its subfolders) and encrypt the PDFs using a password provided on
the command line. Save each encrypted PDF with an _encrypted.pdf suffix added to the
original filename. Before deleting the original file, have the program attempt to read
and decrypt the file to ensure that it was encrypted correctly.

Then, write a program that finds all encrypted PDFs in a folder (and its subfolders)
and creates a decrypted copy of the PDF using a provided password. If the password
is incorrect, the program should print a message to the user and continue to the next
PDF. (see PDF paranoia 2.py)
"""
import os
import PyPDF2
import re
import sys

# Password argument
password = sys.argv[1]

os.chdir(r'C:\Users\tomal\Desktop\pdfs')
path = os.getcwd()

# Normal folder walk.
for folder, subfolders, files in os.walk(path):
    for file in files:
        # You can search multiple .endswith strings if you place them in a tuple
        if file.endswith(('.pdf', '.PDF')):
            # Filter PDF's and and attempt to open each pdf. Remember, to open the pdf you need
            # the full path! so call .join. Also remember to open in 'rb' since there is more than just text
            # Create the pdf_reader as well as the pdf_writer. Then write the encryption using
            # the system argument given
            print('Encrypting ' + file + '...')
            pdf = open(os.path.join(folder, file), 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf)
            pdf_writer = PyPDF2.PdfFileWriter()
            pdf_writer.encrypt(sys.argv[1])
            # Once the pdf is opened, we need to copy each page into the pdf writer by creating
            # a loop and page object
            for page_num in range(pdf_reader.numPages):
                page_obj = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page_obj)
            # Now we need to rename the file. Sub the extension for nothing, then open a new pdf
            # The new name will (join paths!) and add _encrypted.pdf to the end. Remember, this one
            # needs to be in 'wb' since we are writing to the file
            # After writing, close both pdfs and let the loop repeat
            file = re.sub('.pdf', '', file)
            new_pdf = open(os.path.join(folder, file + '_encrypted.pdf'), 'wb')
            pdf_writer.write(new_pdf)
            pdf.close()
            new_pdf.close()

# The second part of the project is trying to open the pdf and ensure its encrypted, then deleting the original
# Walk through the directory with searcing for encrypted.pdf
# We need a try and except statement, because assuming the files were encrypted successfully, opening it
# will cause an PyPDF.utils.PdfReadError.
# If this error occurs, the pdf was encrypted so we can delete the original.
# Use os.remove to delete it INSIDE the except loop. You need to rename the file so you don't delete
# the encrypted ones by mistake
# Note: Don't get confused with being able to successfully call open() on a pdf that is encrypted. This will
# NOT cause an error. The error is caused when you try to obtain a page. So use pdf_reader.getPage(0) to
# try and actually read the pdf.
for folder, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith('encrypted.pdf'):
            pdf = open(os.path.join(folder, file), 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf)
            try:
                page_obj = pdf_reader.getPage(0)
            except PyPDF2.utils.PdfReadError:
                file = re.sub('_encrypted.pdf', '', file)
                print('Deleting %s...' % (os.path.join(folder, file)))
                os.remove(os.path.join(folder, file + '.pdf'))

print('Finished')
