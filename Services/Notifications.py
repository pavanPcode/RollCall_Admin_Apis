from flask import Blueprint,request,jsonify
from BL import dbNotifications
from HelperClass.commonutil import commonutil
from datetime import datetime
import json
from HelperClass.commonutil import commonutil
import datetime as DT

cutil = commonutil()

Notification = Blueprint('Notification',__name__)

@Notification.route("/NotificationForAll", methods=['POST'])
def NotificationForAll():
    try:
        if request.method == 'POST':
            reqdata = request.json
            notifybl = dbNotifications.NotofiyBL()
            retrows = notifybl.dbcreateNotificationForAll(reqdata)
            return jsonify(retrows)
    except Exception as e:
        retmdl = cutil.InvalidResult(f"Error occured : {str(e)}")
        return jsonify(retmdl)

@Notification.route("/NotificationForEmp", methods=['POST'])
def NotificationForEmp():
    try:
        if request.method == 'POST':
            reqdata = request.json
            notifybl = dbNotifications.NotofiyBL()
            retrows = notifybl.dbcreateNotificationForSingleUser(reqdata)
            return jsonify(retrows)
    except Exception as e:
        retmdl = cutil.InvalidResult(f"Error occured : {str(e)}")
        return jsonify(retmdl)