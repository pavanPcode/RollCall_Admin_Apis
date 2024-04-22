from flask import Blueprint,request,jsonify
from BL import dbshifts
from HelperClass.commonutil import commonutil

Shifts = Blueprint('Shifts',__name__)

@Shifts.route('/assignShifts',methods = ['Post'])
def assignShifts():
    data = request.json
    shiftbl = dbshifts.ShiftsBL()
    result = shiftbl.dbcreateShifts(data)
    return jsonify(result)

@Shifts.route('/getShiftsTypes')
def getShiftsTypes():
    superid = request.args.get('superid')
    if superid == None:
        cut = commonutil()
        return jsonify(cut.InvalidResult('required superid parameter').__dict__)
    shiftbl = dbshifts.ShiftsBL()
    result = shiftbl.dbgetShiftsTypes(superid)
    return jsonify(result)

@Shifts.route('/getAssignshiftByEmp')
def getAssignshiftByEmp():
    regid = request.args.get('regid')
    if regid == None:
        cut = commonutil()
        return jsonify(cut.InvalidResult('required regid parameter').__dict__)
    shiftbl = dbshifts.ShiftsBL()
    result = shiftbl.dbgetAssignshiftByEmp(regid)
    return jsonify(result)