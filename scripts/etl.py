import pandas as pd
from sqlalchemy import create_engine

# 1. Read CSV
df = pd.read_csv("data/raw/barista_coffee_sales_data_for_eda.csv")

# 2. Quick check
print("Dataset shape:", df.shape)
print("Columns:", df.columns)

# 3. Create SQLite connection
engine = create_engine("sqlite:///data/coffee_sales.db")

# 4. Load data into SQL (replace if exists)
df.to_sql("coffee_sales", con=engine, if_exists="replace", index=False)

print("Data loaded into 'coffee_sales' table in coffee_sales.db")
