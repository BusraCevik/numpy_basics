import numpy as np

# ==================================================
# NumPy Version Check
# ==================================================
print(np.__version__)

# ==================================================
# Scalar Arithmetic (Vectorized Element-wise)
# ==================================================
# Operations between an array and a single value (scalar) are applied element-wise
array = np.array([1, 2, 3])
print("Original array:", array)

print("Add 1:", array + 1)
print("Subtract 1:", array - 1)
print("Multiply by 2:", array * 2)
print("Divide by 2:", array / 2)
print("Floor divide by 2:", array // 2)
print("Modulo 2:", array % 2)
print("Power of 2:", array ** 2)

# ==================================================
# Vectorized Math Functions (Ufuncs)
# ==================================================
# NumPy Universal Functions (ufuncs) perform fast, loopless element-wise operations
float_array = np.array([1.01, 2.5, 3.99])
print("\nSquare root:", np.sqrt(float_array))
print("Rounded:", np.round(float_array))
print("Floor:", np.floor(float_array))
print("Ceil:", np.ceil(float_array))

print("Sine:", np.sin(float_array))
print("Cosine:", np.cos(float_array))
print("Pi constant:", np.pi)

# ==================================================
# Mathematical Exercise: Circle Areas
# ==================================================
radii = np.array([1, 2, 3])
circle_areas = np.pi * (radii ** 2)
print("\nCircle areas for radii [1, 2, 3]:", circle_areas)

# ==================================================
# Element-wise Array Arithmetic vs Matrix Dot Product
# ==================================================
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Standard operators execute element-wise operations (Shapes must match or broadcast)
print("\nElement-wise Addition:", array1 + array2)
print("Element-wise Multiplication:", array1 * array2)
print("Element-wise Power:", array1 ** array2)

# Matrix Multiplication / Dot Product (The interview contrast)
# For 1D arrays, dot product calculates the inner product (1*4 + 2*5 + 3*6)
dot_product = np.dot(array1, array2)  # Or alternatively using the '@' operator: array1 @ array2
print("Matrix Dot Product (Scalar result):", dot_product)

# ==================================================
# Comparison Operators & Boolean Masking
# ==================================================
scores = np.array([91, 55, 100, 73, 82, 64])

# Step 1: Generate a Boolean Mask
boolean_mask = scores > 60
print("\nBoolean mask for scores > 60:\n", boolean_mask)

# Step 2: Use the mask to conditionally filter or update array values in-place
scores[scores < 60] = 0
print("Updated scores (values < 60 forced to 0):\n", scores)

# ==================================================
# Notes
# ==================================================
'''
Notes:

1. Universal Functions (Ufuncs):
   - Functions like `np.sqrt()`, `np.sin()`, and standard operators (+, -, *, /) are Ufuncs.
   - They execute highly optimized C-loops under the hood instead of slow native Python loops.
   - This architectural paradigm is known as Vectorization.

2. Element-wise Multiplication vs. Dot Product:
   - The `*` operator performs purely element-by-element math. Shapes must be identical.
   - The `@` operator or `np.dot()` performs linear algebra matrix multiplication.

3. Boolean Masking Mechanics:
   - Conditional statements evaluated on arrays generate a distinct array of Boolean flags.
   - Passing this boolean layout back into the bracket index maps strictly to 'True' coordinates.
   - This allows direct in-place mutation without spawning secondary temporary structures.
'''