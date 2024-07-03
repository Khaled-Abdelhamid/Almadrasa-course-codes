# %% [markdown]
# # Introduction to Pandas
# 
# <img src="https://raw.githubusercontent.com/fralfaro/DS-Cheat-Sheets/main/docs/examples/pandas/pandas.png" alt="numpy logo" width = "300">
# 
# [Pandas](https://pandas.pydata.org/) is built on NumPy and provides easy-to-use
# data structures and data analysis tools for the Python
# programming language.
# 
# ## Install and import Pandas
# 
# `
# $ pip install pandas
# `

# %%
# Import Pandas convention
import pandas as pd

# %% [markdown]
# ## Pandas Data Structures

# %% [markdown]
# ### Series
# 
# <img src="https://raw.githubusercontent.com/fralfaro/DS-Cheat-Sheets/main/docs/examples/pandas/serie.png" alt="numpy logo" >
# 
# A **one-dimensional** labeled array a capable of holding any data type.

# %%
# Import pandas
import pandas as pd

# Create a pandas Series representing monthly sales data
sales_data = pd.Series(
    [1500, 1200, 1800, 1600, 1300, 1700, 1400, 1500, 1600, 1800],
    index=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct']
)

# Print the pandas Series
print("Monthly Sales Data:")
print(sales_data)
print(type(sales_data))

# %% [markdown]
# ### DataFrame
# 
# <img src="https://raw.githubusercontent.com/fralfaro/DS-Cheat-Sheets/main/docs/examples/pandas/df.png" alt="numpy logo" >
# 
# **two-dimensional** labeled data structure with columns of potentially different types.

# %%
# Create a pandas DataFrame with more instances
data = {
    'country': ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Italy', 'Brazil', 'Canada'],
    'capital': ['Washington, D.C.', 'Beijing', 'Tokyo', 'Berlin', 'London', 'New Delhi', 'Paris', 'Rome', 'Brasília', 'Ottawa'],
    'population': [331449281, 1393000000, 126476461, 83783945, 67886011, 1303171035, 67186600, 60277900, 211050000, 37742154],
    'GDP': [21.44, 14.34, 5.07, 4.01, 2.99, 3.11, 2.78, 2.15, 1.77, 1.73]
}
df = pd.DataFrame(
    data,
    columns=['country', 'capital', 'population', 'GDP']
)

# Print the DataFrame 'df'
print("\ndf:")
df

# %%
import pandas as pd

# Original data structure
data_list_of_dicts = [
    {"country": "United States","capital": "Washington, D.C.","population": 331449281,"GDP": 21.44,},
    {"country": "China", "capital": "Beijing", "population": 1393000000, "GDP": 14.34},
    {"country": "Japan", "capital": "Tokyo", "population": 126476461, "GDP": 5.07},
    {"country": "Germany", "capital": "Berlin", "population": 83783945, "GDP": 4.01},
    {"country": "United Kingdom","capital": "London","population": 67886011,"GDP": 2.99},
    {"country": "India", "capital": "New Delhi", "population": 1303171035, "GDP": 3.11},
    {"country": "France", "capital": "Paris", "population": 67186600, "GDP": 2.78},
    {"country": "Italy", "capital": "Rome", "population": 60277900, "GDP": 2.15},
    {"country": "Brazil", "capital": "Brasília", "population": 211050000, "GDP": 1.77},
    {"country": "Canada", "capital": "Ottawa", "population": 37742154, "GDP": 1.73},
]

# Creating DataFrame from list of dictionaries
df = pd.DataFrame(
    data_list_of_dicts, columns=["country", "capital", "population", "GDP"]
)
df.sample()

# %% [markdown]
# # How to read Data

# %% [markdown]
# ## Read csv files

# %%
import pandas as pd

# %%
covid_df = pd.read_csv('./pandas_data/covid19-og.csv')
covid_df

# %%
# Load the first 10 rows of the AirBnb NYC 2019 dataset for quick inspection
nyc_df = pd.read_csv("./pandas_data/AirBnb_NYC_2019.csv", index_col=0)
nyc_df

# %%
# Load the dataset with multi-level indices and headers
warehouse_df = pd.read_csv(
    "./pandas_data/multi_index_warehouses.csv", index_col=[0, 1, 2], header=[0, 1]
)
warehouse_df

# %% [markdown]
# ## Read Excel files

# %%
pd.read_excel("./pandas_data/covid19.xlsx", sheet_name="gre")

# %% [markdown]
# ## Read JSON files

# %%
pd.read_json("./pandas_data/admits.json")

