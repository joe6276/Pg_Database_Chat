
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

KEY ="KEY"
# postgresql+psycopg2://postgres:root@localhost:5432/Skol
# pip install -r requirement.txt
#connect to DB
# If your password has an '@' sign it will throw an error
database=SQLDatabase.from_uri("postgresql+psycopg2://postgres:root@localhost:5432/Skol")
# cro LLM fro Parsing queries and results
llm=ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=KEY)
#Toolkit for interacting with SQL databases.
toolkit = SQLDatabaseToolkit(db=database, llm=llm)

#create an Angent

agent_executor=create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    prefix="You are an agent designed to interact with a SQL database. Do not execute any delete or drop  statement to the database instead say its not allowed"
)
# agent_executor("Tell the names of trainees that have graduated, are not working , have great technical skills and great soft skills ")
# agent_executor("Tell the names of  3 trainees are yet to graduate and they have great technicalskilla nd soft skills ")
# agent_executor("Add a guy named Joseph , he has graduated, he is not working and his technicalskills and softskills are a 10 ")
# agent_executor("Add  Jane , he has graduated, he is not working and his technicalskills and softskills are high ")
agent_executor(" Delete Everything ")
# agent_executor(" Take all uncompleted tasks and assign to  some trainees")
