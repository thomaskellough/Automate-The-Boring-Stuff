#! python3
# invitations.py - Will import a txt file with a list of names then
# generate a Word document with a specific invitation style
"""
We need to make some syntax changes here for the program to work. In order to add a page break,
you first need to import WD_BREAK from docx.enum.text
Then, after a run, type .add_break(break_type=WD_BREAK.PAGE)
There are more breaks, but this is all we need for this program. I believe Automate The Boring Stuff
has older info that is outdated for this feature
"""
import docx
from docx.enum.text import WD_BREAK


doc = docx.Document('invitation.docx')
# When you open your guest file you need to open it with read() to read each line
# Then, split each line with a new line so you can run a for loop with each name
names = open('guests.txt')
names = names.read()
names = names.split(sep='\n')
# If you are following through with the chapter, this stuff should be fairly easy. Way easier
# than the last couple of projects we have been working on. You will have to guess the style
# that he wants you to have since it's not written down. The part of this program you may forget
# is that you need to first create the a style in the word document, then open the document so
# you can use them. My 'invitation.docx' document is blank, but I have styles saved
# You'll end up saving it to a new document (Note my new name is plural)
# Your style names will be different than mine most likely, so make sure you keep it the same
# as your specific word document. If your document doesn't look like it should but you think your
# program is correct, check the default settings on your Word. I had to adjust mine to make
# it look correct.
for name in names:
    doc.add_paragraph('It would be a pleasure to have the company of').style = 'inviteStyleLine1'
    doc.add_paragraph(name).style = 'Name'
    doc.add_paragraph('at 11010 Memory Lane on the Evening of').style = 'inviteStyleLine2'
    doc.add_paragraph('April 1st').style = 'invitedate'
    date_line = doc.add_paragraph('at 7 o\'clock')
    date_line.runs[0].add_break(break_type=WD_BREAK.PAGE)
    date_line.style = 'inviteStyleLine2'

doc.save('invitations.docx')
