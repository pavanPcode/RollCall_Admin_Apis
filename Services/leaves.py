from flask import Blueprint,request,jsonify
from BL import dbleaves
from HelperClass.commonutil import commonutil
from datetime import datetime
import json
from HelperClass.commonutil import commonutil
import datetime as DT

cutil = commonutil()

leaves = Blueprint('leaves',__name__)


@leaves.route("/getleaveaccruals")
def getleaveaccruals():
    try:
        regid = request.args.get('regid')
        leavebl = dbleaves.LeaveBL()
        retrows = leavebl.leaveaccruals(int(regid))
        return json.dumps(retrows.__dict__,default=str)
    except Exception as e:
        retmdl = cutil.InvalidResult(f"Error occured : {str(e)}")
        return json.dumps(retmdl.__dict__,default=str)

@leaves.route("/getleavetype")
def getleavetype():
    try:
        superid = request.args.get('superid')
        leavebl = dbleaves.LeaveBL()
        retrows = leavebl.leavetypes(int(superid))
        return json.dumps(retrows.__dict__,default=str)
    except Exception as e:
        retmdl = cutil.InvalidResult(f"Error occured : {str(e)}")
        return json.dumps(retmdl.__dict__,default=str)

@leaves.route("/getempleaves")
def getempleaves():
    try:
        regid = request.args.get("regid", default=0, type=int)
        status = request.args.get("status", default=0, type=int)
        year = request.args.get("year", default=DT.date.today().year, type=int)
        leavebl = dbleaves.LeaveBL()
        retrows = leavebl.empleaves(int(regid),status,year)
        return json.dumps(retrows.__dict__,default=str)
    except Exception as e:
        retmdl = cutil.InvalidResult(f"Error occured : {str(e)}")
        return json.dumps(retmdl.__dict__,default=str)