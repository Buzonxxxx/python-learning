# Importing the pandas library which provides data structures and data analysis tools.
import pandas as pd

# Reading a CSV file containing FIFA19 player data into a DataFrame.
data_frame = pd.read_csv('FIFA19_official_data.csv')

# Printing the shape (number of rows, number of columns) of the data.
print(data_frame.shape)

# Printing the statistical summary of the DataFrame's columns.
print(data_frame.describe())

# Printing the underlying data of the DataFrame in an array format.
print(data_frame.values)

# Filtering and printing players who are older than 40 years.
print(data_frame[data_frame["Age"] > 40])

# Defining a function to convert string values with 'K', 'M', or 'B' suffixes to their respective float values.
# For instance, "1.5K" becomes 1500.0, "2M" becomes 2000000.0, etc.
def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0

# Creating a new DataFrame with columns "Name", "Wage", and "Value" from the original data.
df1 = pd.DataFrame(data_frame, columns=["Name", "Wage", "Value"])

# Cleaning the 'Wage' and 'Value' columns to remove the '€' symbol and converting the cleaned values using the value_to_float function.
wage = df1['Wage'].replace('[\€]', '', regex=True).apply(value_to_float)
value = df1['Value'].replace('[\€]', '', regex=True).apply(value_to_float)

# Updating the 'Wage' and 'Value' columns in df1 with the cleaned and converted values.
df1["Value"] = value
df1["Wage"] = wage

# Calculating the difference between 'Value' and 'Wage' for each player and storing it in a new column 'difference'.
df1["difference"] = df1["Value"] - df1["Wage"]

# Sorting the DataFrame based on the 'difference' column in descending order and printing it.
print(df1.sort_values('difference', ascending=False))
