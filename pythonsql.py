import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",  #port erbij indien mac
  user="root",
  password="root",
  database="abc"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM telefoon")

myresult = mycursor.fetchall()

for x in myresult:
  print(x[2])

gaan = input("vul naam in")
sql = "INSERT INTO telefoon (merk, prijs) VALUES (%s, %s)"
val = (gaan, 21)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")