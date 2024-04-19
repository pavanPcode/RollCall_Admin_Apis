from flask import Blueprint,request,jsonify
from BL import dbBranches
from HelperClass.commonutil import commonutil

Holidays = Blueprint('Holidays',__name__)

@Holidays.route('/createbranch',methods = ['Post'])
def createbranch():
    data = request.json
    branchbl = dbBranches.BranchesBL()
    result = branchbl.dbcreateBranch(data)
    return jsonify(result)

@Holidays.route('/updatebranch',methods = ['Post'])
def updatebranch():
    data = request.json
    branchbl = dbBranches.BranchesBL()
    result = branchbl.dbupdateBranch(data)
    return jsonify(result)

@Holidays.route('/deletebranch',methods = ['Post'])
def deletebranch():
    data = request.json
    branchbl = dbBranches.BranchesBL()
    result = branchbl.dbdeleteBranch(data)
    return jsonify(result)

@Holidays.route('/getbranch')
def getbranch():
    superid = request.args.get('superid')
    if superid == None:
        cut = commonutil()
        return jsonify(cut.InvalidResult('required superid parameter').__dict__)
    branchbl = dbBranches.BranchesBL()
    result = branchbl.dbgetBranch(superid)
    return jsonify(result)
