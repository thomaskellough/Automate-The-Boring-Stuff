#! python3
# password breaker - will break into any encrypted PDF document that has
# a password that is one english word
"""
Using the file-reading skills you learned in Chapter 8, create a list of word strings
by reading this file. Then loop over each word in this list, passing it to the decrypt()
method. If this method returns the integer 0, the password was wrong and your program
should continue to the next password. If decrypt() returns 1, then your program should
break out of the loop and print the hacked password. You should try both the uppercase
and lower-case form of each word. (On my laptop, going through all 88,000 uppercase and
lowercase words from the dictionary file takes a couple of minutes. This is why you
shouldn’t use a simple English word for your passwords.)
"""
import PyPDF2

# Same as invitations.py - use read and split each word
text = open('dictionary.txt')
text = text.read()
text = text.split('\n')
# Open the encrypted document and create a reader and writer
pdf = open('watermarkencrypted.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf)
pdf_writer = PyPDF2.PdfFileWriter()

# The loop will begin by iterating over each word in the text document
# I print a message at the beginning so the user knows the program is still running
# since it can take a while for the program to complete, depending on your word.
# Once again, try and except. Same as previous programs
# Inside the try is where we do our magic. As the problem states, if decrypt returns a 1
# then it's a success. Just set an if statement for the word and word.lower == 1 that
# will break out if successful
for word in text:
    print('Trying to break in with ' + word + '...')
    try:
        if pdf_reader.decrypt(word) == 1:
            print('Congratulations! The password was ' + word + '!')
            break
        elif pdf_reader.decrypt(word.lower()) == 1:
            print('Congratulations! The password was ' + word + '!')
            break
    except:
        print('Could not determine the password')


# There is no point in breaking into a PDF if you don't plan on reading it. Use what you
# learned from PDF_paranoia.py to write a new file
for num_page in range(pdf_reader.numPages):
    page_obj = pdf_reader.getPage(num_page)
    pdf_writer.addPage(page_obj)

new_pdf = open('passwordbroken.pdf', 'wb')
pdf_writer.write(new_pdf)
new_pdf.close()
pdf.close()
