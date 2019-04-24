#! python3
# A program designed to quickly zip a file


import os
import zipfile


while True:
	zip_file = input('What file would you like to zip?\n')
	wd = input('Where would you like to zip ' + zip_file + ' to?\n')
	while True:
		try: 
			os.chdir(wd)
			break
		except:
			print('Cannot find directory.\nPlease enter another.\n')
			wd = input()
			continue
	try:
		zipped_file = zipfile.ZipFile(zip_file + '.zip')
		zipped_file.extractall()
		zipped_file.close()
		print(zip_file + 'has been successfully zipped.')
		break
	except FileNotFoundError:
		print('There is no file by that name to zip.')
		continue

