from DAL import query
from .typedefinition import PROJECTS
from HelperClass import sqlhelper,commonutil,dataoutputmodel

cutil = commonutil.commonutil()


class ProjectsBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"
    def dbcreateproject(self,data):
        try:
            sqlquery = query.CreateProject.format(data['title'],data['customerid'],data['startdate'],data['enddate'],data['status']
                                                  ,data['managerid'],data['superid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('project Invalid').__dict__
            else:
                return cutil.SuccessResult('project created Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbupdateproject(self,data):
        try:
            sqlquery = query.updateProject.format(data['title'], data['customerid'], data['startdate'], data['enddate'],
                                                  data['status']
                                                  , data['managerid'], data['superid'],data['projectid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('project Invalid').__dict__
            else:
                return cutil.SuccessResult('project Updated Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbdeleteproject(self,data):
        try:
            sqlquery = query.deleteProject.format(data['projectid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('project Invalid').__dict__
            else:
                return cutil.SuccessResult('project deleted Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbgetproject(self,managerid):
        try:
            sqlquery = query.GetProjects.format(managerid)
            print(sqlquery)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            resultmodel =  dataoutputmodel.DataOutputModel('getproject',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__


class ProjectsTeamBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"
    def dbcreateprojectteam(self,data):
        try:
            sqlquery = query.createprojectteam.format(data['regid'],data['superid'],data['projectid'],data['createdby'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('projectTeam Invalid').__dict__
            else:
                return cutil.SuccessResult('projectteam created Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__



    def dbdeleteprojectteam(self,data):
        try:
            sqlquery = query.deleteprojectteam.format(data['projectteamid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('projectTeam Invalid').__dict__
            else:
                return cutil.SuccessResult('projectTeam deleted Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbgetprojectTeam(self,projectid):
        try:
            sqlquery = query.getprojectteam.format(projectid)
            print(sqlquery)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            resultmodel =  dataoutputmodel.DataOutputModel('dbgetprojectTeam',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__


class MilestoneBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"
    def dbcreateMilestone(self,data):
        try:
            sqlquery = query.createMilestone.format(data['projectid'],data['startdate'],data['enddate'],data['description'],
                                                    data['superIid'],data['createdby'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('Milestone Invalid').__dict__
            else:
                return cutil.SuccessResult('Milestone created Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbupdateMilestone(self,data):
        try:
            sqlquery = query.updateMilestone.format(data['projectid'],data['startdate'],data['enddate'],data['description'],
                                                    data['superIid'],data['milestoneid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('Milestone Invalid').__dict__
            else:
                return cutil.SuccessResult('Milestone Updated Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbdeleteMilestone(self,data):
        try:
            sqlquery = query.deleteMilestone.format(data['milestoneid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('Milestone Invalid').__dict__
            else:
                return cutil.SuccessResult('Milestone deleted Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbgetMilestone(self,projectid):
        try:
            sqlquery = query.getMilestone.format(projectid)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            resultmodel =  dataoutputmodel.DataOutputModel('getMilestone',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

class TaskBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"
    def dbcreatetask(self,data):
        try:
            sqlquery = query.createtask.format(data['title'],data['description'],data['projectid'],data['milestoneid'],
                                                    data['startdate'],data['enddate'],data['priority'],
                                               data['superid'],data['createdby'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('Task Invalid').__dict__
            else:
                return cutil.SuccessResult('Task created Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbupdatetask(self,data):
        try:
            sqlquery = query.updatetask.format(data['title'],data['description'],data['projectid'],data['milestoneid'],
                                                    data['startdate'],data['enddate'],data['priority'],
                                               data['superid'],data['taskid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('Task Invalid').__dict__
            else:
                return cutil.SuccessResult('Task Updated Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbdeletetask(self,data):
        try:
            sqlquery = query.deletetask.format(data['taskid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('Task Invalid').__dict__
            else:
                return cutil.SuccessResult('Task deleted Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbgettask(self,projectid):
        try:
            sqlquery = query.gettask.format(projectid)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            resultmodel =  dataoutputmodel.DataOutputModel('getTask',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

class TimesheetBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"
    def dbcreatetimesheet(self,data):
        try:
            sqlquery = query.createtimesheet.format(data['taskid'],data['date'],data['description'],data['starttime'],
                                                    data['endtime'],data['regid'],data['superid'],
                                               data['createdby'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('Timesheet Invalid').__dict__
            else:
                return cutil.SuccessResult('Timesheet created Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbupdatetimesheet(self,data):
        try:
            sqlquery = query.updateTimesheet.format(data['taskid'],data['date'],data['description'],data['starttime'],
                                                    data['endtime'],data['regid'],data['superid'],
                                               data['timesheetid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('Timesheet Invalid').__dict__
            else:
                return cutil.SuccessResult('Timesheet Updated Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbdeletetimesheet(self,data):
        try:
            sqlquery = query.deletetimesheet.format(data['timesheetid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('Timesheet Invalid').__dict__
            else:
                return cutil.SuccessResult('Timesheet deleted Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbgettimesheet(self,TaskId,regid):
        try:
            if TaskId == None or TaskId == '':
                TaskId = 'TaskId'
            if regid == None or regid == '':
                regid = 'regid'

            sqlquery = query.Gettimesheet.format(TaskId,regid)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            resultmodel =  dataoutputmodel.DataOutputModel('getTimesheet',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

class AnnouncemetsBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"
    def dbcreateAnnouncemets(self,data):
        try:
            sqlquery = query.createAnnouncemets.format(data['superid'],data['name'],data['description'],data['startdatetime'],
                                                    data['enddatetime'],data['createdby'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('Announcemets Invalid').__dict__
            else:
                return cutil.SuccessResult('Announcemets created Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbupdateAnnouncemets(self,data):
        try:
            sqlquery = query.updateAnnouncemets.format(data['superid'],data['name'],data['description'],data['startdatetime'],
                                                    data['enddatetime'],data['notificationid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('Announcemets Invalid').__dict__
            else:
                return cutil.SuccessResult('Announcemets Updated Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbupdateAnnouncemetIsRead(self,data):
        try:
            sqlquery = query.updateIsread.format(data['notificationid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('Announcemets Invalid').__dict__
            else:
                return cutil.SuccessResult('Announcemets isread Updated Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbdeleteAnnouncemets(self,data):
        try:
            sqlquery = query.deleteAnnouncemets.format(data['notificationid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult('Announcemets Invalid').__dict__
            else:
                return cutil.SuccessResult('Announcemets deleted Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbgetAnnouncemets(self,superid):
        try:

            sqlquery = query.GetAnnouncemets.format(superid)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            resultmodel =  dataoutputmodel.DataOutputModel('getAnnouncemets',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__
