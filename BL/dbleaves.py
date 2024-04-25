from HelperClass.commonutil import commonutil
from HelperClass.dataoutputmodel import DataOutputModel
#from BL.typedefinition import Punch
from datetime import date, datetime
import calendar
from HelperClass.sqlhelper import sqlhelper
from DAL import query


class LeaveBL:
    global cutil
    cutil = commonutil()

    def __init__(self):
        self.dbname = "premiumdb"

    def leaveaccruals(self, regid):
        exequery = query.leaveaccruals.format(regid, 2020)  # datetime.now().year)
        runqry = sqlhelper(self.dbname)
        rows = runqry.queryall(exequery)
        if rows == None:
            return cutil.InvalidResult('No LeaveAccruals')
        elif len(rows) == 0:
            return cutil.InvalidResult('No LeaveAccruals Available')

        return DataOutputModel('Leave Accruals', rows, True)

    def leavetypes(self, superid):
        exequery = query.leavetypes.format(superid)
        runqry = sqlhelper(self.dbname)
        rows = runqry.queryall(exequery)
        if rows == None:
            return cutil.InvalidResult('No Leaves Available')
        elif len(rows) == 0:
            return cutil.InvalidResult('No Leaves Available')

        return DataOutputModel('Leave Types', rows, True)

    def empleaves(self, regid, status, year):
        if status == 1:
            exequery = query.emppendingleaves.format(regid, year, status)
        elif status == 2:
            exequery = query.empapprovedleaves.format(regid, year, status)
        elif status == 3:
            exequery = query.empapprovedleaves.format(regid, year, status)
        else:
            exequery = query.empleaves.format(regid, year)
        runqry = sqlhelper(self.dbname)
        rows = runqry.queryall(exequery)
        if rows == None:
            return cutil.InvalidResult('No Leaves Available')
        elif len(rows) == 0:
            return cutil.InvalidResult('No Leaves Available')

        return DataOutputModel('Leaves Taken', rows, True)



    def saveleave(self, requestdata):
        superid = requestdata['superid']
        regid = requestdata['regid']
        lvtype = requestdata['lvtypeid']
        halfday = requestdata['halfday']
        startdate = requestdata['startdate']
        enddate = requestdata['enddate']
        leavecount = requestdata['leavecount']
        comments = requestdata['comments']

        exequery = query.leaverec.format(superid, regid, lvtype, halfday, startdate, enddate, leavecount, comments)
        runqry = sqlhelper(self.dbname)
        rows = runqry.execstoredproc(exequery)
        if rows == None:
            return cutil.InvalidResult('Error Occured While Updating Leave')
        elif len(rows) == 0:
            return cutil.InvalidResult('Error Occured While Updating Leave')

        # if succesful send alert to Employee and Manager regarding the Leave to approve
        return DataOutputModel('Leave Updated Successfully', rows, True)

    def approveleave(self, data):
        exequery = query.approveleave.format(data['status'], data['leaveid'], data['regid'], data['comments'])
        runqry = sqlhelper(self.dbname)
        rows = runqry.update(exequery)
        if rows < 1:
            return cutil.InvalidResult('Leave Invalid')
        else:
            return cutil.SuccessResult('Leave Updated Successfully')



