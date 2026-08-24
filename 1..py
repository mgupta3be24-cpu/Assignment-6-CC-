import numpy as np
arr = [1, 2, 3 ,4, 5]
u =[]

add=[2,2,2,2,2]

for n,m in zip(arr , add):
    u.append(n+m)
print(u)

mul=[3,3,3,3,3]
u2=[]
for n, m in zip(arr, mul):
    u2.append(n * m)
print(u2)

div=[2,2,2,2,2]
u3=[]
for n, m in zip(arr, div):
    u3.append(n / m)
print(u3)