import pandas as pd

# Load CSV file into a DataFrame
data = pd.read_csv('01.Data Cleaning and Preprocessing.csv')

# Display the type of the object
print(type(data))

# Get information about the DataFrame
print(data.info())

# Get descriptive statistics of the DataFrame
print(data.describe())

# Drop duplicate rows
data = data.drop_duplicates()
print(data)

# Check for missing values
print(data.isnull())
print(data.isnull().sum())

# Check for non-missing values
print(data.notnull())

# Count total missing values
total_missing = data.isnull().sum().sum()
print(total_missing)

# Fill missing values with 0 and create a new DataFrame
data2 = data.fillna(value=0)
print(data2)
print(data2.isnull().sum().sum())

# Fill missing values using forward fill method
data3 = data.fillna(method='pad')
print(data3)

# Fill missing values using backward fill method
data4 = data.fillna(method='bfill')
print(data4)

# Drop a specific column, 'Observation', if it exists
if 'Observation' in data2.columns:
    data2.drop(['Observation'], axis=1, inplace=True)
print(data2.columns)

# Calculate the Interquartile Range (IQR) for outlier detection
Q1 = data2.quantile(0.25)
Q3 = data2.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

# Remove outliers based on the IQR method
data2 = data2[~((data2 < (Q1 - 1.5 * IQR)) | (data2 > (Q3 + 1.5 * IQR))).any(axis=1)]
print(data2)

# Get descriptive statistics of the cleaned DataFrame
print(data2.describe())