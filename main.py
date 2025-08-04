import pandas as pd
df = pd.read_csv("marketing_campaign.csv", sep='\t')  # Use sep=',' if it's comma-separated
df.isnull().sum()  # See which columns have missing values
df = df.drop_duplicates()
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y')  # or detect format automatically
df.columns = df.columns.str.lower().str.replace(' ', '_')
df.dtypes  # Inspect current types
df.to_csv("cleaned_marketing_campaign.csv", index=False)

