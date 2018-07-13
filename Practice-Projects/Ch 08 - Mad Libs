#! python3
# mad_libs.py
"""
Create a Mad Libs program that reads in text files and lets users add their own text anywhere
the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
"""
import re


# Writes the madlib to a new text file
mad_text = open('madlibs.txt', 'r')
mad_libs = mad_text.read()
print(mad_libs)

# Regex for adjective, noun, adverb, and verb
adjective_regex = re.compile('ADJECTIVE')
noun_regex = re.compile('NOUN')
adverb_regex = re.compile('ADVERB')
verb_regex = re.compile('VERB')

# The program iterates through the sentence imported by the user and if it runs into an adjective,
# noun, adverb, or verb it has the user input a word to replace these.
# Each word is subbed with a new word until its complete. Note: I'm not sure if the book goes over
# the third argument in sub. If you leave the third argument out, it will replace all matches.
# However, you can add 1 as a third argument to replace only the first occurence. This is why the
# while loop will loop continuously until there are no more matches.
while adjective_regex.search(mad_libs) is not None:
    adjective = input('Please enter an adjective:\n')
    mad_libs = adjective_regex.sub(adjective, mad_libs, 1)
while noun_regex.search(mad_libs) is not None:
    noun = input('Please enter a noun:\n')
    mad_libs = noun_regex.sub(noun, mad_libs, 1)
while adverb_regex.search(mad_libs) is not None:
    adverb = input('Please enter an adverb:\n')
    mad_libs = adverb_regex.sub(adverb, mad_libs, 1)
while verb_regex.search(mad_libs) is not None:
    verb = input('Please enter a verb:\n')
    mad_libs = verb_regex.sub(verb, mad_libs, 1)

# Saves the mad_libs to a new text file
new_text = open('new_mad_lib.txt', 'w')
new_text.write(mad_libs)
new_text.close()
mad_text.close()
print(mad_libs)