# %% [markdown]
# # Editing the DF

# %% [markdown]
# ## Renaming indices/columns

# %%
import pandas as pd

# Original data structure
data_list_of_dicts = [
    {"country": "United States","capital": "Washington, D.C.","population": 331449281,"GDP": 21.44},
    {"country": "China", "capital": "Beijing", "population": 1393000000, "GDP": 14.34},
    {"country": "Japan", "capital": "Tokyo", "population": 126476461, "GDP": 5.07},
    {"country": "Germany", "capital": "Berlin", "population": 83783945, "GDP": 4.01},
    {"country": "United Kingdom","capital": "London","population": 67886011,"GDP": 2.99},
    {"country": "India", "capital": "New Delhi", "population": 1303171035, "GDP": 3.11},
    {"country": "France", "capital": "Paris", "population": 67186600, "GDP": 2.78},
    {"country": "Italy", "capital": "Rome", "population": 60277900, "GDP": 2.15},
    {"country": "Brazil", "capital": "Brasília", "population": 211050000, "GDP": 1.77},
    {"country": "Canada", "capital": "Ottawa", "population": 37742154, "GDP": 1.73},
]

# Creating DataFrame from list of dictionaries
df = pd.DataFrame(
    data_list_of_dicts, columns=["country", "capital", "population", "GDP"]
)
df.head(10)

# %%
new_df = df.set_index("country")
new_df.rename({"united States": "us", "United Kingdom": "uk"}, axis=0,inplace=True)
new_df

# %%
df.rename({0: "zero"}, axis=0)

# %%
df.rename({"population": "population_number","GDP" : "gross_domestic_product"}, axis=1)

# %%
import pandas as pd

# Original data structure
data_list_of_dicts = [
    {"Country": "United States","Capital": "Washington, D.C.","Population Number": 331449281,"Gross Domestic Product": 21.44},
    {"Country": "China", "Capital": "Beijing", "Population Number": 1393000000, "Gross Domestic Product": 14.34},
    {"Country": "Japan", "Capital": "Tokyo", "Population Number": 126476461, "Gross Domestic Product": 5.07},
    {"Country": "Germany", "Capital": "Berlin", "Population Number": 83783945, "Gross Domestic Product": 4.01},
    {"Country": "United Kingdom","Capital": "London","Population Number": 67886011,"Gross Domestic Product": 2.99},
    {"Country": "India", "Capital": "New Delhi", "Population Number": 1303171035, "Gross Domestic Product": 3.11},
    {"Country": "France", "Capital": "Paris", "Population Number": 67186600, "Gross Domestic Product": 2.78},
    {"Country": "Italy", "Capital": "Rome", "Population Number": 60277900, "Gross Domestic Product": 2.15},
    {"Country": "Brazil", "Capital": "Brasília", "Population Number": 211050000, "Gross Domestic Product": 1.77},
    {"Country": "Canada", "Capital": "Ottawa", "Population Number": 37742154, "Gross Domestic Product": 1.73},
]

# Creating DataFrame from list of dictionaries
df = pd.DataFrame(
    data_list_of_dicts, columns=["Country", "Capital", "Population Number", "Gross Domestic Product"]
)
df.head(10)

# %%
df.columns = df.columns.str.lower().str.replace(" ","_")
df

# %%
df.columns = [col.lower().replace(" ", "_") for col in df.columns]
df

# %% [markdown]
# ## Getting Elements
# 

# %%
# Import pandas
import pandas as pd

# Create a pandas Series representing monthly sales data
sales_data = pd.Series(
    [1500, 1200, 1800, 1600, 1300, 1700, 1400, 1500, 1600, 1800],
    index=["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct"],
)
sales_data

# %%
# Get one element from a Series
sales_data["jan"]

# # another way to do it
# sales_data.jan

# %%
sales_data[["jan", "apr"]]

# %%
# Get subset of a DataFrame
sales_data[1:6:2]

# %%
sales_data[sales_data > 1500]

# %%
import pandas as pd

