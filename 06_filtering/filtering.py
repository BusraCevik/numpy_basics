import numpy as np

# ==================================================
# NumPy Version Check
# ==================================================
print(np.__version__)

# ==================================================
# Base Array Creation (2x8 Matrix)
# ==================================================
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

print("Original Ages Matrix:\n", ages)

# ==================================================
# Boolean Indexing (Filtreleme -> 1D Vector output)
# ==================================================
# Single condition
teenagers = ages[ages < 18]
print("\nTeenagers (<18):", teenagers)

# Multiple conditions using Bitwise AND (&) - Parentheses are mandatory
adults = ages[(ages >= 18) & (ages <= 65)]
print("Adults (18-65):", adults)

seniors = ages[ages > 65]
print("Seniors (>65):", seniors)

# Modulo filtering
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 == 1]
print("Even ages:", evens)
print("Odd ages:", odds)

# ==================================================
# Universal Conditional Element Selection: np.where()
# ==================================================
# Approach 1: 3-Parameter Mode -> np.where(condition, if_true, if_false)
# Creates a brand new array matching the original structural shape
adults_clean_matrix = np.where(ages >= 18, ages, 0)
print("\nMatrix using np.where (Non-adults forced to 0):\n", adults_clean_matrix)

# Approach 2: 1-Parameter Mode -> np.where(condition)
# Returns a tuple of arrays representing the exact spatial coordinates (indices)
row_indices, col_indices = np.where(ages > 65)
print("\nCoordinates where age is > 65:")
print("Row indices:", row_indices)
print("Column indices:", col_indices)
print("Exact located value:", ages[row_indices, col_indices])

# ==================================================
# Notes
# ==================================================
'''
Notes:

1. The Vectorized Flattening Phenomenon:
   - Filtering a multidimensional matrix with a boolean mask `matrix[mask]` flattens the result into 1D.
   - Reason: NumPy cannot guarantee a symmetrical geometric matrix structure since the matching 
     elements might be randomly distributed across different rows and columns.

2. Bitwise Operators (`&`, `|`) vs Python Logical Keywords (`and`, `or`):
   - Standart short-circuit `and`/`or` keywords evaluate truth value of an entire array, triggering a ValueError.
   - Vectorized environments require element-wise evaluation, achieved strictly via `&` (AND) and `|` (OR).
   - Each conditional evaluation chunk must be strictly wrapped inside isolated parentheses `()`.

3. Dual Architecture of `np.where()`:
   - When fed with 3 arguments, it acts as a functional element-wise ternary operator (transforms data while preserving shape).
   - When fed with 1 argument (only condition), it switches behavior to return tuple-based coordinate indices.
'''