from flask import Blueprint,request,jsonify
from BL import dbproject
from HelperClass.commonutil import commonutil

Projects = Blueprint('Projects',__name__)

@Projects.route('/createproject',methods = ['Post'])
def createproject():
    data = request.json
    projectbl = dbproject.ProjectsBL()
    result = projectbl.dbcreateproject(data)
    return jsonify(result)

@Projects.route('/updateproject',methods = ['Post'])
def updateproject():
    data = request.json
    projectbl = dbproject.ProjectsBL()
    result = projectbl.dbupdateproject(data)
    return jsonify(result)

@Projects.route('/deleteproject',methods = ['Post'])
def deleteproject():
    data = request.json
    projectbl = dbproject.ProjectsBL()
    result = projectbl.dbdeleteproject(data)
    return jsonify(result)

@Projects.route('/getproject')
def getproject():
    managerid = request.args.get('managerid')
    if managerid == None:
        cut = commonutil()
        return jsonify(cut.InvalidResult('required managerid parameter').__dict__)
    projectbl = dbproject.ProjectsBL()
    result = projectbl.dbgetproject(managerid)
    return jsonify(result)

###############ProjectTeam########

@Projects.route('/createprojectteam',methods = ['Post'])
def createprojectTeam():
    data = request.json
    Teambl = dbproject.ProjectsTeamBL()
    result = Teambl.dbcreateprojectteam(data)
    return jsonify(result)

@Projects.route('/getprojectteam')
def getprojectteam():
    projectid = request.args.get('projectid')
    if projectid == None:
        cut = commonutil()
        return jsonify(cut.InvalidResult('required projectid parameter').__dict__)
    teambl = dbproject.ProjectsTeamBL()
    result = teambl.dbgetprojectTeam(projectid)
    return jsonify(result)

@Projects.route('/deleteprojectteam',methods = ['Post'])
def deleteprojectteam():
    data = request.json
    teambl = dbproject.ProjectsTeamBL()
    result = teambl.dbdeleteprojectteam(data)
    return jsonify(result)

##############################Milestone
@Projects.route('/deletemilestone',methods = ['Post'])
def deletemilestone():
    data = request.json
    milestonebl = dbproject.MilestoneBL()
    result = milestonebl.dbdeleteMilestone(data)
    return jsonify(result)

@Projects.route('/createmilestone',methods = ['Post'])
def createmilestone():
    data = request.json
    milestonebl = dbproject.MilestoneBL()
    result = milestonebl.dbcreateMilestone(data)
    return jsonify(result)

@Projects.route('/updatemilestone',methods = ['Post'])
def updatemilestone():
    data = request.json
    milestonebl = dbproject.MilestoneBL()
    result = milestonebl.dbupdateMilestone(data)
    return jsonify(result)

@Projects.route('/getmilestone')
def getmilestone():
    projectid = request.args.get('projectid')
    if projectid == None:
        cut = commonutil()
        return jsonify(cut.InvalidResult('required projectid parameter').__dict__)
    milestonebl = dbproject.MilestoneBL()
    result = milestonebl.dbgetMilestone(projectid)
    return jsonify(result)


##################task
@Projects.route('/updatetask',methods = ['Post'])
def updatetask():
    data = request.json
    taskbl = dbproject.TaskBL()
    result = taskbl.dbupdatetask(data)
    return jsonify(result)

@Projects.route('/deletetask',methods = ['Post'])
def deletetask():
    data = request.json
    taskbl = dbproject.TaskBL()
    result = taskbl.dbdeletetask(data)
    return jsonify(result)

@Projects.route('/createtask',methods = ['Post'])
def createtask():
    data = request.json
    taskbl = dbproject.TaskBL()
    result = taskbl.dbcreatetask(data)
    return jsonify(result)

@Projects.route('/gettask')
def gettask():
    projectid = request.args.get('projectid')
    if projectid == None:
        cut = commonutil()
        return jsonify(cut.InvalidResult('required projectid parameter').__dict__)
    taskbl = dbproject.TaskBL()
    result = taskbl.dbgettask(projectid)
    return jsonify(result)


@Projects.route('/createtimesheet',methods = ['Post'])
def createtimesheet():
    data = request.json
    sheetbl = dbproject.TimesheetBL()
    result = sheetbl.dbcreatetimesheet(data)
    return jsonify(result)

@Projects.route('/updatetimesheet',methods = ['Post'])
def updatetimesheet():
    data = request.json
    sheetbl = dbproject.TimesheetBL()
    result = sheetbl.dbupdatetimesheet(data)
    return jsonify(result)

@Projects.route('/deletetimesheet',methods = ['Post'])
def deletetimesheet():
    data = request.json
    sheetbl = dbproject.TimesheetBL()
    result = sheetbl.dbdeletetimesheet(data)
    return jsonify(result)

@Projects.route('/gettimesheet')
def gettimesheet():
    TaskId = request.args.get('taskid')
    regid = request.args.get('regid')
    # if TaskId == None or :
    #     cut = commonutil()
    #     return jsonify(cut.InvalidResult('required projectid parameter').__dict__)
    sheetbl = dbproject.TimesheetBL()
    result = sheetbl.dbgettimesheet(TaskId,regid)
    print(result,type(result))
    return jsonify(result)


###############Announcemets
@Projects.route('/deleteannouncemets',methods = ['Post'])
def deleteannouncemets():
    data = request.json
    annoubl = dbproject.AnnouncemetsBL()
    result = annoubl.dbdeleteAnnouncemets(data)
    return jsonify(result)

@Projects.route('/createannouncemets',methods = ['Post'])
def createannouncemets():
    data = request.json
    annoubl = dbproject.AnnouncemetsBL()
    result = annoubl.dbcreateAnnouncemets(data)
    return jsonify(result)

@Projects.route('/updateannouncemets',methods = ['Post'])
def updateannouncemets():
    data = request.json
    annoubl = dbproject.AnnouncemetsBL()
    result = annoubl.dbupdateAnnouncemets(data)
    return jsonify(result)

@Projects.route('/updateannouncemetisread',methods = ['Post'])
def updateannouncemetisread():
    data = request.json
    annoubl = dbproject.AnnouncemetsBL()
    result = annoubl.dbupdateAnnouncemetIsRead(data)
    return jsonify(result)

@Projects.route('/getannouncemets')
def getannouncemets():
    superid = request.args.get('superid')
    if superid == None  :
        cut = commonutil()
        return jsonify(cut.InvalidResult('required superid parameter').__dict__)
    annoubl = dbproject.AnnouncemetsBL()
    result = annoubl.dbgetAnnouncemets(superid)
    return jsonify(result)