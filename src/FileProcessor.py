from __future__ import annotations
from json import dump
import csv

def processFile(file: FileStorage):
	fieldnames = ['Date', 'Type', 'Amount($)', 'Memo']
	filepath = './uploads/'

	# Save the file to a processing location
	file.save(filepath + 'processing_data.csv')

	revenue = 0
	expenses = 0
	with open(filepath + 'processing_data.csv') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			# Ignore rows that don't conform to expected length or types
			if len(row) == 4:
				for index, item in enumerate(row):
					row[index] = item.strip().lower()
				if row[1] == 'income':
					revenue += float(row[2])
				elif row[1] == 'expense':
					expenses += float(row[2])
			else:
				continue

	result = {
		"gross-revenue": round(revenue,2),
		"expenses": round(expenses),
		"net-revenue": round(revenue - expenses)
	}
	
	with open(filepath + 'result.json', 'x') as file:
		dump(result, file)
	return 'OK', 200
