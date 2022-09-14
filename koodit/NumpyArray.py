import numpy as np

a = np.arange(25).reshape(5,5)

Slice1 = a[:, 1:4:2]
Slice2 = a[1:4:2, 0:3:2]
Slice3 = a[4, :]

print("Oranssi: ", Slice1)
print("Sininen: ", Slice2)
print("Keltainen: ", Slice3)
