
from DAL import query
from HelperClass import sqlhelper,commonutil,dataoutputmodel

cutil = commonutil.commonutil()


class BranchesBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"
    def dbcreateBranch(self,data):
        try:
            sqlquery = query.createbranch.format(data['superid'],data['name'],data['code'],data['createdby'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('Branch created Successfully').__dict__
        except Exception as e:
            return cutil.InvalidResult(str(e)).__dict__

    def dbupdateBranch(self,data):
        try:
            sqlquery = query.updatebranch.format(data['superid'],data['name'],data['code'],data['createdby'],data['branchid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('Branch Updated Successfully').__dict__
        except Exception as e:
            return cutil.InvalidResult(str(e)).__dict__

    def dbdeleteBranch(self,data):
        try:
            sqlquery = query.deletebranch.format(data['branchid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('Branch deleted Successfully').__dict__
        except Exception as e:
            return cutil.InvalidResult(str(e)).__dict__

    def dbgetBranch(self,superid):
        try:
            sqlquery = query.getbranches.format(superid)
            print(sqlquery)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            resultmodel =  dataoutputmodel.DataOutputModel('getBranch',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.InvalidResult(str(e)).__dict__