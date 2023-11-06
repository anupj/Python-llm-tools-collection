# This example shows how to query a sqlite database

from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

db = SQLDatabase.from_uri("sqlite:///chinook.db")
llm = OpenAI(temperature=0)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# Now run queries against the database
db_chain.run("How many employees are there?")
db_chain.run("What is the name of the first employee")
db_chain.run("Which customer has the most invoices")
db_chain.run("List all music genres in the database")
db_chain.run("List all the tables in this database")
