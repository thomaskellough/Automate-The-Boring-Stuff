import os

os.chdir(r'C:\Users\tomal\Desktop\pdfs')
path = os.getcwd()
for folder, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith('encrypted.pdf'):
            os.remove(os.path.join(folder, file))
