import pyodbc

# Establish connection to the SQL Server
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=sql8002.site4now.net;'
                      'DATABASE=db_a99f12_qarcpayroll;'
                      'UID=db_a99f12_qarcpayroll_admin;'
                      'PWD=q@rcp@yr0ll')

# Create a cursor object
cursor = conn.cursor()

# SQL query to declare and insert values into a table variable
sql_query = """
SET NOCOUNT ON

DECLARE @Filter [PROD].[Type_RollCallReportFilter]
INSERT INTO @Filter (SuperId, ReportId, StartDate, EndDate, RegId, DeptId, AttendanceStatus, ShiftId, BranchId)
VALUES (10051, 4, '2024-01-09', '2024-01-10', 0, 0, null, 0, 0)
EXEC [PROD].[SP_RollCallGenerateReport] @Filter;
"""

# Execute the SQL query
cursor.execute(sql_query)

# Fetch the data, if any
data = cursor.fetchall()

# Close the cursor and connection
cursor.close()
conn.close()

# Print the fetched data
print(data)
