from langchain_community.agent_toolkits import SQLDatabaseToolkit
from os import environ
from postgres_connection import db_object 
from langchain_openai import ChatOpenAI
import load_env_vars

model = ChatOpenAI
#API key
api_key = environ.get('OPENAI_API_KEY', '')

#MODEL
model = ChatOpenAI(model = 'gpt-4o-mini', api_key = api_key)
#Object
toolkit = SQLDatabaseToolkit(db = db_object, llm = model)

#view the different tools
#tools are resources that models use to perform specific tasks

tools = toolkit.get_tools()
#this displays all the stages how sql query was formed, tables considered
#before results are generated 
# for tool in tools:
#     print(f"{tool.name}: {tool.description}\n")
