from flask import Blueprint,request,jsonify
from BL import dbsignin
from HelperClass.commonutil import commonutil

Signin = Blueprint('Signin',__name__)

@Signin.route('/portallogin',methods = ['Post'])
def createHolidays():
    data = request.json
    dignbl = dbsignin.SignBL()
    result = dignbl.dbportalLogin(data)
    return jsonify(result)