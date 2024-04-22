
from DAL import query
from HelperClass import sqlhelper,commonutil,dataoutputmodel

cutil = commonutil.commonutil()


class TeamBL:
    cutil = commonutil.commonutil()

    def __init__(self):
        self.dbname = "premiumdb"

    def dbcreateTeam(self, data):
        try:
            checkTeamDup = query.checkTeammember.format(data['regid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(checkTeamDup)
            if rows[0]['type'] == 0:
                return cutil.InvalidResult('Emp already added in another Team').__dict__

            sqlquery = query.createEmpManager.format(data['superid'], data['regid'], data['managerid'])
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('Team addede Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbupdateTeam(self, data):
        try:
            sqlquery = query.updateEmpManager.format(data['superid'], data['regid'], data['managerid'])
            print(sqlquery)

            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('Team Updated Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbdeleteTeam(self, data):
        try:
            sqlquery = query.deleteEmpManager.format(data['regid'])
            print(sqlquery)

            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('Team deleted Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbgetTeam(self, regid):
        try:
            sqlquery = query.getempmanager.format(regid)
            print(sqlquery)

            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)

            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            resultmodel = dataoutputmodel.DataOutputModel('getTeam', rows, True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__
