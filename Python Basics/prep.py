# Importing the necessary libraries
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer as si
# Load the dataset
data=pd.read_csv(r'D:\Python Projects\csv\book1.csv')
print(data)
x=data.iloc[:,1:]
y=data.iloc[:,1:-1]
print(x)
print(y)
# Identify missing data (assumes that missing data is represented as NaN)
change=si(missing_values=np.NaN)
# Print the number of missing entries in each column
print(change)
# Configure an instance of the SimpleImputer class
change=si(missing_values=np.NaN, strategy='mean')
col=data.columns[1:]
# Fit the imputer on the DataFrame
change.fit(data[col])
# Apply the transform to the DataFrame
data=change.transform(data[col])
#Print your updated matrix of features
print(data)