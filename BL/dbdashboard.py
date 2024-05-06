
from DAL import query
from HelperClass import sqlhelper,commonutil,dataoutputmodel
import datetime as DT
import json

cutil = commonutil.commonutil()


class dashboardBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"

    def dbgetDashboardAttendance(self,superid,InStatus):
        try:
            todaydate =  DT.date.today()
            stardate = f'{todaydate} 00:00:01'
            enddate = f'{todaydate} 23:59:59'

            sqlquery = query.getDashboardAttendance.format(superid,stardate,enddate,InStatus)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            # rows = json.dumps(rows)
            resultmodel =  dataoutputmodel.DataOutputModel('getDashboardAttendance',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.InvalidResult(str(e)).__dict__

    def dbgetdashboardcount(self,superid):
        try:
            todaydate =  DT.date.today()
            stardate = f'{todaydate} 00:00:01'
            enddate = f'{todaydate} 23:59:59'

            sqlquery = query.getdashboardcount.format(superid)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            resultmodel =  dataoutputmodel.DataOutputModel('getdashboardcount',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.InvalidResult(str(e)).__dict__