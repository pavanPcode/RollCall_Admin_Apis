from flask import Flask, jsonify,request
from flask_cors import CORS
import requests
from datetime import datetime
import logging
from Services import Holidays,Reports,Branch,Department,Registration,signin,Team,Termination,Shifts
app = Flask(__name__)

CORS(app)

@app.route('/')
def ServiceHealth():
    return jsonify('RollCall Admin Service Is Up')

app.register_blueprint(signin.Signin,url_prefix='/rcadmin/signin')
app.register_blueprint(Holidays.Holidays,url_prefix='/rcadmin/holidays')
app.register_blueprint(Reports.Reports,url_prefix='/rcadmin/reports')
app.register_blueprint(Branch.branch,url_prefix='/rcadmin/branch')
app.register_blueprint(Department.Department,url_prefix='/rcadmin/department')
app.register_blueprint(Registration.Registration,url_prefix='/rcadmin/registration')
app.register_blueprint(Team.Team,url_prefix='/rcadmin/team')
app.register_blueprint(Termination.Termination,url_prefix='/rcadmin/termination')
app.register_blueprint(Shifts.Shifts,url_prefix='/rcadmin/shifts')


if __name__ == "__main__":
    app.run()
