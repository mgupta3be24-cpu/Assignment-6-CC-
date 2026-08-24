import numpy as np
#i.
arr=np.array([1,2,3,6,4,5])
print(arr)

reverse_arr = arr[::-1]
print(reverse_arr)

#ii.
#a.
x=np.array([1,2,3,4,5,1,2,1,1,1])
values, counts = np.unique(x, return_counts=True)
freq_x = values[np.argmax(counts)]
print("Index",np.argmax(counts))
print("Value",freq_x)
print("\n")

#b.
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3 ])
values_y, counts_y = np.unique(y, return_counts=True)
freq_y = values_y[np.argmax(counts_y)]
print("Index",np.argmax(counts_y))
print("Value",freq_y)

