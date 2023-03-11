import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-UF559B1\SQLEXPRESS;"
                      "Database=BigData;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM HappyIndex_2015')

for row in cursor:
    print('%r' % (row,))

#Add new string
print('\r Tatarstan,', ' Europe,', '260.0,', '1.839,',
       '0.06727,', '0.20868,', '0.13995,', '0.28443,', '0.36453,', '0.10731,', '0.16681,', '1.56726,')