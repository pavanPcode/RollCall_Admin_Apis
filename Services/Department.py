from flask import Blueprint,request,jsonify
from BL import dbdepartment
from HelperClass.commonutil import commonutil

Department = Blueprint('Department',__name__)

@Department.route('/createdepartment',methods = ['Post'])
def createdepartment():
    data = request.json
    deptbl = dbdepartment.DepartmentBL()
    result = deptbl.dbcreatedepartment(data)
    return jsonify(result)

@Department.route('/updatedepartment',methods = ['Post'])
def updatedepartment():
    data = request.json
    deptbl = dbdepartment.DepartmentBL()
    result = deptbl.dbupdatedepartment(data)
    return jsonify(result)

@Department.route('/deletedepartment',methods = ['Post'])
def deletedepartment():
    data = request.json
    deptbl = dbdepartment.DepartmentBL()
    result = deptbl.dbdeletedepartment(data)
    return jsonify(result)

@Department.route('/getdepartment')
def getdepartment():
    superid = request.args.get('superid')
    if superid == None:
        cut = commonutil()
        return jsonify(cut.InvalidResult('required superid parameter').__dict__)
    deptbl = dbdepartment.DepartmentBL()
    result = deptbl.dbgetdepartment(superid)
    return jsonify(result)
