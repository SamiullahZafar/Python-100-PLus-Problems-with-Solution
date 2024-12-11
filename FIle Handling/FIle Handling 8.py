# Task No 73 " Implement a function that takes a list of strings and returns a set of unique characters present in all string"


def unique_char(list):
  list = set(list)
  return list


list = [1, 2, 3, 4, 5, 1, 2, 3]
print(unique_char(list))
list = ["apple", "banana", "orange", "apple", "kiwi", "banana", "grape"]
print(unique_char(list))

# Task No 74 "Write a program that reads a text file and prints its contents"

r = open("my_file1.txt", "r")
print(r.read())
r.close()

# Task No 75 "Create a new text file and write some content into it"

from os import write

r = open("my_file1.txt", "w")
r.write("Hello World")
r.close()

r = open("my_file1.txt", "r")
print(r.read())
r.close()

# Task No 76 "Read a CSV file and process its data"

r = open("grades.csv", "r")
print(r.read())
r.close()

# Task No 77 "Write a Python program to copy the contents of one text file into another"

from os import write

r = open("my_file1.txt", "r+")
w = open("my_file2.txt", "r+")
w.write(r.read())
w.close()
r.close()
w = open("my_file2.txt", "r+")
print(w.read())
w.close()

# Task No 78 "Given a CSV file with student names and scores, find the student with the highest score)"

import pandas as pd

data = pd.read_csv("grades.csv")
print(max(data["Final"]))

# Task No 79 " Create a function that takes a list of sentences and writes them to a new text file, each on a new line)"

file = open("my_file1.txt", "a")
list = input("Enter the new line: ")
file.write(list)
file.close()
file = open("my_file1.txt", "r")
print(file.read())
file.close()

# Task No 80 "Given a CSV file with Studests details (name, age, salary), calculate the average final score of all students)"

import pandas as pd

data = pd.read_csv("grades.csv")
sum_final = sum(data["Final"])
avg = sum_final / len(data["Final"])
print("Average of Final marks of student is: ", avg)
data.close()

# Task No 81 "Write a program that reads a CSV file and finds the total sales revenue for a specific product"

import pandas as pd

data = pd.read_csv("grades.csv")
Sum = sum(data["Final"])
print("Total Marks in final is: ", Sum)

#Task NO 82 " Given a text file with a list of numbers, write a function that finds the numbers of students in the file"

import pandas as pd

data = pd.read_csv("grades.csv")
Sum = len(data["Final"])
print("Total Marks in final is: ", Sum)
