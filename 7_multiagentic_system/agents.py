import os
from langchain_openai import ChatOpenAI

# GitHub model configuration
token = os.environ.get("GITHUB_TOKEN")
endpoint = "https://models.github.ai/inference"
model_name = "openai/gpt-4o-mini"

# Use ChatOpenAI with GitHub model endpoint
model = ChatOpenAI(
    model=model_name,
    temperature=0,
    openai_api_key=token,
    openai_api_base=endpoint,
)

#custom imports 
from tools import add, multiply , subtract , divide , search_tavily

# Using the correct import for langchain
from langgraph.prebuilt import create_react_agent


#custom imports 
math_agent = create_react_agent(
    model=model,
    tools=[add, multiply, subtract, divide],
    name="math_expert",
    prompt="You are a math expert. Always use one tool at a time."
)

research_agent = create_react_agent(
    model=model,
    tools=[search_tavily],
    name="research_expert",
    prompt="You are a world class researcher with access to web search. Do not do any math."
)
