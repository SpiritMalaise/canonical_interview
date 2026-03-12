from __future__ import annotations
import csv

def processFiles(files: list(FileStorage)) -> dict:
	for file in files:
		return processFile(files[file])

def processFile(file: FileStorage):
	fieldnames = ['Date', 'Type', 'Amount($)', 'Memo']
	filepath = './uploads/processing_data.csv'

	# Save the file to a processing location
	file.save(filepath)

	result = []
	with open(filepath) as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			# Ignore rows that don't conform to expected format
			if len(row) == 4:
				for index, item in enumerate(row):
					row[index] = item.strip()
				result.append(row)
		return result
