from DAL import query
from HelperClass import sqlhelper,commonutil,dataoutputmodel

cutil = commonutil.commonutil()


class SignBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"

    def dbportalLogin(self,data):
        try:
            sqlquery = query.Loginquarry.format(data['username'],data['password'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            resultmodel =  dataoutputmodel.DataOutputModel('portalLogin',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__