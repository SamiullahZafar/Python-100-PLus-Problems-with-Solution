#Task No 1 "Split data into training and testing sets using Scikit-Learn."

Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# Load the CSV file
data = pd.read_csv('data1.csv')

x = data.iloc[:,:-1]
y = data.iloc[:,-1]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state = 42)

print(f"Training Features Shape: {x_train.shape}")
print(f"Testing Features Shape: {x_test.shape}")
print(f"Training Labels Shape: {y_train.shape}")
print(f"Testing Labels Shape: {y_test.shape}")

#Test NO 2 "Train a Linear Regression model using Scikit-Learn."

from pandas.core.frame import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

data = pd.read_csv("data1.csv")
data_f = DataFrame(data)
data = data_f.dropna()

x = data.iloc[:,:-1]
y = data.iloc[:,-1]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size = 0.2, random_state = 42)

model = LinearRegression()

model.fit(x_train,y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Output the results
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Optional: Print the model coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

from pandas.core.frame import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

data = pd.read_csv("data1.csv")
data_f = DataFrame(data)
data = data_f.dropna()
print(data)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list.reverse()
print(list)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my = my_list[::-1]  # This reverses the list in place
print(my)     # Now print the reversed list

il = []
list =  ['my','name','is','Sami','Ullah']
for i in list:
  il.append(i[::-1])
print(il)

#Test NO 3 "Evaluate the performance of a model using accuracy score."

from sklearn.metrics import accuracy_score
import pandas as pd

# data = pd.read_csv('data.csv')
# dataf = DataFrame(data)
# y_true = dataf['target']
# y_pred = dataf['predicted']
# Example: Ground truth labels (true values)
y_true = [0, 1, 0, 1, 0, 1, 1]

# Example: Model predictions
y_pred = [0, 0, 0, 1, 0, 1, 1]

# Calculate accuracy score
accuracy = accuracy_score(y_true, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")