from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("computingvictor/transactions-fraud-datasets")

# Load environment variables
load_dotenv()
# def connnect_to_db():
    
#     )
#     return create_engine(db_url)


db_url = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")

engine = create_engine(db_url,connect_args={'connect_timeout': 60})

df = pd.read_csv(path+'/transactions_data.csv', header =0)

column_mapping = { 'use_chip': 'transaction_mode',
    'errors': 'error'
}

df = df.rename(columns=column_mapping)
df['amount'] = df['amount'].str.replace('$', '', regex=False).str.replace(',', '').astype(float)

failed_rows = [] 

#####> Batch input(Faster but stops at error) [Good for Big dataset]
df.to_sql('transaction', con=engine, if_exists='append', index=False, chunksize=1000)

#####> Row wise input(slower but will give you failed_df) [Good for small dataset]
# for index, row in df.iterrows():
#     try:
#         # Insert row into MySQL
#         row_df = pd.DataFrame([row])  # Convert single row to DataFrame
#         row_df.to_sql('transaction', con=engine, if_exists='append', index=False)
#     except Exception as e:
#         # If there's an error, log the failed row and continue
#         failed_rows.append(row)
#         #print(f"Error inserting row {index}: {e}")

failed_rows_df = pd.DataFrame(failed_rows)
failed_rows_df.to_csv('failed_rows.csv', index=False)

print("Data successfully imported!")
print(f"Failed rows saved to 'failed_rows.csv'.")