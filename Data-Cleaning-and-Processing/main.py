#Task No 1 "Remove missing values from a Pandas DataFrame."

import pandas as pd
data = pd.read_csv('data1.csv')
df = pd.DataFrame(data)
df_clean = df.dropna()
print(df_clean)

# Task No 2 " Convert categorical variables into numerical values using Label Encoding."
import pandas as pd
from sklearn.preprocessing import LabelEncoder
aFrame
data = pd.read_csv('data1.csv')

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
label_encoder = LabelEncoder()

for column in df.select_dtypes(include=['object']).columns:
    df[column] = label_encoder.fit_transform(df[column])

print("\nDataFrame after Label Encoding:")
print(df)

#Task No 4 "Given a Pandas DataFrame, remove duplicate rows and reset the index of the DataFrame1"

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data =  pd.read_csv('data1.csv')
data_f = pd.DataFrame(data)
data_clean = data_f.drop_duplicates().reset_index(drop=True)
print(data_clean)

#Task No 5 " Implement a program that reads a CSV file into a Pandas DataFrame and handles missing values using Imputation1"

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('data1.csv')
data_f = pd.DataFrame(data)

data_clean = data_f.dropna()
print(data_clean)

Taskk No 6 "Create a function that takes a Pandas DataFrame and converts text data into numerical values using One-Hot Encoding1"

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def One_Hot_Encoding1(df):
  data_f = pd.DataFrame(df)
  result = pd.get_dummies(data_f, columns=['EMPLOYEE_ID', 'SALARY'], drop_first=True)
  print('The required Result is ',result)

data = pd.read_csv('data1.csv')
data_f = pd.DataFrame(data)
One_Hot_Encoding1(data_f)
plt.figure(figsize=(6, 4))
plt.title("One Hot Encoding")
sns.barplot(x=data_f.columns, y=data_f.count())
plt.show()

#TASK NO 7 " Given a Pandas DataFrame, normalize the numerical features using Z-Score Normalization"

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data1.csv')
df = pd.DataFrame(data)
df['SALARY'] = pd.to_numeric(df['SALARY'])
numeric_df = df.select_dtypes(include=[float, int])
data_clean = numeric_df.dropna()
print(data_clean['SALARY'])
vlue = sum(data_clean['SALARY'])
mean = np.mean(data_clean['SALARY'])
std = np.std(data_clean['SALARY'])

z_score = (vlue - mean)/std

print(f'Z Score of data is ',"{:.2f}".format(z_score))

#Task No 8 " Write a Python program that uses Scikit-Learn to perform data standardization on a dataset"

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('data1.csv')

print("Original Dataset:")
print(data)
numeric_df = data.select_dtypes(include=[float, int])
scaler = StandardScaler()
standardized_data = scaler.fit_transform(numeric_df)
standardized_df = pd.DataFrame(standardized_data, columns=numeric_df.columns)

non_numeric_df = data.select_dtypes(exclude=[float, int])
final_df = pd.concat([non_numeric_df.reset_index(drop=True), standardized_df], axis=1)

print("\nStandardized Dataset:")
print(final_df)

print("\nMean of Standardized Numeric Data:")
print(standardized_df.mean())
print("\nStandard Deviation of Standardized Numeric Data:")
print(standardized_df.std())

#Task No 9 "Implement a program that reads a JSON file into a Pandas DataFrame and handles outliers using Winsorization1"

import pandas as pd
import numpy as np
from scipy.stats import mstats

def read_and_winsorize(json_file, lower_limit=0.05, upper_limit=0.05):
  df = pd.read_json('example_2.json')
  print("Original DataFrame:")
  print(df.describe())
  df['winsorized'] = mstats.winsorize(df['value'],
                                      limits=[lower_limit, upper_limit])
  print("\nWinsorized DataFrame:")
  print(df.describe())

  return df

json_file_path = 'example_2.json'
result_df = read_and_winsorize(json_file_path)
result_df.to_json('example_2', orient='records', lines=True)

Task No 10 "Given a CSV file with customer details, preprocess the data for further analysis (e.g., handle missing values, scale  features)"

import pandas as pd
import seaborn as sns

data = pd.read_csv('data1.csv')
clean_data = data.dropna()
print(clean_data)

# Task NO 11 " Write a Python program that uses Scikit-Learn to perform data transformation using PCA (Principal Component (Analysis)"

Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = pd.read_csv("data1.csv")  # replace with your actual dataset
data.dropna(subset=['SALARY', 'EMPLOYEE_ID', 'DEPARTMENT_ID'], inplace=True)
X = data[['SALARY', 'EMPLOYEE_ID',
          'DEPARTMENT_ID']]  # Replace with your actual feature columns

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=2)  # Set the number of principal components you want

X_pca = pca.fit_transform(X_scaled)
print("Explained Variance Ratio:", pca.explained_variance_ratio_)

# Optional: Create a DataFrame of the PCA results for easier interpretation
pca_df = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
print(pca_df.head())

plt.scatter(pca_df['PC1'], pca_df['PC2'], edgecolor='k', s=100)
plt.title('PCA of Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(label='Target (Commission Percentage)')
plt.grid(True)
plt.show()

#Task No 12 "Implement a function that takes a Pandas DataFrame and performs data discretization on a numerical feature."

import pandas as pd

def discretize_feature(df, feature_name, bins, labels=None, strategy='equal-width'):
  if strategy == 'equal-width':
      discretized = pd.cut(df[feature_name], bins=bins, labels=labels, include_lowest=True)
  elif strategy == 'quantile':
      discretized = pd.qcut(df[feature_name], q=bins, labels=labels)
  else:
      raise ValueError("Strategy not supported. Use 'equal-width' or 'quantile'.")

  return discretized

data = pd.read_csv('data1.csv')              
d1 = data['SALARY']
d2 = data['JOB_ID']
dframe = {'SALARY':d1}
df = pd.DataFrame(dframe)

df['Age_binned'] = discretize_feature(df, 'SALARY', bins=3, labels=['SH_CLERK','AD_ASST','MK_MAN','MK_REP','HR_REP','PR_REP','AC_MGR','AC_ACCOUNT','AD_PRES','AD_VP','IT_PROG','FI_MGR','FI_ACCOUNT','PU_MAN','PU_CLERK','ST_MAN','ST_CLERK'])

# print(df)


import pandas as pd

def discretize_feature(df, feature_name, bins, labels=None, strategy='equal-width'):
    if strategy == 'equal-width':
        discretized = pd.cut(df[feature_name], bins=bins, labels=labels, include_lowest=True)
    elif strategy == 'quantile':
        discretized = pd.qcut(df[feature_name], q=bins, labels=labels)
    else:
        raise ValueError("Strategy not supported. Use 'equal-width' or 'quantile'.")

    return discretized

data = pd.read_csv('data1.csv')
d1 = data['SALARY']
df = pd.DataFrame({'SALARY': d1})

job_labels = ['SH_CLERK', 'AD_ASST', 'MK_MAN', 'MK_REP', 'HR_REP', 'PR_REP', 'AC_MGR', 'AC_ACCOUNT', 
              'AD_PRES', 'AD_VP', 'IT_PROG', 'FI_MGR', 'FI_ACCOUNT', 'PU_MAN', 'PU_CLERK', 'ST_MAN', 'ST_CLERK']

df['SALARY_binned'] = discretize_feature(df, 'SALARY', bins=len(job_labels), labels=job_labels)

print(df)