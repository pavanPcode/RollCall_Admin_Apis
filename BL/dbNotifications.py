
from DAL import query
from HelperClass import sqlhelper,commonutil,dataoutputmodel

cutil = commonutil.commonutil()


class NotofiyBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"
    def dbcreateNotificationForAll(self,data):
        try:
            sqlquery = query.createNotificationForAll.format(data['superid'],data['title'],data['description'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('Notification created Successfully').__dict__
        except Exception as e:
            return cutil.InvalidResult(str(e)).__dict__

    def dbcreateNotificationForSingleUser(self,data):
        try:
            sqlquery = query.createNotificationForSingle.format(data['superid'],data['regid'],data['title'],data['description'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('Notification created Successfully').__dict__
        except Exception as e:
            return cutil.InvalidResult(str(e)).__dict__