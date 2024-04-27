from DAL import query
from HelperClass import sqlhelper,commonutil,dataoutputmodel

cutil = commonutil.commonutil()


class AccessBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"
    def dbAddMobileAccess(self,data):
        try:
            sqlquery = query.addmobileAccess.format(data['regid'],1,1234)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('MobileAccess added Successfully').__dict__
        except Exception as e:
            return cutil.InvalidResult(str(e)).__dict__

    def dbAddEmpPortalAccess(self,data):
        try:
            sqlquery = query.addempportalAccess.format(data['regid'],2,1234)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('EmpPortalAccess added Successfully').__dict__
        except Exception as e:
            return cutil.InvalidResult(str(e)).__dict__

    def dbremovemobileAccess(self,data):
        try:
            sqlquery = query.removemobileAccess.format(data['regid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('removed mobileAccess  Successfully').__dict__
        except Exception as e:
            return cutil.InvalidResult(str(e)).__dict__

    def dbremoveempportalAccess(self,data):
        try:
            sqlquery = query.removeempportalAccess.format(data['regid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('removed empportalAccess  Successfully').__dict__
        except Exception as e:
            return cutil.InvalidResult(str(e)).__dict__