from DAL import query
from HelperClass import sqlhelper,commonutil,dataoutputmodel

cutil = commonutil.commonutil()

class ReportsBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"

    def dbgetReports(self,superid,reportiid,StartDate,EndDate,RegId,DeptId,AttendanceStatus,ShiftId,BranchId):
        try:
            sqlquery = query.getReports.format(superid,reportiid,StartDate,EndDate,RegId,DeptId,AttendanceStatus,ShiftId,BranchId)
            print(sqlquery)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.execstoredproc(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            # Convert datetime objects to strings only if not None
            for item in rows:
                # if 'Date' in item and item['Date'] is not None and not isinstance(item['Date'], str):
                #     item['Date'] = item['Date'].strftime('%Y-%m-%d')
                # if 'In Time' in item and item['In Time'] is not None and not isinstance(item['In Time'], str):
                #     item['In Time'] = item['In Time'].strftime('%H:%M:%S')
                # if 'Out Time' in item and item['Out Time'] is not None and not isinstance(item['Out Time'], str):
                #     item['Out Time'] = item['Out Time'].strftime('%H:%M:%S')
                #
                # if 'Transaction Date' in item and item['Transaction Date'] is not None and not isinstance(item['Transaction Date'], str):
                #     item['Transaction Date'] = item['Transaction Date'].strftime('%Y-%m-%d %H:%M:%S')

                if 'Date' in item and item['Date'] is not None :
                    item['Date'] = str(item['Date'])
                if 'In Time' in item and item['In Time'] is not None :
                    item['In Time'] = str(item['In Time'])
                if 'Out Time' in item and item['Out Time'] is not None :
                    item['Out Time'] = str(item['Out Time'])

                if 'Transaction Date' in item and item['Transaction Date'] is not None :
                    item['Transaction Date'] = str(item['Transaction Date'])

                if 'Duration' in item and item['Duration'] is not None:
                    item['Duration'] = str(item['Duration'])

            resultmodel =  dataoutputmodel.DataOutputModel('getReports',rows,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.SuccessResult(str(e)).__dict__