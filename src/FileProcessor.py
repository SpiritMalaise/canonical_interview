from __future__ import annotations
from json import dump

from werkzeug.datastructures.file_storage import FileStorage

def processFile(file: FileStorage) -> tuple[str, int]:
	revenue = 0
	expenses = 0

	file.seek(0)
	bytestring = file.read()
	for row in bytestring.decode('utf-8').splitlines():
		# Ignore rows that don't conform to expected length or types
		row = row.split(', ')
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
		"expenses": round(expenses,2),
		"net-revenue": round(revenue - expenses,2)
	}
	
	with open('./data/result.json', 'w+') as output:
		dump(result, output)
	return 'OK', 200
