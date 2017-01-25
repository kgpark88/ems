import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

con = sqlite3.connect("bems.db")
sql =" SELECT date_time, usage, peak FROM energy "
df = pd.read_sql(sql , con=con) 
con.close()

print("전력사용량")
print(df)
print("\n전력사용량 통계")
print(df.describe())
df.plot(title="POWER USAGE",  figsize=(10, 3), ylim=(0,2000) )
plt.show()