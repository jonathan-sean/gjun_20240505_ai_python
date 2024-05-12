import math

# 圓面積=pi * r^2, pi: 圓周率, r: 半徑
r=10
#pi=3.14159
a=round((math.pi * r**2), 2)
print(str.format("圓面積 - 半徑: {}, 面積: {}", r, a))