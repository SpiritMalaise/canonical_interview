from flask import Flask

app = Flask(__name__)

@app.route("/health")
def health_check():
	return  'OK', 200

@app.post("/transactions")
def transactions():
	return 501

@app.post("/report")
def transactions():
	return 501