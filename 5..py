import numpy as np

ucs420_Madhav = np.array([[10,20,30,40],[50,60,70,80],[90,15,20,35]])
print(ucs420_Madhav)
print("Mean", np.mean(ucs420_Madhav))
print("Median", np.median(ucs420_Madhav))
print("Max", np.max(ucs420_Madhav))
print("Min", np.min(ucs420_Madhav))
print("Unique Elements", np.unique(ucs420_Madhav))

print("\n")
reshaped_ucs420_Madhav=ucs420_Madhav.reshape(4,3)
print(reshaped_ucs420_Madhav)
print("\n")
resized_ucs420_Madhav = np.resize(ucs420_Madhav,(2,3))
print(resized_ucs420_Madhav)
