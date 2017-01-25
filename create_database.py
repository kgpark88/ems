import sqlite3

# 데이터베이스 생성 및 접속
con = sqlite3.connect("bems.db")
cursor = con.cursor()

# energy 테이블 생성
cursor.executescript("""
    DROP TABLE IF EXISTS energy; 
    CREATE TABLE energy( date_time, b_code text, usage real, peak real, 
    unit_price real, temp real, rh real ); """)

# energy 테이블에 데이터 추가 
cursor.execute("INSERT INTO  energy VALUES('201501271200', 'SGBD', 424.8, 1699.2, 100, 7, 50   )")
cursor.execute("INSERT INTO  energy VALUES('201501271215', 'SGBD', 434.8, 1799.2, 100, 8, 52   )")
cursor.execute("INSERT INTO  energy VALUES('201501271230', 'SGBD', 444.8, 1899.2, 100, 9, 55   )")
cursor.execute("INSERT INTO  energy VALUES('201501271245', 'SGBD', 454.8, 1799.2, 100, 8, 59   )")

con.commit()
con.close()
