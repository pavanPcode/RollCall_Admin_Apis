from flask import Blueprint,request,jsonify
from BL import dbBranches
from HelperClass.commonutil import commonutil

branch = Blueprint('branch',__name__)

@branch.route('/createbranch',methods = ['Post'])
def createbranch():
    data = request.json
    branchbl = dbBranches.BranchesBL()
    result = branchbl.dbcreateBranch(data)
    return jsonify(result)

@branch.route('/updatebranch',methods = ['Post'])
def updatebranch():
    data = request.json
    branchbl = dbBranches.BranchesBL()
    result = branchbl.dbupdateBranch(data)
    return jsonify(result)

@branch.route('/deletebranch',methods = ['Post'])
def deletebranch():
    data = request.json
    branchbl = dbBranches.BranchesBL()
    result = branchbl.dbdeleteBranch(data)
    return jsonify(result)

@branch.route('/getbranch')
def getbranch():
    superid = request.args.get('superid')
    if superid == None:
        cut = commonutil()
        return jsonify(cut.InvalidResult('required superid parameter').__dict__)
    branchbl = dbBranches.BranchesBL()
    result = branchbl.dbgetBranch(superid)
    return jsonify(result)
