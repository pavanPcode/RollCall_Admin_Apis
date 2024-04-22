from flask import Blueprint,request,jsonify
from BL import dbTeam
from HelperClass.commonutil import commonutil

Team = Blueprint('Team',__name__)


@Team.route('/getEmpTeam')
def getEmpTeam():
    regid = request.args.get('regid')
    teambl = dbTeam.TeamBL()
    result = teambl.dbgetTeam(regid)
    return jsonify(result)

@Team.route('/createTeam',methods = ['Post'])
def createTeam():
    data = request.json
    teambl = dbTeam.TeamBL()
    result = teambl.dbcreateTeam(data)
    return jsonify(result)

@Team.route('/updateTeam',methods = ['Post'])
def updateTeam():
    data = request.json
    teambl = dbTeam.TeamBL()
    result = teambl.dbupdateTeam(data)
    return jsonify(result)


@Team.route('/deleteTeam',methods = ['Post'])
def deleteTeam():
    data = request.json
    teambl = dbTeam.TeamBL()
    result = teambl.dbdeleteTeam(data)
    return jsonify(result)