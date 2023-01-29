import numpy as np

arr = [1,2,3,4,5,6,7,8,9]

print(type(arr))

a = np.array(arr)
print(type(a))
print(a.shape)
print(a.dtype)

print(a.ndim)

# for i in arr:
#     print(i)