import csv

import csv
with open('filled_by_doctors.csv', newline='') as infile:
	with open('processed_filled_by_doctors.csv', 'w', newline='') as outfile:
		reader = csv.DictReader(infile)
		writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['Encounter_Description', 'CC', 'Specialty'])
		for row in reader:
			if (row['CC'] != '' and row['Specialty'] != ''):
				row['CC'] = row['CC'].replace('dyspnea', 'shortness of breath')
				writer.writerow([row['Encounter_Description'], row['CC'], row['Specialty']])