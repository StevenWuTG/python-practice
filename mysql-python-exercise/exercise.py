import mysql.connector

con = mysql-connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word=input("Enter the word: ")

wuery = cursor.execute("SELECT * FROM DICTIONARY")
results = cursor.fetchall()

print(results)