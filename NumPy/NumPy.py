# Task No 108  "Create a NumPy array from a Python list and perform"

import numpy as np

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr = np.array(list)

print("NumPy Array: ", arr)
print("NumPy Array Addition: ", arr + 1)
print("NumPy Array Subtraction: ", arr - 1)
print("NumPy Array Multiplication: ", arr * 2)
print("NumPy Array Division: ", arr / 2)

# Task No 109  "Generate a NumPy array of random numbers and calculate its mean, median, and standard deviation"

import numpy as np
from scipy import stats

data = np.array([
    12, 45, 67, 34, 89, 23, 56, 78, 90, 11, 13, 57, 68, 34, 25, 47, 88, 99, 41,
    22, 34
])

# Calculate the mean
mean = np.mean(data)
print(f"Mean: {mean}")  # Output: Mean: 49.95

# Calculate the median
median = np.median(data)
print(f"Median: {median}")  # Output: Median: 46.0

# Calculate the mode
mode = stats.mode(data)
print("Mode: ", mode)  # Output: Mode: 34

stand = np.std(data)
print("Standard Deviation: ", stand)

#Task No 110 "Create a NumPy array and reshape it into a different shape"

import numpy as np

array = np.arange(1, 21)
print("Original Array is: ", array)

reshaped_array = array.reshape(4, 5)
print("Reshaped Array is: \n", reshaped_array)

#Task No 111 " Given a list of numbers, create a NumPy array and find the sum and product of its elements1"

import numpy as np

array1 = np.arange(1, 21)
array2 = np.arange(1, 21)
arr1 = array1.reshape(4, 5)
arr2 = array2.reshape(4, 5)
print("Reshaped Array is: \n", arr1)
print("Reshaped Array is: \n", arr2)
addi = array1 + array2
print("Sum of Array is: ", addi)
dote = np.dot(array1, array2)
print("Dot product is: ", dote)

#Task No 112 "Implement a program that generates a NumPy array with numbers from 0 to 9 and reshapes it into a 3x3 matrix"

import numpy as np

array = np.arange(0, 9)
print("Original Array is: ", array)

array_shape = array.reshape(3, 3)
print("Reshaped Array is: \n", array_shape)

#Task No 113 "Write a Python program that uses NumPy to find the mean, median, and standard deviation of a dataset1"

import numpy as np

array = np.arange(0, 60)

Mean = np.mean(array)
print("Mean of the array is: ", Mean)
Median = np.median(array)
print("Median of the array is: ", Median)
stan = np.std(array)
print("Standard Deviation of the array is: ", stan)

#Task No 114 "Create a function that takes a list of numbers and returns the NumPy array sorted in ascending order1"

import numpy as np


class sorted:

  def __init__(self, list):
    self.list = list

  def Srt(self):
    sorted_array = np.sort(self.list)
    return sorted_array


list = [2, 2, 5, 8, 11, 2, 3, 5, 7, 10, 26, 45, 78, 90, 75]
obj = sorted(list)
print("Roted ascending order array is: ", obj.Srt())

#Task No 115 "Given a list of lists, create a 2D NumPy array and find the sum of elements in each row and column"

import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Array is: ", array)
sum = np.sum(array, axis=0)
print("Sum of elements in each row: ", sum)
sum1 = np.sum(array, axis=1)
print("Sum of elements in each column: ", sum1)

#Task No 116 "Implement a program that generates a random NumPy array and finds the maximum and minimum values1"

import numpy as np

array = np.random.randint(0, 100, size=20)
print(array)
max = np.max(array)
print("Maximum number in Array is: ", max)
min = np.min(array)
print("Minimun number in Array is: ", min)

#Task No 117 Write a function that takes a NumPy array and returns a new array with all elements squared

import numpy as np


def squ(array):
  square = np.square(array)
  return square


array = np.random.randint(0, 100, size=20)
print("Original Array is: \n")
print(array)
print("Asrray with Square is: \n", squ(array))

#Task No 118 "Given a NumPy array, calculate the dot product of the array with itself"

import numpy as np

array1 = np.random.randint(0, 100, size=(2, 2))
array2 = np.random.randint(0, 100, size=(2, 2))
print("Ogiginal Array is: \n")
print(array1, "\n\n", array2)
Dot = np.dot(array1, array2)
print("Dot product of Arrays is: ", Dot)

#Task No 119 "Create a program that uses NumPy to calculate the inverse of a 2x2 matrix"

import numpy as np

array1 = np.random.randint(0, 100, size=(3, 3))
print(array1)
inv_zero = np.linalg.det(array1)
if inv_zero != 0:
  inverse = np.linalg.inv(array1)
  print("Inverse of Array is: ", inverse)
else:
  print("Inverse of Array is: ", inv_zero)

#Task No 120 "Implement a function that takes a NumPy array and returns the transpose of the arra"

import numpy as np

array1 = np.random.randint(0, 100, size=(3, 3))
print("Original Matrix is: \n", array1)

transpose = np.transpose(array1)
print("Transpose of Matrix is: \n", transpose)
