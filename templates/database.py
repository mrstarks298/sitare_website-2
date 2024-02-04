import pandas as pd
import pymysql
from sqlalchemy import create_engine

# Create a SQLAlchemy engine
engine = sqlalchemy.create_engine(
    "mysql+pymysql://Sitareemployee123_carriedmet:@mki.h4887b0f58e95516fa09edff1f15469ab1dbff887.filess.io:3306/Sitareemployee123_carriedmet"
)

# Execute a query and fetch the result into a Pandas DataFrame
df = pd.read_sql_query("SELECT * FROM  employee", con=engine)

# Print the DataFrame
print(df)




