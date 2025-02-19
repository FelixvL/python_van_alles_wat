import pyodbc

server = 'datadbserverdamen.database.windows.net'
database = 'staging_elony'
username = 'admindamen'
password = 'uiop7890UIOP&*()'
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
)
cursor = conn.cursor()
cursor.execute("SELECT TOP 10 * FROM jouw_tabel")
for row in cursor.fetchall():
    print(row)