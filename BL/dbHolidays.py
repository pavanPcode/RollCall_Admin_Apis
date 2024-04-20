
from DAL import query
from HelperClass import sqlhelper,commonutil,dataoutputmodel

cutil = commonutil.commonutil()


class HolidaysBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"
    def dbcreateHolidays(self,data):
        try:
            sqlquery = query.createHoliday.format(data['superid'],data['holidaydt'],data['reason'],data['optional']
                                                  ,data['createdby'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('Holiday created Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbupdateHolidays(self,data):
        try:
            sqlquery = query.updateHoliday.format(data['superid'],data['holidaydt'],data['reason'],data['optional']
                                                  ,data['createdby'],data['holidayid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('Holiday Updated Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbdeleteHolidays(self,data):
        try:
            sqlquery = query.deleteHoliday.format(data['holidayid'])
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.update(sqlquery)
            if rows < 1:
                return cutil.InvalidResult(' Invalid').__dict__
            else:
                return cutil.SuccessResult('Holiday deleted Successfully').__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__

    def dbgetHolidays(self,superid):
        try:
            sqlquery = query.getHolidays.format(superid)
            print(sqlquery)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.queryall(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            resultmodel =  dataoutputmodel.DataOutputModel('getholiday',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__