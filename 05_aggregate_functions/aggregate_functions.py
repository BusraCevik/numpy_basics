import numpy as np

# ==================================================
# Aggregate Functions
# ==================================================
'''
💡 Aggregate functions summarize data and typically return a single value.
They can also be applied along a specific axis (rows or columns).
'''

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

# ==================================================
# Basic aggregate operations
# ==================================================
print("Sum of all elements:", np.sum(array))
print("Average of all elements:", np.average(array))
print("Median of all elements:", np.median(array))
print("Standard deviation:", np.std(array))
print("50th percentile (median):", np.percentile(array, 50))
print("Variance:", np.var(array))
print("Maximum value:", np.max(array))
print("Minimum value:", np.min(array))
print("Index of maximum value:", np.argmax(array))
print("Index of minimum value:", np.argmin(array))

# ==================================================
# Aggregate along axes
# ==================================================
# Sum along columns (axis=0)
print("Sum along columns:", np.sum(array, axis=0))

# Sum along rows (axis=1)
print("Sum along rows:", np.sum(array, axis=1))
