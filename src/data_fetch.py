import pandas as pd

df = pd.read_csv('../data/NVDA_5_years.csv', usecols=['Close/Last', 'Open', 'High', 'Low'])

monetary_columns = [col for col in df.columns if isinstance(df[col][0], str) and '$' in df[col][0]]

# Convert each identified column from string to float, removing the dollar sign and commas
for col in monetary_columns:
    df[col] = df[col].replace({'\$': '', ',': ''}, regex=True).astype(float)
    
df.to_csv('../data/NVDA_processed.csv', index=False)

# Display the modified DataFrame to confirm the conversion
print(df.head(10))

df2 = pd.read_csv("../data/NVDA_processed.csv")

print(df2.head(10))