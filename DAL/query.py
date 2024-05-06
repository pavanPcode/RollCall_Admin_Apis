
#holidays##########################
createHoliday = """INSERT INTO [PROD].[Holidays] (SuperId, HolidayDt, UpdatedBy, UpdatedOn, Reason, Optional)
VALUES ({0}, '{1}', {4}, DATEADD(MINUTE, 330, GETUTCDATE()), '{2}', {3} );"""

updateHoliday = """UPDATE [PROD].[Holidays]
SET superid = {0},HolidayDt = '{1}',
    UpdatedBy = {4},
    UpdatedOn =  DATEADD(MINUTE, 330, GETUTCDATE()),
    Reason = '{2}',
    Optional = {3}
WHERE Id = {5};"""

deleteHoliday = """update [PROD].[Holidays] set isactive  = 0 where id = {0}"""

getHolidays = """select id holidayid,SuperId, HolidayDt, UpdatedBy, UpdatedOn, Reason, Optional from [PROD].[Holidays]
 where superid = {0} and isactive = 1 and HolidayDt between '{1}' and '{2}'
 order by HolidayDt"""



#branche###########################
createbranch = """insert into [PROD].[Branches] (superid,name,code,CreatedBy,CreatedOn,IsActive)
values({0},'{1}','{2}',{3},DATEADD(MINUTE, 330, GETUTCDATE()),1) """

updatebranch = """update [PROD].[Branches] set superid = {0},name = '{1}',code = '{2}' ,UpdatedBy ={3} ,
UpdatedOn = DATEADD(MINUTE, 330, GETUTCDATE()) where id = {4} """

deletebranch = """update [PROD].[Branches] set isactive = 0,UpdatedOn = DATEADD(MINUTE, 330, GETUTCDATE()) where id = {0}"""

getbranches = """select id branchid,SuperId,Name,code from [PROD].[Branches] where SuperId = {0} and IsActive = 1 """

########################department
getdepartment = """select id departmentid,SuperId,Name,code from [PROD].[Department] where isactive = 1 and SuperId = {0}"""

getEmpByDept = """

SELECT Id regid, UserName + '-' + Badge AS UserName
FROM prod.V_AllRegDetails
WHERE SuperId = {1} AND DeptId = {0}
ORDER BY Badge;"""

createdepartment = """insert into [PROD].[Department] (SuperId,name,code,IsActive)
values({0},'{1}','{2}',1) """

updatedepartment = """update [PROD].[Department] set SuperId = {0},Name = '{1}' ,Code = '{2}' where id =  {3}"""

deletedepartment = """update [PROD].[Department] set isactive = 0  where id = {0}"""

###############Employee
createEmployee = """DECLARE @RegId INT;
insert into [PROD].[Registration](superid,Badge,UserName,DateOfBirth,Designation,CardId,Mobile,RFID,Gender)
values({0},{1},'{2}','{3}','{4}',{5},'{6}','{7}',{9})

SET @RegId = SCOPE_IDENTITY()

insert into [PROD].[EmpBranch](SuperId,RegId,BranchId,CreatedBy)
values({0},@RegId ,{10},{12})

insert into [PROD].[EmpDept] (regid,deptid)
values(@RegId ,{11})"""

updateEmployee = """update [PROD].[Registration] set superid = {0},Badge = {1},UserName = '{2}',DateOfBirth = '{3}',Designation = '{4}'
,CardId = {5},Mobile = '{6}',RFID = '{7}',Gender = {9} where id = {12};

update  [PROD].[EmpBranch]set BranchId = {10} where RegId ={12};
update [PROD].[EmpDept] set deptid = {11} where regid = {12};"""

deleteEmployee = """update [PROD].[Registration] set IsActive = 0 where id = {0}"""

getEmployee = """
select r.id regid,r.superid,r.Badge,r.UserName,r.DateOfBirth,r.Designation,r.CardId,r.Mobile,r.RFID,r.DateOfBirth,r.Gender,emp.branchid,
b.Name branchname ,b.Code branchcode,ed.DeptId Departmentid ,d.Name Departmentname ,d.Code Departmentcode,r.isactive,r.dateofjoining,
r.MobileAccess,r.EmpPortalAccess
from [PROD].[Registration] r
left join [PROD].[EmpBranch] emp on emp.RegId = r.id
left join [PROD].[Branches] b on b.id = emp.BranchId
left join [PROD].[EmpDept] ed on ed.RegId = r.id
left join [PROD].[Department] d on d.id = ed.deptid
where r.superid = {0} and r.isactive = 1 
and ed.DeptId = {1} and r.id = {2}
order by r.id desc"""

