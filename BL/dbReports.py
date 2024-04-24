from DAL import query
from HelperClass import sqlhelper,commonutil,dataoutputmodel

cutil = commonutil.commonutil()
from datetime import datetime, time,date

class ReportsBL:
    cutil = commonutil.commonutil()
    def __init__(self):
        self.dbname = "premiumdb"

    def dbgetReports(self,superid,reportiid,StartDate,EndDate,RegId,DeptId,AttendanceStatus,ShiftId,BranchId):
        try:
            sqlquery = query.getReports.format(superid,reportiid,StartDate,EndDate,RegId,DeptId,AttendanceStatus,ShiftId,BranchId)
            sqlobj = sqlhelper.sqlhelper(self.dbname)
            rows = sqlobj.execstoredproc(sqlquery)
            if rows == None or len(rows) == 0:
                return cutil.InvalidResult('No data available').__dict__
            # Convert datetime objects to strings only if not None
            # for item in rows:
            #     if 'Date' in item and item['Date'] is not None and not isinstance(item['Date'], str):
            #         item['Date'] = item['Date'].strftime('%Y-%m-%d')
            #     if 'In Time' in item and item['In Time'] is not None and not isinstance(item['In Time'], str):
            #         item['In Time'] = item['In Time'].strftime('%H:%M:%S')
            #     if 'Out Time' in item and item['Out Time'] is not None and not isinstance(item['Out Time'], str):
            #         item['Out Time'] = item['Out Time'].strftime('%H:%M:%S')
            #
            #     if 'Transaction Date' in item and item['Transaction Date'] is not None and not isinstance(item['Transaction Date'], str):
            #         item['Transaction Date'] = item['Transaction Date'].strftime('%Y-%m-%d %H:%M:%S')
            #
            #
            #
            #     if 'Duration' in item and item['Duration'] is not None:
            #         item['Duration'] = str(item['Duration'])

            # Function to convert datetime objects to strings
            def convert_to_str(item):
                for key, value in item.items():
                    if isinstance(value, datetime):
                        item[key] = value.strftime('%Y-%m-%d %H:%M:%S')  # Change the format as needed
                    elif isinstance(value, time):
                        item[key] = value.strftime('%H:%M:%S')  # Change the format as needed
                    elif isinstance(value, date):
                        item[key] = value.strftime('%Y-%m-%d')  # Change the format as needed

                return item

            # Convert datetime objects to strings
            modified_data = [convert_to_str(item) for item in rows]

            resultmodel =  dataoutputmodel.DataOutputModel('getReports',modified_data,True)
            return resultmodel.__dict__
        except Exception as e:
            return cutil.InvalidResult(str(e)).__dict__