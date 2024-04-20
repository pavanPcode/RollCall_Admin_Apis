from DAL import query
from HelperClass import sqlhelper,commonutil,dataoutputmodel

cutil = commonutil.commonutil()


class EmployeeBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"
    def dbcreateEmployee(self,data):
        try:
            sqlquery = query.createEmployee.format(data['superid'],data['badge'],data['username'],data['dateofbirth']
                                                  ,data['designation'],data['cardid'],data['mobile'],data['rfid']
                                                   ,data['dateofbirth'],data['gender'],data['branchid'],data['departmentid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('Employee created Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbupdateEmployee(self,data):
        try:
            sqlquery = query.updateEmployee.format(data['superid'],data['badge'],data['username'],data['dateofbirth']
                                                  ,data['designation'],data['cardid'],data['mobile'],data['rfid']
                                                   ,data['dateofbirth'],data['gender'],data['branchid'],data['departmentid'],data['regid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('Employee Updated Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbdeleteEmployee(self,data):
        try:
            sqlquery = query.deleteEmployee.format(data['regid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('Employee deleted Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbgetEmployee(self,regid):
        try:
            sqlquery = query.getEmployee.format(regid)
            print(sqlquery)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            resultmodel =  dataoutputmodel.DataOutputModel('getEmployee',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

class RegBankDetailsBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"
    def dbcreateRegBankDetails(self,data):
        try:
            sqlquery = query.createRegBankDetails.format(data['superid'],data['regid'],data['accountNo'],data['accountholdersname']
                                                  ,data['bankName'],data['bankbranch'],data['ifsccode'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('RegBankDetails created Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbupdateRegBankDetails(self,data):
        try:
            sqlquery = query.updateRegBankDetails.format(data['accountNo'],data['accountholdersname']
                                                  ,data['bankName'],data['bankbranch'],data['ifsccode'],data['regid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('RegBankDetails Updated Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbdeleteRegBankDetails(self,data):
        try:
            sqlquery = query.deleteRegBankDetails.format(data['regid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('RegBankDetails deleted Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbgetRegBankDetails(self,regid):
        try:
            sqlquery = query.getRegBankDetails.format(regid)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            resultmodel =  dataoutputmodel.DataOutputModel('getRegBankDetails',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__