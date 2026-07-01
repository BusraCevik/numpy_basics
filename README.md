# NumPy Basics

This repository documents my journey of learning **NumPy fundamentals** with clear explanations, practical examples, and small practice exercises.

---

## Purpose

The main goal of this repository is to build a strong foundation in numerical computing with Python and prepare for real-world data analysis and machine learning projects.

---

## Topics Covered

### 1. Introduction to NumPy
- **Core Concept:** NumPy (Numerical Python) is the foundational library for scientific computing in Python. It introduces the `ndarray` (N-dimensional array) object.
- **Key Advantage:** Unlike standard Python lists, NumPy arrays store data in contiguous memory blocks and enforce a single data type (`dtype`), enabling blazing-fast vectorized operations implemented in C.

### 2. Multidimensional Arrays
- **Core Concept:** Arrays can span multiple dimensions: 1D (vectors), 2D (matrices), and 3D or higher (tensors).
- **Key Attributes:**
  - `.shape`: Returns a tuple showing the size of the array along each axis (e.g., `(3, 4)` for 3 rows and 4 columns).
  - `.ndim`: Returns the number of array dimensions.
  - `.dtype`: Reveals the data type of the internal elements.

### 3. Slicing & Indexing
- **Core Concept:** Extracting specific subsets of data using the `start:stop:step` syntax across multiple axes simultaneously `[row_slice, column_slice]`.
- **The Memory Trap:** Slicing a Python list creates a deep copy, but slicing a NumPy array creates a **View**. Modifying a view directly mutates the original array because they share the same memory layout. Always use `.copy()` if safety is required.

### 4. Arithmetic Operations
- **Core Concept:** Standard operators (`+`, `-`, `*`, `/`) and mathematical functions (`np.sqrt()`, `np.sin()`) operate **element-wise** on arrays without explicit `for` loops.
- **Ufuncs:** These functions are known as Universal Functions (ufuncs), executing highly optimized, compiled C-code under the hood.

### 5. Broadcasting
- **Core Concept:** A powerful mechanism that allows arithmetic operations between arrays of different shapes by virtually expanding smaller dimensions to match larger ones.
- **Compatibility Protocol:** Dimensions are evaluated from right to left (trailing dimension first). Two axes are compatible only if they are **exactly equal in size**, or if **at least one of them is 1**.

### 6. Aggregate Functions
- **Core Concept:** Functions used to summarize full datasets or specific dimensions into compressed statistical metrics (`np.sum()`, `np.mean()`, `np.median()`, `np.std()`, `np.max()`).
- **Axis Control:** - `axis=0`: Collapses rows and operates vertically down columns.
  - `axis=1`: Collapses columns and operates horizontally across rows.
- **Dynamic Weights:** `np.average()` stands out from `np.mean()` by accepting a `weights` array parameter, crucial for processing real-world expected values.

### 7. Filtering (Boolean Indexing)
- **Core Concept:** Selecting specific elements that fulfill conditional statements (e.g., `matrix[matrix > 18]`). Evaluated conditions generate a Boolean Mask.
- **Operators:** Since element-wise logic is mandatory, standard Python `and`/`or` keywords cause failures. You must use bitwise operators `&` (AND), `|` (OR) wrapped inside strict parentheses `()`.
- **Ternary Mapping:** `np.where(condition, x, y)` creates a brand new structurally preserved array replacing elements based on truth value mapping.

### 8. Random Numbers
- **Core Concept:** Generating structured synthetic data, distributions, shuffling sequences, and extraction sampling.
- **Modern Architecture:** Legacy global states like `np.random.seed()` are deprecated. The modern standard relies on initiating an isolated Generator object via `np.random.default_rng(seed=1)`, providing superior statistical randomness and deterministic reproducibility.

---

## Notes

### I. Memory Mechanics: Views vs. Deep Copies
NumPy prioritizes performance. When you execute a slice like `sub_matrix = matrix[0:2, 0:2]`, NumPy avoids allocating new multi-gigabyte memory blocks. Instead, it builds a **View**—a lightweight pointer structure mapping directly to the original array's memory address space. 
* **Impact:** Modifying `sub_matrix[0,0] = 99` will instantly alter the baseline `matrix`.
* **Guardrail:** If independent manipulation is mandatory, decouple the relationship using the explicit duplication method: `safe_copy = matrix[0:2, 0:2].copy()`.

### II. Structural Integrity & Dimensionality Preservation
Standard scalar integer indexing flattens multi-dimensional spatial layouts.
* `matrix[:, 0]` extracts the first column but compresses the structural shape from a 2D matrix down into a flat 1D vector.
* `matrix[:, 0:1]` leverages slicing syntax, forcing NumPy to fully retain the explicit 2D structure (`N` rows, `1` column). Uniform structural preservation is critical when piping arrays into Scikit-Learn pipelines or neural network layers.

### III. The Strict Broadcasting Right-to-Left Alignment Rule
When performing math on mismatched shapes, NumPy aligns dimensions to the right:

```text
Example 1: (3, 4) and (4,)               Example 2: (3, 4) and (3,)
Matrix 1:  3  4                          Matrix 1:  3  4
Matrix 2:     4                          Matrix 2:     3
-----------------                        -----------------
Evaluation: Rightmost match (4=4).       Evaluation: Rightmost mismatch (4!=3).
            Leftmost fills with 1 (3=1).             Neither is 1.
Result: SUCCESS (Yields shape 3x4)       Result: CRASH (ValueError)
```

During successful broadcasting, NumPy manipulates strides (byte step jumps) at the internal C-level to simulate matrix expansion without cloning elements in memory.

### IV. Universal Functions (Ufuncs) & Optimization
NumPy bypasses slow Python dynamic typing loops by executing operations via compiled C-loops. Functions like `np.exp()`, `np.log()`, or operators like `+` are heavily vectorized. To locate coordinate layouts after aggregations without flattening geometry, combine structural wrappers: `np.unravel_index(np.argmax(matrix), matrix.shape)`.

### V. Large Scale Automated Weights Generation
In enterprise big-data environments, initializing manual matrices for `np.average(weights=...)` is impossible.
* **Condition-Based:** Utilize `np.where(customer_types == "Premium", 3.0, 1.0)` to instantly construct an automated, vectorized weights array matching massive shapes.
* **Feature-Based:** Bind raw continuous scale columns (e.g., customer wait durations, distances, or age distributions) straight as the weights vector parameter.

---

## Future Plans

- Real-life projects using NumPy
- Integration with Pandas & Matplotlib
- Data analysis & machine learning applications