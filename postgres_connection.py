from os import getcwd, environ
from dotenv import load_dotenv 
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.engine import URL

from sqlalchemy import create_engine

import load_env_vars

host = environ.get('DB_HOST')

user = environ.get('DB_USER')
password = environ.get('DB_PASSWORD')
port = environ.get('DB_PORT')
database = environ.get('DB_NAME')

# connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'
connection_string = URL.create(
    drivername="postgresql+psycopg",
    username=user,
    password=password,
    host=host,
    port=port,
    database=database
)
try:
    engine = create_engine(connection_string)

    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

        if result.scalar() == 1:
            print("PostgreSQL connection successful!")

except SQLAlchemyError as e:
    print(f"PostgreSQL connection failed: {e}")

engine = create_engine(connection_string)

db_object = SQLDatabase(engine = engine )