import csv

types = ['FAMILY PRACTICE/PRIMARY CARE', 'CARDIOLOGY', 'PULMONARY DISEASE']
replaces = {'PULMONARY DISEASE': 'CARDIOLOGY', 'dyspnea': 'shortness of breath'}
typeset = {}

import csv
with open('filled_by_doctors.csv', newline='') as infile:
	with open('processed_filled_by_doctors.csv', 'w', newline='') as outfile:
		reader = csv.DictReader(infile)
		writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['Encounter_Description', 'CC', 'Specialty'])
		for row in reader:
			if (row['CC'] != '' and row['Specialty'] != '' and row['Specialty'] in types):
				for key in replaces:
					row['CC'] = row['CC'].replace(key, replaces[key])
					row['Specialty'] = row['Specialty'].replace(key, replaces[key])
					
				if (row['Specialty'] in typeset):
					typeset[row['Specialty']] += 1
				else:
					typeset[row['Specialty']] = 1
				
				if (typeset[row['Specialty']] >= 400): 
					continue
				
				writer.writerow([row['Encounter_Description'], row['CC'], row['Specialty']])
				
print(typeset)