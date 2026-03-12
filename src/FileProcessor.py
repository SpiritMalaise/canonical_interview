from __future__ import annotations
from json import dump

from werkzeug.datastructures.file_storage import FileStorage

def processFile(file: FileStorage) -> tuple[str, int]:
	"""
	Takes a file and processes the contents
	"""
	file.seek(0)
	filestring = file.read().decode('utf-8').splitlines()
	revenue, expenses = extractValues(filestring)
	result = formatResult(revenue, expenses)
	saveResult(result)
	return 'OK', 200

def extractValues(file) -> tuple[float,float]:
	revenue = 0
	expenses = 0

	for row in file:
		# Ignore rows that don't conform to expected length
		row = row.split(', ')
		if len(row) == 4:
			row = formatInput(row)
			if row[1] == 'income':
				revenue += float(row[2])
			elif row[1] == 'expense':
				expenses += float(row[2])
			else:
				continue
		else:
			continue
		
	return revenue, expenses

def formatInput(row: list) -> list:
	for index, item in enumerate(row):
		row[index] = item.strip().lower()
	return row

def formatResult(revenue: float, expenses: float) -> dict[str, float]:
	return {
		"gross-revenue": round(revenue,2),
		"expenses": round(expenses,2),
		"net-revenue": round(revenue - expenses,2)
	}

def saveResult(result: dict):
	with open('./data/result.json', 'w+') as output:
		dump(result, output)