import pandas as pd

# Read all three CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine all files into one dataframe
df = pd.concat([df1, df2, df3], ignore_index=True)

# Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Remove the '$' sign from price and convert to float
df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

# Calculate sales
df["sales"] = df["quantity"] * df["price"]

# Keep only required columns
output = df[["sales", "date", "region"]]

# Rename columns
output.columns = ["Sales", "Date", "Region"]

# Save the output
output.to_csv("formatted_sales_data.csv", index=False)

print("Formatted file created successfully!")