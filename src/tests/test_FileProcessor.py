import unittest

from src import FileProcessor as fp

class TestFileProcessor(unittest.TestCase):
	def setUp(self):
		self.file_string = """2020-07-01, Expense, 18.77, Gas
			2020-07-04, Income, 40.00, 347 Woodrow
			2020-07-06, Income, 35.00, 219 Pleasant
			2020-07-12, Expense, 49.50, Repairs"""

	def test_formatInput(self):
		test_value = self.file_string.splitlines()[0].split(', ')
		result = fp.formatInput(test_value)
		self.assertEqual(result, ['2020-07-01', 'expense', '18.77', 'gas'])

	def test_formatResult(self):
		result = fp.formatResult(10.50,12.25)
		self.assertIsInstance(result,dict)
		self.assertEqual(result.get("gross-revenue"),10.50)
		self.assertEqual(result.get("expenses"),12.25)
		self.assertEqual(result.get("net-revenue"),-1.75)

	def test_extractValues(self):
		test_value = self.file_string.splitlines()
		revenue, expenses = fp.extractValues(test_value)
		self.assertEqual(revenue,75.00)
		self.assertEqual(expenses,68.27)

	def test_saveResult(self):
		import os
		from json import load

		test_value = self.file_string.splitlines()
		revenue, expenses = fp.extractValues(test_value)
		result = fp.formatResult(revenue, expenses)
		fp.saveResult(result)

		file_path = './data/result.json'
		with open(file_path) as file:
			data = load(file)
			self.assertEqual(data.get("gross-revenue"),75.00)
			self.assertEqual(data.get("expenses"),68.27)
			self.assertEqual(data.get("net-revenue"),6.73)
		if os.path.exists(file_path):
			os.remove(file_path)

if __name__ == '__main__':
	unittest.main()