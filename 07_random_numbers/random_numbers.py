import numpy as np

# ==================================================
# NumPy Version Check
# ==================================================
print(np.__version__)

# ==================================================
# The Modern Way: Initializing the Generator
# ==================================================
# Setting a seed ensures exact reproducibility across different machine executions
rng = np.random.default_rng(seed=1)

# ==================================================
# Random Integers
# ==================================================
# Generates a 3x2 matrix with values from 0 up to (but excluding) 100
random_integers = rng.integers(low=0, high=100, size=(3, 2))
print("Random integers (3x2):\n", random_integers)

# ==================================================
# Random Floats (Uniform Distribution)
# ==================================================
# Modern replacement for legacy np.random.uniform()
print("\nRandom float [0.0, 1.0):", rng.uniform())
print("Random float in range [-1, 1):", rng.uniform(low=-1, high=1))
print("Random 3x2 matrix of floats [-1, 1):\n", rng.uniform(low=-1, high=1, size=(3, 2)))
print("Random 1D array of 3 floats [-1, 1):", rng.uniform(low=-1, high=1, size=3))

# ==================================================
# Sequence Shuffling: In-place vs Copying
# ==================================================
base_array = np.array([1, 2, 3, 4, 5])

# 1. rng.shuffle() mutates the original array directly (In-place)
rng.shuffle(base_array)
print("\nShuffled array (Original array changed):", base_array)

# 2. rng.permutation() returns a brand new shuffled copy, preserving the original array
fresh_array = np.array([10, 20, 30, 40, 50])
shuffled_copy = rng.permutation(fresh_array)
print("Shuffled copy via permutation:", shuffled_copy)
print("Original array after permutation (Unchanged):", fresh_array)

# ==================================================
# Random Choice & Selection
# ==================================================
fruits = np.array(["apple", "banana", "cherry", "date"])

# Single random extraction
single_fruit = rng.choice(fruits)
print("\nRandomly selected single fruit:", single_fruit)

# Random sample extraction (returns a matching NumPy structural array)
fruits_sample = rng.choice(fruits, size=2, replace=False) # replace=False prevents pulling the same element twice
print("Random choice sample array (size 2, no replacement):", fruits_sample)

# ==================================================
# Notes
# ==================================================
'''
Notes:

1. Legacy vs. Modern Generator API:
   - Old school syntax like `np.random.seed()` and `np.random.randint()` relies on a global random state.
   - Modern syntax utilizes `np.random.default_rng()`, spawning an isolated, faster, and statistically 
     superior PCG64 pseudo-random number generator object.

2. Deterministic Reproducibility:
   - The `seed` argument anchors the internal mathematical algorithms to a specific initialization node.
   - This ensures that anyone executing the code will yield identical array generations, critical for 
     academic cross-validation and deep learning training alignment.

3. Shuffling Paradigms:
   - Use `rng.shuffle()` when memory efficiency is paramount and mutating the original layout is intented.
   - Use `rng.permutation()` when structural preservation of the input baseline sequence is mandatory.
'''