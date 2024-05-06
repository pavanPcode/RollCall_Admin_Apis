from flask import Blueprint,request,jsonify
from BL import dbdashboard
from HelperClass.commonutil import commonutil

dashboard = Blueprint('dashboard',__name__)



@dashboard.route('/getDashboardAttendance')
def DashboardAttendance():
    superid = request.args.get('superid')
    InStatus = request.args.get('InStatus')
    if superid == None:
        cut = commonutil()
        return jsonify(cut.InvalidResult('required superid parameter').__dict__)
    if InStatus == None:
        cut = commonutil()
        return jsonify(cut.InvalidResult('required InStatus parameter').__dict__)
    branchbl = dbdashboard.dashboardBL()
    result = branchbl.dbgetDashboardAttendance(superid,InStatus)
    return jsonify(result)

@dashboard.route('/getdashboardcount')
def getdashboardcount():
    superid = request.args.get('superid')
    if superid == None:
        cut = commonutil()
        return jsonify(cut.InvalidResult('required superid parameter').__dict__)
    branchbl = dbdashboard.dashboardBL()
    result = branchbl.dbgetdashboardcount(superid)
    return jsonify(result)
