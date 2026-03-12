from flask import Flask, request
from src import FileProcessor

app = Flask(__name__)

data_store = {}

@app.route("/health")
def health_check():
	return  'OK', 200

@app.post("/transactions")
def transactions():
	return FileProcessor.processFiles(request.files)

@app.get("/report")
def report():
	return "Not Yet Implemented", 501