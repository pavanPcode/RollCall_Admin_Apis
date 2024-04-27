
from DAL import query
from HelperClass import sqlhelper,commonutil,dataoutputmodel

cutil = commonutil.commonutil()


class ShiftsBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"
    def dbcreateShifts(self,data):
        try:
            for regid in data['regid']:
                sqlquery = query.assignshift.format(regid,data['shiftid'],data['startdate'],data['enddate'])
                sqlobj = sqlhelper.sqlhelper(self.dbname)
                rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('Shift assigned Successfully').__dict__
        except Exception as e:
            return cutil.InvalidResult(str(e)).__dict__

    def dbgetShiftsTypes(self,superid):
        try:
            sqlquery = query.getShiftsTypes.format(superid)
            print(sqlquery)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            resultmodel =  dataoutputmodel.DataOutputModel('getShiftsTypes',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.InvalidResult(str(e)).__dict__

    def dbgetAssignshiftByEmp(self,regid):
        try:
            sqlquery = query.getAssignshiftByEmp.format(regid)
            print(sqlquery)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            resultmodel =  dataoutputmodel.DataOutputModel('getAssignshiftByEmp',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.InvalidResult(str(e)).__dict__