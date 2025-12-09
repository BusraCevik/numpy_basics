import numpy as np

'''
Broadcasting allows NumPy to perform operations on arrays
with different shapes by virtually expanding dimensions
so they match the larger array's shape.

Two arrays are compatible when:
- the dimensions have the same size, or
- one of the dimensions has a size of 1

Example below demonstrates broadcasting with arrays of shape (1,3) and (4,1).
'''

array1 = np.array([[1, 2, 3]])
array2 = np.array([[1], [2], [3], [4]])

print("Array 1:")
print(array1)
print("Array 2:")
print(array2)
print("-----------")
print("Shapes:")
print(array1.shape)  # (1, 3)
print(array2.shape)  # (4, 1)

# They don't match exactly, but one of the dimensions is 1, so broadcasting is possible
print("-----------")
print("Result of array1 * array2:")

# ==================================================
# How broadcasting works:
#
# array1 shape (1,3) is broadcast to (4,3):
# [[1, 2, 3],
#  [1, 2, 3],
#  [1, 2, 3],
#  [1, 2, 3]]
#
# array2 shape (4,1) is broadcast to (4,3):
# [[1, 1, 1],
#  [2, 2, 2],
#  [3, 3, 3],
#  [4, 4, 4]]
#
# Element-wise multiplication:
# [[1*1, 2*1, 3*1],   -> [1, 2, 3]
#  [1*2, 2*2, 3*2],   -> [2, 4, 6]
#  [1*3, 2*3, 3*3],   -> [3, 6, 9]
#  [1*4, 2*4, 3*4]]   -> [4, 8, 12]
# ==================================================

print(array1 * array2)
