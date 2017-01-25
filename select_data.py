import sqlite3

con = sqlite3.connect("bems.db")

with con:     
    cursor = con.cursor()   
    # 2016년 1월 10일 10일의 10시대의 데이터만 조회
    cursor.execute(" SELECT date_time, usage, peak FROM energy \
                     WHERE b_code ='SGBD' AND date_time LIKE '2016011010%' ")

    rows = cursor.fetchall()

    for row in rows:
        print(row)        
        
con.close()