import csv
import re
import unicodedata
import os
import glob

# grab the newest csv file in the directory
list_of_files = glob.glob('*.csv')
latest_file = max(list_of_files, key=os.path.getctime)
regexDate = re.split('\.', latest_file)
updated_file = regexDate[0] + '-updated.csv'

# read CSV file into a list
with open(latest_file, newline='', encoding='utf-8') as f:
  reader = csv.reader(f)
  your_list = list(reader)

def checkAuthorities():
	updated_list = []

	authorityLines = len(your_list)
	i=0
	while (i <= authorityLines-1):
    # BIB Heading Before column--normalize to Unicode Normalization Form Canonical Decomposition
		filtered1 = unicodedata.normalize('NFD', your_list[i][6])
    # BIB Heading After column--normalize to Unicode Normalization Form Canonical Decomposition
		filtered2 = unicodedata.normalize('NFD', your_list[i][7])

    # Remove all non-alphanumeric characters
		filtered1 = re.sub(r'[^\w]','',filtered1)
		filtered2 = re.sub(r'[^\w]','',filtered2)

		print(filtered1.encode('utf-8'))
		print(filtered2.encode('utf-8'))

		if (filtered1 == filtered2):
		  print('match!')
      # for testing purposes, so you can see the records being removed from the file
		else: 
		  print('no match!')
		  updated_list.append(your_list[i])
      # if there is an actual change in the heading, add it to the list to outputted
		i += 1

	# save updated file as yyyy-mm-dd-updated.csv
	with open(updated_file, 'w', encoding='utf-8') as myfile1:
	    wr = csv.writer(myfile1, quoting=csv.QUOTE_ALL)
	    wr.writerows(updated_list)
      
	# delete original file
	os.remove(latest_file)

checkAuthorities()
