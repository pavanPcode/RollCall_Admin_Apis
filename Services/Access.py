from flask import Blueprint,request,jsonify
from BL import dbAccess
from HelperClass.commonutil import commonutil

Access = Blueprint('Access',__name__)

@Access.route('/addmobileaccess',methods = ['Post'])
def addmobileaccess():
    data = request.json
    accbl = dbAccess.AccessBL()
    result = accbl.dbAddMobileAccess(data)
    return jsonify(result)

@Access.route('/addempportalaccess',methods = ['Post'])
def createbranch():
    data = request.json
    accbl = dbAccess.AccessBL()
    result = accbl.dbAddEmpPortalAccess(data)
    return jsonify(result)


@Access.route('/removeempportalaccess',methods = ['Post'])
def removeempportalaccess():
    data = request.json
    accbl = dbAccess.AccessBL()
    result = accbl.dbremoveempportalAccess(data)
    return jsonify(result)


@Access.route('/removemobileaccess',methods = ['Post'])
def removemobileaccess():
    data = request.json
    accbl = dbAccess.AccessBL()
    result = accbl.dbremovemobileAccess(data)
    return jsonify(result)