# Original data structure
data_list_of_dicts = [
    {
        "country": "United States",
        "capital": "Washington, D.C.",
        "population": 331449281,
        "GDP": 21.44,
    },
    {"country": "China", "capital": "Beijing", "population": 1393000000, "GDP": 14.34},
    {"country": "Japan", "capital": "Tokyo", "population": 126476461, "GDP": 5.07},
    {"country": "Germany", "capital": "Berlin", "population": 83783945, "GDP": 4.01},
    {
        "country": "United Kingdom",
        "capital": "London",
        "population": 67886011,
        "GDP": 2.99,
    },
    {"country": "India", "capital": "New Delhi", "population": 1303171035, "GDP": 3.11},
    {"country": "France", "capital": "Paris", "population": 67186600, "GDP": 2.78},
    {"country": "Italy", "capital": "Rome", "population": 60277900, "GDP": 2.15},
    {"country": "Brazil", "capital": "Brasília", "population": 211050000, "GDP": 1.77},
    {"country": "Canada", "capital": "Ottawa", "population": 37742154, "GDP": 1.73},
]

# Creating DataFrame from list of dictionaries
df = pd.DataFrame(
    data_list_of_dicts, columns=["country", "capital", "population", "GDP"]
)
df.head(10)

# %%
df[(df["GDP"] > 10) | (df["population"] > 331449281)]

# %% [markdown]
# ## Dropping
# 

# %%
# Import pandas
import pandas as pd

# Create a pandas Series representing monthly sales data
sales_data = pd.Series(
    [1500, 1200, 1800, 1600, 1300, 1700, 1400, 1500, 1600, 1800],
    index=["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct"],
)
sales_data

# %%
# Drop values from rows (axis=0)
sales_data.drop(['may', 'mar'])

# %%
import pandas as pd

# Original data structure
data_list_of_dicts = [
    {"country": "United States","capital": "Washington, D.C.","population": 331449281,"GDP": 21.44},
    {"country": "China", "capital": "Beijing", "population": 1393000000, "GDP": 14.34},
    {"country": "Japan", "capital": "Tokyo", "population": 126476461, "GDP": 5.07},
    {"country": "Germany", "capital": "Berlin", "population": 83783945, "GDP": 4.01},
    {"country": "United Kingdom","capital": "London","population": 67886011,"GDP": 2.99},
    {"country": "India", "capital": "New Delhi", "population": 1303171035, "GDP": 3.11},
    {"country": "France", "capital": "Paris", "population": 67186600, "GDP": 2.78},
    {"country": "Italy", "capital": "Rome", "population": 60277900, "GDP": 2.15},
    {"country": "Brazil", "capital": "Brasília", "population": 211050000, "GDP": 1.77},
    {"country": "Canada", "capital": "Ottawa", "population": 37742154, "GDP": 1.73},
]

# Creating DataFrame from list of dictionaries
df = pd.DataFrame(
    data_list_of_dicts, columns=["country", "capital", "population", "GDP"]
)
df.head(20)

# %%
df.drop_duplicates(subset=["country", "capital"],keep="last")

# %%
df.duplicated(subset=["country", "capital"]).sum()

# %%
import pandas as pd

# Assuming the original DataFrame creation code remains unchanged
data_list_of_dicts = [
    {"country": "United States","capital": "Washington, D.C.","population": 331449281,"GDP": 21.44},
    {"country": "China", "capital": "Beijing", "population": 1393000000, "GDP": 14.34},
    {"country": "Japan", "capital": "Tokyo", "population": 126476461, "GDP": 5.07},
    {"country": "Germany", "capital": "Berlin", "population": 83783945, "GDP": 4.01},
    {"country": "United Kingdom","capital": "London","population": 67886011,"GDP": 2.99},
    {"capital": "New Delhi", "population": 1303171035, "GDP": 3.11},
    {"country": "France", "capital": "Paris", "population": 67186600},
    {"country": "Italy", "capital": "Rome", "population": 60277900, "GDP": 2.15},
    {"country": "Brazil", "capital": "Brasília", "GDP": 1.77},
    {"country": "Canada", "capital": "Ottawa", "population": 37742154, "GDP": 1.73},
]

df = pd.DataFrame(
    data_list_of_dicts, columns=["country", "capital", "population", "GDP"]
)
df



# %%
na_counts = df.isna().sum()
print(na_counts)

# %%
# Dropping rows with any NaN values
df.dropna()

# %% [markdown]
# ## Applying Functions
# 

# %%
df

# %%
# Apply function to DataFrame
df.apply(lambda x: x/2)

# %%
df["country"] = df["country"].apply(lambda x: x.upper())
df["capital"] = df["capital"].apply(lambda x: x.lower())

df

# %% [markdown]
# ## TQDM with pandas

# %%
import time

def placeholder_function(x):
    time.sleep(0.5)
    return x.upper()




# %%
from tqdm import tqdm
# # Create new `pandas` methods which use `tqdm` progress
# # (can use tqdm_gui, optional kwargs, etc.)
tqdm.pandas()

