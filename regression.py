import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 생산량
output = [110, 125, 140, 145, 160, 166, 179, 190, 200, 215, 230, 250]
# 전력사용량
power_usage = [98, 115, 120, 136, 140, 156, 160, 177, 185, 195, 210, 225]
# p-value   : 유의 확률, 일반적으로 0.05 미만일 때 유의미
slope, intercept, r_value, p_value, stderr = stats.linregress(output, power_usage)

# 생산량 134개일 때 전기사용량 예측
product = 134
print("기울기(slope) : ", slope)
print("절편(intercept) : ", intercept)
print("상관계수(r_value) : ", r_value)
print("유의확률(p_value) : ", p_value )
print("{}개 => 예측량 {}kWh".format(product, product*slope + intercept))

plt.scatter(output, power_usage) 
x = np.arange(0, 300)
y = [(slope*num + intercept) for num in x]
plt.plot(x, y, 'b', lw=1) 
plt.xlabel("Output(EA)")
plt.ylabel("Power Usage(kWh)")
plt.show()
