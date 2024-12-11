#Task No 1 "Create a simple line plot using Matplotlib to visualize a series of data points."

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
x = df['SALARY']
y = df['EMPLOYEE_ID']
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#Task NO 2 " Generate a scatter plot using Matplotlib to visualize the relationship between two variables."

import matplotlib.pyplot as plt

import pandas as pd

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
x = df['SALARY']
y = df['EMPLOYEE_ID']
plt.scatter(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show

#Task NO 3 "Create a bar plot using Seaborn to compare the categories in a dataset."
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')
sns.set(style="whitegrid")
plt.figure(figsize=(7, 4))
bar_plot = sns.barplot(x=data['HIRE_DATE'], y=data['SALARY'], data=data)

bar_plot.set_title('Salary By Date of Hire')
bar_plot.set_xlabel('Day of the Week')
bar_plot.set_ylabel('Total Bill')

plt.show()

#Task NO 3 "Given a Pandas DataFrame, create a line plot to visualize the trend of a specific column over time."

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')
sns.set(style="whitegrid")
plt.figure(figsize=(7, 4))
bar_plot = sns.lineplot(x=data['HIRE_DATE'], y=data['SALARY'], data=data)

bar_plot.set_title('Salary By Date of Hire')
bar_plot.set_xlabel('Day of the Week')
bar_plot.set_ylabel('Total Bill')

plt.show()

#Task No 4 "Implement a program that generates a histogram using Matplotlib to visualize the distribution of data."

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')
sns.set(style="whitegrid")
plt.figure(figsize=(7, 4))
bar_plot = sns.histplot(x=data['HIRE_DATE'], y=data['SALARY'], data=data)

bar_plot.set_title('Salary By Date of Hire')
bar_plot.set_xlabel('Day of the Week')
bar_plot.set_ylabel('Total Bill')

plt.show()

#Task No 5 "Write a Python program that uses Seaborn to create a scatter plot matrix for multiple variables in a DataFrame."

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')
sns.set(style="whitegrid")
plt.figure(figsize=(7, 4))
bar_plot = sns.pairplot(data)

plt.show()

#Task NO 6 "Create a function that takes a Pandas DataFrame and generates a box plot to visualize the distribution of data."

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def box_plot(df):
  sns.boxplot(df)
  plt.figure(figsize=(8,6))
  plt.title("Line Plot")
  plt.xlabel('x axis')
  plt.ylabel('y axis')
  plt.show()
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
box_plot(df)

#Task NO 7 'Given a CSV file with sales data, use Matplotlib to create a bar plot to compare the sales of different products.

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('data.csv')

y = data['SALARY']
x = data['DEPARTMENT_ID']

plt.bar(x,y)
plt.title("Bar Graph using Matployt Lib")
plt.xlabel("Salary")
plt.ylabel("Department ID")
plt.show()

#Task NO 8 "Implement a program that reads a JSON file into a Pandas DataFrame and uses Seaborn to create a violin plot "

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_json('data.json')
sns.violinplot(x=data['sports'], y=data['maths'], data=data)
plt.title("Voinlin Plot")
plt.xlabel("Sports")
plt.ylabel('Maths')
plt.show()

#Task No 9 " Write a function that takes a Pandas DataFrame and generates a pair plot to visualize the relationships between variables"

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')
sns.pairplot(data)
plt.show()

#Task NO 10 "Write a function that takes a Pandas DataFrame and generates a pair plot to visualize the relationships  between variables"

import pandas as pd
from pandas.core.frame import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
df = DataFrame(data)
custom_palette = ['#FF5733', '#33FF57', '#3357FF']
sns.pairplot(df)
plt.figure(figsize=(6, 4))
plt.show()
# Load example dataset
iris = sns.load_dataset('iris')
print(iris)
plt.show()

Create pair plot
sns.pairplot(iris, hue='species')

#Task No 11 " Given a Pandas DataFrame, create a pie chart using Matplotlib to visualize the distribution of data in a specific column"

import pandas as pd
import seaborn as sns
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
df = DataFrame(data)
plt.pie(df['SALARY'], labels=df['DEPARTMENT_ID'])
plt.show()

#Tsk NO 12 "Create a program that reads a CSV file into a Pandas DataFrame and uses Seaborn to create a swarm plot for  data visualization"

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.core.frame import DataFrame

data = pd.read_csv('data.csv')
df = DataFrame(data)
sns.swarmplot(x=df['SALARY'], y=df['DEPARTMENT_ID'])
plt.show()

#Tsk NO 13 "# Implement a function that takes a Pandas DataFrame and generates a heatmap using Seaborn to visualize the correlation between variables."

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data directly as a DataFrame
data = pd.read_csv('data.csv')

# Select only numeric columns
numeric_df = data.select_dtypes(include=[float, int])

# Create the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap of Correlation Matrix")
plt.show()