df["country"] = df["country"].progress_apply(placeholder_function)

df

# %%
# Even better progress bar
from tqdm.auto import tqdm
# Create new `pandas` methods which use `tqdm` progress
# (can use tqdm_gui, optional kwargs, etc.)
tqdm.pandas()

df["country"] = df["country"].progress_apply(placeholder_function)

df

# %% [markdown]
# ## Basic Information
# 

# %%
import pandas as pd

# Original data structure
data_list_of_dicts = [
    {"country": "United States","capital": "Washington, D.C.","population": 331449281,"GDP": 21.44},
    {"country": "China", "capital": "Beijing", "population": 1393000000, "GDP": 14.34},
    {"country": "Japan", "capital": "Tokyo", "population": 126476461, "GDP": 5.07},
    {"country": "Germany", "capital": "Berlin", "population": 83783945, "GDP": 4.01},
    {"country": "United Kingdom","capital": "London","population": 67886011,"GDP": 2.99},
    {"country": "India", "capital": "New Delhi", "population": 1303171035, "GDP": 3.11},
    {"country": "France", "capital": "Paris", "population": 67186600, "GDP": 2.78},
    {"country": "Italy", "capital": "Rome", "population": 60277900, "GDP": 2.15},
    {"country": "Brazil", "capital": "Brasília", "population": 211050000, "GDP": 1.77},
    {"country": "Canada", "capital": "Ottawa", "population": 37742154, "GDP": 1.73},
]

# Creating DataFrame from list of dictionaries
df = pd.DataFrame(
    data_list_of_dicts, columns=["country", "capital", "population", "GDP"]
)
df.head(20)

# %%
df

# %%
# Get the shape (rows, columns)
df.shape

# %%
# df = df.set_index("country")
df = df.reset_index()

# %%
# Describe index
df.index

# %%
# Describe DataFrame columns
df.columns

# %%
# Info on DataFrame
df.info()

# %%
# Number of non-NA values
df.count()

# %%
df["country"].value_counts()

# %%
df["country"].hist(xrot=40)

# %% [markdown]
# ## Summary

# %%
# Sum of values
df['population'].sum()

# # Cumulative sum of values
df['population'].cumsum()

# # Minimum/maximum values
df['population'].min()
df['population'].max()

# # Index of minimum/maximum values
df['population'].idxmin()
df['population'].idxmax()


# # Mean of values
df['population'].mean()

# # Median of values
df['population'].median()

# # Summary statistics
df['population'].describe()

# %%
# easier way to get the summaries
# df.describe()
df.describe().T

# %% [markdown]
# ## Introduction to data profiling

# %%
from ydata_profiling import ProfileReport
profile = ProfileReport(df, title="Profiling Report",explorative=True)
# profile.to_widgets()
# profile.to_notebook_iframe()
profile.to_file("your_report.html")

# %% [markdown]
# ## Pivot Table
# 
# Pivot tables allow you to transform and summarize data, similar to the pivot table feature in Excel. 

# %%
# Create a DataFrame with some sales data
data = {
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02', '2023-01-03'],
    'city': ['New York', 'New York', 'New York', 'Los Angeles', 'Los Angeles', 'Los Angeles'],
    'sales': [100, 150, 200, 50, 60, 70]
}
sales_df = pd.DataFrame(data)
sales_df

# %%
# Pivot the data to show sales for each city by date
pivot_df = sales_df.pivot(index='date', columns='city', values='sales')
pivot_df

# %% [markdown]
# ## GroupBy
# 
# Grouping data in pandas can help you to aggregate and summarize your data in powerful ways.

# %%
# Group by city and calculate the total sales for each city
grouped_sales_df = sales_df.groupby('city').sum()
grouped_sales_df

# %%
# Group by city and get descriptive statistics for sales
grouped_sales_stats = sales_df.groupby('city').describe()
grouped_sales_stats

# %% [markdown]
# ## Aggregate (agg)
# 
# The `agg` method allows you to apply multiple aggregation functions to your grouped data.

# %%
# Group by city and apply multiple aggregation functions
aggregated_sales_df = sales_df.groupby('city').agg({
    'sales': ['sum', 'mean', 'max', 'min']
})
aggregated_sales_df

# %%
# Group by city and apply custom aggregation functions
custom_agg_sales_df = sales_df.groupby('city').agg({
    'sales': lambda x: x.max() - x.min()  # Range of sales
})
custom_agg_sales_df

This addition to the tutorial demonstrates how to use `pivot`, `groupby`, and `agg` methods to manipulate and analyze data in pandas effectively.