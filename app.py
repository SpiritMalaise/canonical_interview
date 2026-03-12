from flask import Flask, request
from json import load

from src import FileProcessor

app = Flask(__name__)

@app.route("/health")
def health_check():
	return  'OK', 200

@app.post("/transactions")
def transactions():
	return FileProcessor.processFile(request.files['data'])

@app.get("/report")
def report():
	try:
		with open('./data/result.json') as file:
			return load(file)
	except Exception as e:
		return "Missing results file, have you uploaded your transactions?", 406