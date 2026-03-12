# Setup
Run the following commands to set up the environment:
```bash
python3 -m venv .venv
. .venv/bin/activate
pip install flask
```

# Tests
From the root of the project run `python -m unittest -v`

# Running the Solution
From the root of the project run the following
```bash
flask run
```
You can then run from another terminal/location
```bash
	curl -F "data=@summer-break/data.csv" http://127.0.0.1:5000/transactions
```
On success this will return an OK response, you can then navigate to [here](http://127.0.0.1:5000/report) or run the following command to recieve the report from the input data.
```bash
	curl http://127.0.0.1:5000/report
```
If you the result data cannot be found a message will be given informing that the transactions must be uploaded first.

# Assumptions
I have made the following assumptions
- The file being uploaded will be called "data"
- Only one file is uploaded at a time
- The file has no header row
- Some rows can be excluded due to not being in the appropriate format

# Shortcomings
This solution is very to the point meeting the requirements required without any assumptions regarding functionality, user experience or potential future development

# Suggestions
With more time and perhaps extension of the requirements I would have like to have done the following:
- Using docker create more robust application with the addition of a database (i.e PostgreSQL) and simple front end (React + Nginx) to allow the following
	- Portability
	- Ease of use (No command line)
	- Data retention with additional functionality for reporting/querying of the data (Structured data)
- Additional data validation on inputs
- Support for upload of multiple files at once