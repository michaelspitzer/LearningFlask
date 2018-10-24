import pyodbc
import csv
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=10.111.17.47;"
                      "Database=AdventureWorks2017;"
                      "uid=GenericUser;"
                      "pwd=P@$$w0rd1!;"
                      "Trusted_Connection=yes;")

cursor = cnxn.cursor()

cursor.execute('SELECT * FROM sales.SalesOrderDetail where UnitPrice > 3000')
data=cursor.fetchall()

with open('dataTester.csv', 'w', newline='') as fp:
    a=csv.writer(fp, delimiter=',')
    for line in data:
        a.writerow(line)

for row in data:
    print (row[0],row[1],row[2],row[3],row[4],row[5],row[6])
cursor.close()
connection.close()


