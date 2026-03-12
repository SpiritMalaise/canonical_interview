from flask import Flask

app = Flask(__name__)

@app.route("/health")
def health_check():
	return  'OK', 200

@app.post("/transactions")
def transactions():
	return "Not Yet Implemented", 501

@app.get("/report")
def report():
	return "Not Yet Implemented", 501