###########################RegBankDetails
createRegBankDetails = """insert into [PROD].[RegBankDetails](SuperId,RegId,AccountNo,AccountHoldersName,BankName,BankBranch,IfscCode,createdby)
values({0},{1},'{2}','{3}','{4}','{5}','{6}',{7})"""

updateRegBankDetails = """update [PROD].[RegBankDetails] set AccountNo = '{0}' ,AccountHoldersName ='{1}' ,BankName = '{2}',
BankBranch = '{3}',IfscCode = '{4}' where RegId = {5}"""

deleteRegBankDetails =  """update [PROD].[RegBankDetails] set IsActive = 0 where RegId = {0}"""

getRegBankDetails = """select SuperId,RegId,AccountNo,AccountHoldersName,BankName,BankBranch,IfscCode from [PROD].[RegBankDetails] 
where regid = {0} and isactive = 1"""

###################RegProofs
createRegProofs = """insert into  [PROD].[RegProofs](SuperId,regid,pan,uan,adhaar,esi,pf,EPFStart,VoterId,CreatedBy)
values({0},{1},'{2}','{3}','{4}','{5}','{6}','{7}','{8}',{9}) """

updateRegProofs = """update [PROD].[RegProofs] set pan = '{0}',uan = '{1}',adhaar = '{2}',esi = '{3}',pf = '{4}',EPFStart = '{5}',
VoterId = '{6}' where RegId = {7}"""

deleteRegProofs = """update [PROD].[RegProofs] set isactive = 0 where RegId = {0}"""

getRegProofs = """select SuperId,regid,pan,uan,adhaar,esi,pf,EPFStart,VoterId from [PROD].[RegProofs] 
where regid = {0} and isactive = 1 """

##########

checkTeammember = """IF NOT EXISTS (SELECT 1 FROM [PROD].[EmpManager] WHERE regid = {0} and isactive = 1)
BEGIN
    select 1 type
END
ELSE
BEGIN
    select 0 type
END"""


createEmpManager = """insert into [PROD].[EmpManager] (superid,regid,ManagerId)
values({0},{1},{2})"""

updateEmpManager = """update [PROD].[EmpManager] set superid = {0} ,ManagerId = {2} where RegId = {1}"""

deleteEmpManager = """update [PROD].[EmpManager] set isactive  = 0 where RegId = {0}"""

getempmanager = """select m.regid,m.cardid,m.badge,m.username,m.designation,m.dateofjoining,m.empportalaccess,m.managerid,m.emailId
from [PROD].[EmpManager] em
inner join  [PROD].[Registration]  e on e.id = em.RegId
inner join  Prod.V_ManagerEmployes m on m.managerid = em.ManagerId
where em.isactive = 1 and em.regid = {0}"""

##################
createRegDetails = """insert into [PROD].[RegDetails](superid,regid,emailid,EmergencyContactNo1,EmergencyContactNo2,CurrentAddress,PermanentAddress,isactive)
values({0},{1},'{2}','{3}','{4}','{5}','{6}',1) """

updateRegDetails = """update [PROD].[RegDetails] set emailid = '{0}',EmergencyContactNo1 = '{1}',EmergencyContactNo2 = '{2}',
CurrentAddress = '{3}',PermanentAddress = '{4}' where RegId =  {5}"""

deleteRegDetails = """update [PROD].[RegDetails] set IsActive = 0 where RegId = {0}"""

getRegDetails = """select superid,regid,emailid,EmergencyContactNo1,EmergencyContactNo2,CurrentAddress,PermanentAddress from [PROD].[RegDetails] 
where IsActive = 1 and RegId = {0} """

################
resignEmp = """insert into [PROD].[RegTermination](regid,TerminationDt,Reason,IsActive,UpdatedOn,UpdatedBy)
values({0},'{1}','{2}',1,DATEADD(MINUTE, 330, GETUTCDATE()),{3});
update [PROD].[Registration] set IsActive = 0 where id = {0}"""

rejoinEmp = """update [PROD].[Registration] set IsActive = 1 where id = {0}
update [PROD].[RegTermination] set IsActive = 0 where regid = {0}"""

