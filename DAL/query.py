
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
 where superid = {0} and isactive = 1 order by HolidayDt"""



#branche###########################
createbranch = """insert into [PROD].[Branches] (superid,name,code,CreatedBy,CreatedOn,IsActive)
values({0},'{1}','{2}',{3},DATEADD(MINUTE, 330, GETUTCDATE()),1) """

updatebranch = """update [PROD].[Branches] set superid = {0},name = '{1}',code = '{2}' ,UpdatedBy ={3} ,
UpdatedOn = DATEADD(MINUTE, 330, GETUTCDATE()) where id = {4} """

deletebranch = """update [PROD].[Branches] set isactive = 0,UpdatedOn = DATEADD(MINUTE, 330, GETUTCDATE()) where id = {0}"""

getbranches = """select id branchid,SuperId,Name,code from [PROD].[Branches] where SuperId = {0} and IsActive = 1 """

########################department
getdepartment = """select id departmentid,SuperId,Name,code from [PROD].[Department] where isactive = 1 and SuperId = {0}"""

createdepartment = """insert into [PROD].[Department] (SuperId,name,code,IsActive)
values({0},'{1}','{2}',1) """

updatedepartment = """update [PROD].[Department] set SuperId = {0},Name = '{1}' ,Code = '{2}' where id =  {3}"""

deletedepartment = """update [PROD].[Department] set isactive = 0  where id = {0}"""

###############Employee
createEmployee = """DECLARE @RegId INT;
insert into [PROD].[Registration](superid,Badge,UserName,DateOfBirth,Designation,CardId,Mobile,RFID,DateOfBirth,Gender)
values({0},{1},'{2}','{3}','{4}',{5},'{6}','{7}','{8}',{9})

SET @RegId = SCOPE_IDENTITY()

insert into [PROD].[EmpBranch](SuperId,RegId,BranchId)
values({0},@RegId ,{10})

insert into [PROD].[EmpDept] (regid,deptid)
values(@RegId ,{11})"""

updateEmployee = """update [PROD].[Registration] set superid = {0},Badge = {1},UserName = '{2}',DateOfBirth = '{3}',Designation = '{4}'
,CardId = {5},Mobile = '{6}',RFID = '{7}',DateOfBirth = '{8}',Gender = {9} where id = {12};

update  [PROD].[EmpBranch]set BranchId = {10} where RegId ={12};
update [PROD].[EmpDept] set deptid = {11} where regid = {12};"""

deleteEmployee = """update [PROD].[Registration] set IsActive = 0 where id = {0}"""

getEmployee = """
select r.id regid,r.superid,r.Badge,r.UserName,r.DateOfBirth,r.Designation,r.CardId,r.Mobile,r.RFID,r.DateOfBirth,r.Gender,emp.branchid,
b.Name branchname ,b.Code branchcode,ed.DeptId Departmentid ,d.Name Departmentname ,d.Code Departmentcode
from [PROD].[Registration] r
inner join [PROD].[EmpBranch] emp on emp.RegId = r.id
inner join [PROD].[Branches] b on b.id = emp.BranchId
inner join [PROD].[EmpDept] ed on ed.RegId = r.id
inner join [PROD].[Department] d on d.id = ed.deptid
where r.id = {0} and r.isactive = 1"""

###########################RegBankDetails
createRegBankDetails = """insert into [PROD].[RegBankDetails](SuperId,RegId,AccountNo,AccountHoldersName,BankName,BankBranch,IfscCode)
values({0},{1},'{2}','{3}','{4}','{5}','{6}')"""

updateRegBankDetails = """update [PROD].[RegBankDetails] set AccountNo = '{0}' ,AccountHoldersName ='{1}' ,BankName = '{2}',
BankBranch = '{3}',IfscCode = '{4}' where RegId = {5}"""

deleteRegBankDetails =  """update [PROD].[RegBankDetails] set IsActive = 0 where RegId = {0}"""

getRegBankDetails = """select SuperId,RegId,AccountNo,AccountHoldersName,BankName,BankBranch,IfscCode [PROD].[RegBankDetails] 
where regid = {0} and isactive = 1"""

###################RegProofs
createRegProofs = """insert into  [PROD].[RegProofs](SuperId,regid,pan,uan,adhaar,esi,pf,EPFStart,VoterId)
values({0},{1},'{2}','{3}','{4}','{5}','{6}','{7}','{8}') """

updateRegProofs = """update [PROD].[RegProofs] set pan = '{0}',uan = '{1}',adhaar = '{2}',esi = '{3}',pf = '{4}',EPFStart = '{5}',
VoterId = '{6}' where RegId = {7}"""

deleteRegProofs = """update [PROD].[RegProofs] set isactive = 0 where RegId = {0}"""

getRegProofs = """select SuperId,regid,pan,uan,adhaar,esi,pf,EPFStart,VoterId from [PROD].[RegProofs] 
where regid = {0} and isactive = 1 """

##########
createEmpManager = """insert into [PROD].[EmpManager] (superid,regid,ManagerId)
values({0},{1},{2})"""

updateEmpManager = """update [PROD].[EmpManager] set superid = {0} ,ManagerId = {2} where RegId = {1}"""

deleteEmpManager = """update [PROD].[EmpManager] set isactive  = 0 where RegId = """

##################
createRegDetails = """insert into [PROD].[RegDetails](superid,regid,emailid,EmergencyContactNo1,EmergencyContactNo2,CurrentAddress,PermanentAddress)
values({0},{1},'{2}','{3}','{4}','{5}','{6}') """

updateRegDetails = """update [PROD].[RegDetails] set emailid = '{0}',EmergencyContactNo1 = '{1}',EmergencyContactNo2 = '{2}',
CurrentAddress = '{3}',PermanentAddress = '{4}' where RegId =  {5}"""

deleteRegDetails = """update [PROD].[RegDetails] set IsActive = 0 where RegId = {0}"""

getRegDetails = """select superid,regid,emailid,EmergencyContactNo1,EmergencyContactNo2,CurrentAddress,PermanentAddress from [PROD].[RegDetails] 
where IsActive = 1 and RegId = {0} """

################
resignEmp = """insert into [PROD].[RegTermination](regid,TerminationDt,Reason,IsActive,UpdatedOn,UpdatedBy)
values(511,'2024-01-27','test',1,'2024-04-02',10);
update [PROD].[Registration] set IsActive = 0 where id = {0}"""

rejoinEmp = """update [PROD].[Registration] set IsActive = 1 where id = {0}
update [PROD].[RegTermination] set IsActive = 0 where regid = {0}"""

Terminatedlist = """select rt.regid,rt.TerminationDt,rt.Reason,rt.IsActive,rt.UpdatedOn,rt.UpdatedBy,r.Badge BIOMetricId,r.Designation,r.UserName
from [PROD].[RegTermination] rt
inner join [PROD].[Registration] r on r.id = rt.RegId
where rt.IsActive = 1 and rt.RegId = {0}"""


getReports = """SET NOCOUNT ON
DECLARE @Filter [PROD].[Type_RollCallReportFilter]
INSERT INTO @Filter (SuperId, ReportId, StartDate, EndDate, RegId, DeptId, AttendanceStatus, ShiftId, BranchId)
VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})
EXEC [PROD].[SP_RollCallGenerateReport] @Filter;
"""
