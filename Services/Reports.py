from flask import Blueprint,request,jsonify
from BL import dbReports
from HelperClass.commonutil import commonutil
import json
Reports = Blueprint('Reports',__name__)

@Reports.route('/getReports')
def getdepartment():
    try:
        superid = request.args.get('superid')
        reportiid = request.args.get('reportiid')
        StartDate = request.args.get('StartDate',default='null')
        EndDate = request.args.get('EndDate',default='null')
        RegId = request.args.get('RegId',default='null',type=int)
        DeptId = request.args.get('DeptId',default='null',type=int)
        AttendanceStatus = request.args.get('AttendanceStatus',default='null',type=int)
        ShiftId = request.args.get('ShiftId',default='null',type=int)
        BranchId = request.args.get('BranchId',default='null',type=int)

        if superid == None or superid == '':
            cut = commonutil()
            return jsonify(cut.InvalidResult('required superid parameter').__dict__)
        if reportiid == None or reportiid == '':
            cut = commonutil()
            return jsonify(cut.InvalidResult('required reportiid parameter').__dict__)
        if  StartDate == '' or StartDate == None:
            StartDate = 'null'
        else:
            StartDate = f"'{StartDate}'"
        if  EndDate == '' or EndDate == None:
            EndDate = 'null'
        else:
            EndDate = f"'{EndDate}'"

        deptbl = dbReports.ReportsBL()
        result = deptbl.dbgetReports(superid,reportiid,StartDate,EndDate,RegId,DeptId,AttendanceStatus,ShiftId,BranchId)
        return json.dumps(result)
    except Exception as e:
        cut = commonutil()
        return jsonify(cut.InvalidResult(str(e)).__dict__)