Terminatedlist = """select rt.regid,rt.TerminationDt,rt.Reason,rt.IsActive,rt.UpdatedOn,rt.UpdatedBy,r.Badge BIOMetricId,r.Designation,r.UserName
from [PROD].[RegTermination] rt
inner join [PROD].[Registration] r on r.id = rt.RegId
where rt.IsActive = 1 and r.superid = {0} order  by rt.id desc"""



##############################Reports ############
getReports = """SET NOCOUNT ON
DECLARE @Filter [PROD].[Type_RollCallReportFilter]
INSERT INTO @Filter (SuperId, ReportId, StartDate, EndDate, RegId, DeptId, AttendanceStatus, ShiftId, BranchId)
VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})
EXEC [PROD].[SP_RollCallGenerateReport] @Filter;
"""

############################login #######################
Loginquarry = """select u.id userid,u.SuperId,u.BranchId,u.FirstName,u.LastName,u.Mobile,u.Address,u.EmailId,u.RoleId,u.IsActive,r.RoleName,r.RoleLevel
from [PROD].[Users] u
inner join [PROD].[Roles] r on r.id = u.RoleId
where u.IsActive = 1 and u.LoginName = '{0}' and PasswordHash = '{1}'"""

#########################

getShiftsTypes = """select id shiftid,Name,CONVERT(varchar(8), StartTime, 108) AS StartTime,
    CONVERT(varchar(8), EndTime, 108) AS EndTime from [PROD].[Shifts] where SuperId = {0} and isactive = 1"""

assignshift = """insert into [PROD].[EmpShift] (regid,ShiftId,StartDate,EndDate)
values({0},{1},'{2}','{3}') """

getAssignshiftByEmp = """select r.id regid,r.Badge,r.CardId,r.UserName,r.Designation,es.ShiftId,es.StartDate,es.EndDate ,s.Name,s.Code
from [PROD].[EmpShift]  es
inner join [PROD].[Registration]  r on r.id = es.RegId
inner join [PROD].[Shifts] s on s.id = es.ShiftId
where es.IsActive =1 and r.id = {0} """

getEmpByShift = """SELECT RegId AS regid, UserName + ' - ' + Badge AS UserName
FROM prod.V_PrevShiftEmp
WHERE SuperId = {1} AND ShiftId = {0}"""

################leaves ##########

leavetypes = """Select LvType,LvTypeId From Prod.OrgLeaveTypes ORGLV INNER JOIN PROD.LeaveTypes LT ON ORGLV.LvTypeId = Lt.Id 
Where ORGLv.IsActive = 1 and ORGLv.SuperId = {0}"""

leaveaccruals = """Select LeaveTypeName,CarryForwardLeaves,Accrued,Taken,Balance, 1 'approved' ,1 'pending',3 'cancelled' 
 from Prod.V_LeaveAccruals 
Where RegId = {0} and Year ={1}"""

empleaves = """\
Select CardId,UserName,Badge,DeptId,DeptName,LvTypeId,LvType,LvCode,Id leaveid,RegId,LeaveCount,Status,\
CONVERT(VARCHAR, StartDt, 103) as StartDt,CONVERT(VARCHAR, EndDt, 103) as EndDt,Reason,Comments,CompOffDate,BranchId\
 from Prod.V_LeaveDetails Where RegId = {0} and Year(StartDt)={1}"""

leaverec = """\
SET NOCOUNT ON EXEC PROD.SP_InsertLeave {0}, {1}, {2}, {3}, '{4}', '{5}',{6},'{7}',1\
COMMIT"""



approveleave = """Update Prod.Leaves Set Status = {0},UpdatedBy={2},UpdatedOn=GetDate(),comments = '{3}' Where Id = {1} """


addmobileAccess = """update [PROD].[Registration] set MobileAccess = 1 where id = {0};
insert into [PROD].[RCEssentials] (regid,SuperId,Badge,UserName,AccessType,AccessPwd)
select id,SuperId,Badge,UserName,{1},{2} from [PROD].[Registration] where id = {0}"""

removemobileAccess = """update [PROD].[Registration] set MobileAccess = 0 where id = {0};"""


addempportalAccess = """update [PROD].[Registration] set EmpPortalAccess = 1 where id = {0};
insert into [PROD].[RCEssentials] (regid,SuperId,Badge,UserName,AccessType,AccessPwd)
select id,SuperId,Badge,UserName,{1},{2} from [PROD].[Registration] where id = {0}"""

removeempportalAccess = """update [PROD].[Registration] set EmpPortalAccess = 0 where id = {0};"""