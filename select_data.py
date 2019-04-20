import sqlite3

con = sqlite3.connect("bems.db")

with con:
    cursor = con.cursor()
    # 2019년 01월 07일 15시 데이터만 조회
    cursor.execute(" SELECT date_time, usage, peak FROM energy \
                     WHERE b_code ='SGBD' AND date_time LIKE '2019010715%' ")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

con.close()