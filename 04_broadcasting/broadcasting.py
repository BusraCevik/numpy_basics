import numpy as np

# ==================================================
# NumPy Version Check
# ==================================================
print(np.__version__)

# ==================================================
# 2D Array with 2D Array Broadcasting (Outer Product Match)
# ==================================================
# Array 1 shape: (1, 3)
# Array 2 shape: (4, 1)
array1 = np.array([[1, 2, 3]])
array2 = np.array([[1], [2], [3], [4]])

print("Array 1:\n", array1)
print("Array 2:\n", array2)
print("Shapes:", array1.shape, "and", array2.shape)

# Virtual expansion maps both matrices to a common shape of (4, 3)
print("\nResult of array1 * array2 (Both dimensions broadcasted):\n", array1 * array2)

# ==================================================
# 2D Matrix with 1D Vector Broadcasting (Common Practical Scenario)
# ==================================================
# Matrix shape: (3, 3)
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

# Vector shape: (3,) -> 1D Array
vector = np.array([1, 2, 3])

print("\nMatrix shape:", matrix.shape, "Vector shape:", vector.shape)
# Right-to-left alignment check:
# Matrix: 3 x 3
# Vector:     3  -> Matches trailing dimension. Sola 1 eklenir -> (1, 3) olarak broadcat edilir.
print("Result of matrix + vector (Vector added to each row):\n", matrix + vector)

# ==================================================
# Notes
# ==================================================
'''
Notes:

1. What is Broadcasting:
   - Broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.
   - It allows element-wise operations without duplicating data in memory, maximizing performance.

2. The Strict Two-Rule Compatibility Protocol:
   - NumPy compares array dimensions element-wise, starting from the trailing (rightmost) dimension and moving left.
   - Dimensions are compatible if:
     a) They are exactly equal in size.
     b) One of them is exactly 1.
   - If neither condition is met, a `ValueError: operands could not be broadcast together` is raised.

3. Memory Efficiency:
   - NumPy does not actually copy the values or create redundant arrays in memory during broadcasting.
   - Instead, it cleverly manipulates the array strides (byte steps) at the C-internal level to simulate expansion.
'''