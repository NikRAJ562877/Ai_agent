# agent_core.py
import os
from dotenv import load_dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import Tool
from langchain.agents import create_agent

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_API_KEY)
search = GoogleSerperAPIWrapper(serper_api_key=SERPER_API_KEY)

tools = [
    Tool(
        name="Intermediate_Answer",
        func=search.run,
        description="Useful for answering questions using live web search",
    ),
]

agent = create_agent(llm, tools)
