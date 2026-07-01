import numpy as np

# ==================================================
# NumPy Version Check
# ==================================================
print(np.__version__)

# ==================================================
# Base Array Creation (2x5 Matrix)
# ==================================================
matrix = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10]])

# ==================================================
# Global Statistical Aggregations (Full Matrix)
# ==================================================
print("Sum of all elements:", np.sum(matrix))
print("Aremetic Mean:", np.mean(matrix))
print("Median value:", np.median(matrix))
print("Standard deviation:", np.std(matrix))
print("Variance:", np.var(matrix))
print("Max value:", np.max(matrix))
print("Min value:", np.min(matrix))

# Percentiles (Useful for statistical distribution and outlier detection)
print("50th percentile (Same as median):", np.percentile(matrix, 50))
print("90th percentile:", np.percentile(matrix, 90))

# ==================================================
# Contrast: np.mean() vs np.average() with Weights
# ==================================================
simple_array = np.array([10, 20, 30])
weights = np.array([0.1, 0.2, 0.7])

print("\nStandard Mean:", np.mean(simple_array))
print("Weighted Average (Using custom weights):", np.average(simple_array, weights=weights))

# ==================================================
# Advanced Dynamic Weight Generation (Scale-up Scenarios)
# ==================================================
# Scenario 1: Condition-Based Weight Allocation using np.where()
mock_ratings = np.array([5, 3, 4, 2, 5])
mock_customer_types = np.array([1, 0, 0, 1, 0])  # 1: Premium, 0: Normal
condition_weights = np.where(mock_customer_types == 1, 3.0, 1.0)
print("\nDynamic condition-based weights:", condition_weights)
print("Weighted average based on customer type:", np.average(mock_ratings, weights=condition_weights))

# Scenario 2: Function-Based Weight Assignment using continuous features
mock_satisfaction = np.array([8, 6, 9, 4])
mock_wait_times = np.array([15, 45, 10, 90])     # Continuous feature acting as weight
continuous_weights = mock_wait_times
print("Weighted average scaled directly by continuous wait times:", np.average(mock_satisfaction, weights=continuous_weights))

# ==================================================
# Spatial Aggregations Along Axes (Dimensionality Reduction)
# ==================================================
# axis=0: Collapses rows, operates vertically down columns
print("\nSum along columns (axis=0):", np.sum(matrix, axis=0))

# axis=1: Collapses columns, operates horizontally across rows
print("Sum along rows (axis=1):", np.sum(matrix, axis=1))

# ==================================================
# Index Tracking (Argmax & Argmin Coordinate Mapping)
# ==================================================
# Global argmax flattens the matrix by default
flat_max_idx = np.argmax(matrix)
print("\nFlattened index of maximum value:", flat_max_idx)

# Unraveling the flattened index to discover the exact 2D (row, col) coordinates
row_idx, col_idx = np.unravel_index(flat_max_idx, matrix.shape)
print(f"Exact 2D coordinates of maximum value: Row {row_idx}, Column {col_idx}")

# ==================================================
# Notes
# ==================================================
'''
Notes:

1. Axis Paradigm (Reduction Mechanics):
   - axis=0: Runs operations vertically down columns. It eliminates the row dimension.
   - axis=1: Runs operations horizontally across rows. It eliminates the column dimension.
   - Rule of thumb: The specified axis is the dimension that gets compressed/squashed.

2. Statistical Variations (mean vs average):
   - `np.mean()` computes strictly uniform unweighted averages.
   - `np.average()` supports the `weights` array parameter, essential for real-world business models 
     (e.g., calculating weighted metrics, expected values, or financial portfolio risk).

3. Scaled & Automated Weight Generation:
   - For massive production-level datasets, manually initializing weights is unfeasible.
   - `np.where(condition, x, y)` facilitates vectorized dynamic tracking to instantly build 
     conditional boolean weights arrays matching the exact size of the target matrix.
   - Continuous raw numeric metrics (e.g., age, duration, distance) can be bound straight as weights vectors.

4. Index Resolution (`np.unravel_index`):
   - Location functions like `argmax` and `argmin` view multidimensional arrays as 1D linear structures.
   - `np.unravel_index()` reconstructs structural spatial integrity, mapping the linear integer 
     back to accurate matrix index coordinates using the target shape template.
'''