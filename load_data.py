import csv, sqlite3

con = sqlite3.connect("bems.db")
cursor = con.cursor()

reader = csv.reader(open('data.csv', 'r'), delimiter=',')

# csv 헤더 스킵
next(reader)

for row in reader:
    to_db = [ row[0], row[1], row[2], row[3] ]
    cursor.execute("INSERT INTO energy (date_time, b_code, usage, peak ) VALUES (?, ?, ?,?);", to_db)

con.commit()
con.close()