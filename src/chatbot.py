import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv() # loads all the environment variables 
groq_api_key  = os.getenv("GROQ_API_KEY")
model = ChatGroq(model= "llama-3.1-8b-instant",groq_api_key = groq_api_key)
store = {}

def get_sessionhistory(session_id:str)-> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

with_messagee_history = RunnableWithMessageHistory(model,get_sessionhistory)

config = {"configurable" : {"session_id": "chat1"}}

SYSTEM_PROMPT = """Youare a helpful Financial analysis agent 
                    suggest me some of the good ways to save mone instead of
                    speding them on Unnecessary things """


context = input("Enter the query :- ")
# response  = model.invoke(
#     [
#         HumanMessage(content = context),
#         AIMessage(content  =SYSTEM_PROMPT)
#     ]
#     )
## Message Hisstory 
response  = with_messagee_history.invoke(
   [
        HumanMessage(content = context),  
    ]
    ,
    config = config

)

print(f"AI Response = {response.content}")