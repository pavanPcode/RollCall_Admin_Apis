from flask import Blueprint,request,jsonify
from BL import dbHolidays
from HelperClass.commonutil import commonutil
from datetime import datetime

Holidays = Blueprint('Holidays',__name__)

@Holidays.route('/createHolidays',methods = ['Post'])
def createHolidays():
    data = request.json
    holbl = dbHolidays.HolidaysBL()
    result = holbl.dbcreateHolidays(data)
    return jsonify(result)

@Holidays.route('/updateholiday',methods = ['Post'])
def updateholiday():
    data = request.json
    holbl = dbHolidays.HolidaysBL()
    result = holbl.dbupdateHolidays(data)
    return jsonify(result)

@Holidays.route('/deleteholiday',methods = ['Post'])
def deleteholiday():
    data = request.json
    holbl = dbHolidays.HolidaysBL()
    result = holbl.dbdeleteHolidays(data)
    return jsonify(result)

@Holidays.route('/getholidays')
def getholidays():
    superid = request.args.get('superid')
    year = request.args.get("year", default=datetime.now().year, type=int)

    # Start of the year
    start_date = datetime(year, 1, 1)
    # End of the year
    end_date = datetime(year, 12, 31)

    if superid == None:
        cut = commonutil()
        return jsonify(cut.InvalidResult('required superid parameter').__dict__)
    holbl = dbHolidays.HolidaysBL()
    result = holbl.dbgetHolidays(superid,start_date,end_date)
    return jsonify(result)
