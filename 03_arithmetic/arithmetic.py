import numpy as np

# ==================================================
# Scalar Arithmetic
# ==================================================
'''
💡 Scalar arithmetic: performing arithmetic operations between an array and a single value (scalar).
The operation is applied element-wise.
'''

array = np.array([1, 2, 3])
print("Original array:", array)

print("Add 1:", array + 1)   # each element +1 → [2, 3, 4]
print("Subtract 1:", array - 1)
print("Multiply by 2:", array * 2)
print("Divide by 2:", array / 2)
print("Floor divide by 2:", array // 2)
print("Modulo 2:", array % 2)
print("Power of 2:", array ** 2)
print("--------------")

# ==================================================
# Vectorized Math Functions
# ==================================================
'''
💡 Vectorized functions: NumPy provides functions that operate element-wise on arrays without explicit loops.
'''

array = np.array([1.01, 2.5, 3.99])
print("Square root:", np.sqrt(array))
print("Rounded:", np.round(array))
print("Floor:", np.floor(array))
print("Ceil:", np.ceil(array))

print("Sine:", np.sin(array))
print("Cosine:", np.cos(array))
print("Tangent:", np.tan(array))
print("Pi constant:", np.pi)
print("--------")

# ==================================================
# Exercise: Circle Areas
# ==================================================
radii = np.array([1, 2, 3])
# Area = pi * r^2
print("Circle areas:", np.pi * radii ** 2)
print("--------")

# ==================================================
# Element-wise Array Arithmetic
# ==================================================
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print("Addition:", array1 + array2)
print("Subtraction:", array1 - array2)
print("Multiplication:", array1 * array2)
print("Division:", array1 / array2)
print("Power:", array1 ** array2)
print("--------")

# ==================================================
# Comparison Operators
# ==================================================
scores = np.array([91, 55, 100, 73, 82, 64])
print("Equals 100:", scores == 100)
print("Greater than 60:", scores > 60)

# Using comparison to update array values
scores[scores < 60] = 0
print("Updated scores (values <60 set to 0):", scores)
