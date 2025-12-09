import numpy as np

# ==================================================
# NumPy Filtering
# ==================================================
'''
💡 Filtering (Boolean indexing) allows selecting elements of an array
that satisfy a condition.

Important:
- Using a Boolean mask like array[condition] **does NOT change the original array**.
- np.where(condition, x, y) **creates a new array**: elements where condition is True take x, else y.
'''

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

# ==================================================
# Basic Filtering
# ==================================================
teenagers = ages[ages < 18]
print("Teenagers (<18):", teenagers)

print("Original ages array (unchanged):")
print(ages)

adults = ages[(ages >= 18) & (ages <= 65)]
print("Adults (18-65):", adults)

seniors = ages[ages > 65]
print("Seniors (>65):", seniors)

evens = ages[ages % 2 == 0]
print("Even numbers:", evens)

odds = ages[ages % 2 == 1]
print("Odd numbers:", odds)

# ==================================================
# np.where
# ==================================================
'''
np.where(condition, x, y) returns a **new array**:
- elements where condition is True take the value from 'x'
- elements where condition is False take the value from 'y'
- original array remains unchanged
'''

adults_array = np.where(ages >= 18, ages, 0)
print("Adults using np.where (others set to 0):")
print(adults_array)
print("Original ages array still unchanged:")
print(ages)
