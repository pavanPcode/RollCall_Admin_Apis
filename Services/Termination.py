from flask import Blueprint,request,jsonify
from BL import dbTermination
from HelperClass.commonutil import commonutil

Termination = Blueprint('Termination',__name__)

@Termination.route('/resignEmp',methods = ['Post'])
def resignEmp():
    data = request.json
    terbl = dbTermination.TerminationBL()
    result = terbl.dbresignEmp(data)
    return jsonify(result)

@Termination.route('/rejoinEmp',methods = ['Post'])
def rejoinEmp():
    data = request.json
    terbl = dbTermination.TerminationBL()
    result = terbl.dbupdaterejoinEmp(data)
    return jsonify(result)

@Termination.route('/getTerminatedlist')
def getTerminatedlist():
    superid = request.args.get('superid')
    if superid == None:
        cut = commonutil()
        return jsonify(cut.InvalidResult('required superid parameter').__dict__)
    projectbl = dbTermination.TerminationBL()
    result = projectbl.dbgetTerminatedlist(superid)
    return jsonify(result)