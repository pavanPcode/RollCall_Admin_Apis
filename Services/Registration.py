from flask import Blueprint,request,jsonify
from BL import dbRegistration
from HelperClass.commonutil import commonutil

Registration = Blueprint('Registration',__name__)

@Registration.route('/createEmployee',methods = ['Post'])
def createEmployee():
    data = request.json
    regbl = dbRegistration.EmployeeBL()
    result = regbl.dbcreateEmployee(data)
    return jsonify(result)


@Registration.route('/updateEmployee',methods = ['Post'])
def updateEmployee():
    data = request.json
    regbl = dbRegistration.EmployeeBL()
    result = regbl.dbupdateEmployee(data)
    return jsonify(result)

@Registration.route('/deleteEmployee',methods = ['Post'])
def deleteEmployee():
    data = request.json
    regbl = dbRegistration.EmployeeBL()
    result = regbl.dbdeleteEmployee(data)
    return jsonify(result)

@Registration.route('/getEmployee')
def getEmployee():
    superid = request.args.get('superid')
    regbl = dbRegistration.EmployeeBL()
    result = regbl.dbgetEmployee(superid)
    return jsonify(result)

@Registration.route('/createRegBankDetails',methods = ['Post'])
def createRegBankDetails():
    data = request.json
    regbl = dbRegistration.RegBankDetailsBL()
    result = regbl.dbcreateRegBankDetails(data)
    return jsonify(result)

@Registration.route('/updateRegBankDetails',methods = ['Post'])
def updateRegBankDetails():
    data = request.json
    regbl = dbRegistration.RegBankDetailsBL()
    result = regbl.dbupdateRegBankDetails(data)
    return jsonify(result)

@Registration.route('/getRegBankDetails')
def getRegBankDetails():
    regid = request.args.get('regid')
    regbl = dbRegistration.RegBankDetailsBL()
    result = regbl.dbgetRegBankDetails(regid)
    return jsonify(result)
@Registration.route('/deleteRegBankDetails',methods = ['Post'])
def deleteRegBankDetails():
    data = request.json
    regbl = dbRegistration.RegBankDetailsBL()
    result = regbl.dbdeleteRegBankDetails(data)
    return jsonify(result)


@Registration.route('/createRegProofs',methods = ['Post'])
def createRegProofs():
    data = request.json
    regbl = dbRegistration.RegProofsBL()
    result = regbl.dbcreateRegProofs(data)
    return jsonify(result)


@Registration.route('/updateRegProofs',methods = ['Post'])
def updateRegProofs():
    data = request.json
    regbl = dbRegistration.RegProofsBL()
    result = regbl.dbupdateRegProofs(data)
    return jsonify(result)

@Registration.route('/getRegProofs')
def getRegProofs():
    regid = request.args.get('regid')
    regbl = dbRegistration.RegProofsBL()
    result = regbl.dbgetRegProofs(regid)
    return jsonify(result)

