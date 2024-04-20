from flask import Flask, jsonify,request
from flask_cors import CORS
import requests
from datetime import datetime
import logging
from Services import Holidays,Reports,Branch
app = Flask(__name__)

CORS(app)

@app.route('/')
def ServiceHealth():
    return jsonify('Service Is Up')



app.register_blueprint(Holidays.Holidays,url_prefix='/rcadmin/holidays')
app.register_blueprint(Reports.Reports,url_prefix='/rcadmin/reports')
app.register_blueprint(Branch.branch,url_prefix='/rcadmin/branch')


if __name__ == "__main__":
    app.run(debug=True)
