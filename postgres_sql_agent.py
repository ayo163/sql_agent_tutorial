from langchain_openai import ChatOpenAI
from os import environ
import load_env_vars
from agent_toolkit import tools
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

api_key = environ.get('OPENAI_API_KEY', '')



#MODEL
model = ChatOpenAI(model = 'gpt-4o-mini', api_key = api_key)


agent = create_agent(model =model, tools = tools)



question = "give me the list of account holders"

#1. list total debit of each account holder
# 2. Total credit and total debit between '2026-11-01' AND '2026-11-06';
# 3. Maximum credit added by customer in descending order 


for step in agent.stream(
    {"messages": [{"role": "user", "content": question}]},
    stream_mode = "values"
): step['messages'][-1].pretty_print()