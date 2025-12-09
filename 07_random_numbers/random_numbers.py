import numpy as np

# ==================================================
# Generating Random Numbers
# ==================================================
'''
💡 NumPy provides tools to generate random numbers, 
including integers, floats, shuffling arrays, and random selection.
'''

# ==================================================
# Random integers using the new Generator
# ==================================================
rng = np.random.default_rng(seed=1)  # seed ensures reproducibility
random_integers = rng.integers(0, 100, (3, 2))  # 3x2 array of integers from 0 to 99
print("Random integers (3x2):")
print(random_integers)
print("----------")

# ==================================================
# Random floats
# ==================================================
print("Random float [0,1):", np.random.uniform())
print("Random float in range [-1,1):", np.random.uniform(low=-1, high=1))
print("Random 3x2 floats in range [-1,1):", np.random.uniform(low=-1, high=1, size=(3, 2)))
print("Random 1D array of 3 floats in range [-1,1):", np.random.uniform(low=-1, high=1, size=3))
print("---------")

# ==================================================
# Shuffling an array
# ==================================================
rng = np.random.default_rng(seed=1)
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print("Shuffled array:")
print(array)

# ==================================================
# Random choice from an array
# ==================================================
fruits = np.array(["apple", "banana", "cherry"])
print("Original fruits array:", fruits)

# Single random choice
fruit = rng.choice(fruits)
print("Randomly selected fruit:", fruit)

# Random choice as an array of size 1
fruits_sample = rng.choice(fruits, size=1)
print("Random choice array of size 1:", fruits_sample)
