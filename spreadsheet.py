import pandas as pd

# sample data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 35, 42, 29],
    'City': ['San Francisco', 'Paris', 'London', 'Post Falls']
}

# create pandas dataframe
df = pd.DataFrame(data)

# define file path
file_path = 'example.csv'

# write data to excel
df.to_csv(file_path, header=True, index=False)

# notify the user
print('CSV file has been saved to {}'.format(file_path))
