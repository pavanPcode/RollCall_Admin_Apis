from flask import Blueprint,request,jsonify
from BL import dbHolidays
from HelperClass.commonutil import commonutil

Holidays = Blueprint('Holidays',__name__)

@Holidays.route('/createproject',methods = ['Post'])
def createproject():
    data = request.json
    holbl = dbHolidays.HolidaysBL()
    result = holbl.dbcreateproject(data)
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
    if superid == None:
        cut = commonutil()
        return jsonify(cut.InvalidResult('required superid parameter').__dict__)
    holbl = dbHolidays.HolidaysBL()
    result = holbl.dbgetHolidays(superid)
    return jsonify(result)
