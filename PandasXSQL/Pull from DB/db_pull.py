from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()
# def connnect_to_db():
    
#     )
#     return create_engine(db_url)


db_url = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")

engine = create_engine(db_url,connect_args={'connect_timeout': 60})

query = "SELECT * FROM transaction"
df = pd.read_sql(query, engine)

print(df.head())

df.to_csv('transactions_from_db.csv', index=False)

print(f"Data successfully exported in 'transactions_from_db.csv'!")
print(f"Failed rows saved to 'failed_rows.csv'.")