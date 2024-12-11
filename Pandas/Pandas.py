#Task No 1 "Create a Pandas Series from a Python list and perform basic operations like filtering, sorting, etc."

import pandas as pd

my_list = [23, 1, 45, 32, 12, 87, 54, 9, 34, 76, 3, 65, 29, 8, 15, 90, 41, 27, 14, 5]
mylist = pd.Series(my_list)
flist = mylist[mylist > 15]
print(flist)
#Ascending order
mylist = mylist.sort_values()
print(mylist)
#descending order
mylist = mylist.sort_values(ascending = False)
print(mylist)

#Task NO 2 "Read a CSV file into a Pandas DataFrame and perform basic data manipulation operations."

import pandas as pd

data = pd.read_csv("data.csv")
cou = len(data["EMPLOYEE_ID"])
print("Number of employees: ", cou)
s = sum(data["SALARY"])
print("Total Salary : ",s)

#Task No 3 "Create a Pandas DataFrame from a dictionary and perform filtering and grouping operations."

import pandas as pd

data = {
    'name': ['sami', 'ehsan', 'ehsan', 'arzoo'],
    'age': [23, 24, 25, 60],
    'salary': [12000, 13000, 15000, 16000]
}
print("Origignal Dictionary is: ", data)
data_f = pd.DataFrame(data)
print("Print the framed Dictionary: ", data_f)

fd = data_f[data_f['age'] > 30]
print("Print the data greater the 30 is: ", fd)

# TAsk 4 "Given a CSV file with student details, read it into a Pandas DataFrame and find the average Salary of Employee,"

import pandas as pd

data = pd.read_csv('data.csv')
data_f = pd.DataFrame(data)
average = data_f['SALARY'].mean()
print("Average Salary of Employee is: ", average)

#Task No 5 "Implement a program that generates a Pandas Series with dates and filter it to get dates in a specific range,"

import pandas as pd

data = pd.date_range(start='07-JUN-02', end='30-SEP-05')
print(data)

#Task NO 6 "Write a Python program that uses Pandas to read a CSV file and find the maximum and minimum values in each column"

import pandas as pd

data = pd.read_csv('data.csv')
max_val  = max(data['SALARY'])
min_val = max(data['SALARY'])
print("Maximum Salary is: ", max_val)
print("Minimum Salary is: ", min_val)

#Task NO 7 " Create a function that takes a Pandas DataFrame and returns a new DataFrame with rows sorted in ascending   order,"

import pandas as pd

def order_list(df):
  data_s = df.sort_values(by='SALARY', ascending=True)
  return data_s

data = pd.read_csv('data.csv')
df = pd.DataFrame(data['SALARY'])
data_s = order_list(df)
print("Sorted Data is: ", data_s)

#Task no 8 "Given a Pandas DataFrame, filter the rows to include only the rows where a specific column meets a condition,"

import pandas as pd

def filter_rows(df, column_name, condition):
    filtered_df = df[df[column_name].apply(condition)]
    return filtered_df

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
condition = lambda x: x > 50000
filtered_df = filter_rows(df, 'SALARY', condition)
print("Data greater than 15000 is: ", filtered_df)

#Task no 9 "Implement a program that reads a CSV file into a Pandas DataFrame and calculates the sum of a specific column,"

import pandas as pd

data = pd.read_csv('data.csv')
df =  pd.DataFrame(data)
sum = df['SALARY'].sum()
print("Sum of All Salaries is: ", sum)

#Task No 9 "Write a function that takes a Pandas DataFrame and adds a  new calculated column to the DataFrame,"

import pandas as pd

def add_calculated_column(df, new_column_name, calculation):
    df[new_column_name] = df.apply(calculation, axis=1)
    return df

data = pd.read_csv('data.csv')

df = pd.DataFrame(data)
bonus = 20000
calculation = lambda row: row['SALARY'] + bonus
df = add_calculated_column(df, 'Bonus', calculation)

print("DataFrame with new calculated column:")
print(df_with_new_column)

#Task No 10 "Given a Pandas DataFrame, group the data by a specific column and calculate the mean of another column,"

import pandas as pd


def group_data(df, column, column_t):
    final_result = df.groupby(column)[column_t].mean().reset_index()
    return final_result


data = pd.read_csv("data.csv")

df = pd.DataFrame(data)
result = group_data(df, 'FIRST_NAME', 'SALARY')
print("Gouped Data is: ", result)

#Task No 11 "Create a program that reads a JSON file into a Pandas DataFrame and extracts specific information from it," 

import pandas as pd
import json

data = json.load(open('product.json'))
data_f = pd.DataFrame(data)
print("Available information in Json File: ", data_f)

Task No 12 " Implement a function that takes a Pandas DataFrame and returns the transpose of the DataFrame"

import pandas as pd

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
result = df.transpose()
print("Transpose of dataframe is: ", result)