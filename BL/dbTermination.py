from DAL import query
from HelperClass import sqlhelper,commonutil,dataoutputmodel

cutil = commonutil.commonutil()


class TerminationBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"
    def dbresignEmp(self,data):
        try:
            sqlquery = query.resignEmp.format(data['regid'],data['terminationdt'],data['reason'],data['createdby'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('resignEmp Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbupdaterejoinEmp(self,data):
        try:
            sqlquery = query.rejoinEmp.format(data['regid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('rejoinEmp Updated Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbgetTerminatedlist(self,superid):
        try:
            sqlquery = query.Terminatedlist.format(superid)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            resultmodel =  dataoutputmodel.DataOutputModel('getTerminatedlist',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__