from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import TavilySearchResults
from langchain_community.tools.file_management import (
    CopyFileTool, DeleteFileTool, FileSearchTool, ListDirectoryTool,
    MoveFileTool, ReadFileTool, WriteFileTool
)

def search_duckduckgo(query: str):
    """Searches DuckDuckGo using LangChain's DuckDuckGoSearchRun tool."""
    search = DuckDuckGoSearchRun()
    return search.invoke(query)

def search_tavily(query: str):
    """Searches Tavily using LangChain's TavilySearchResults tool."""
    search = TavilySearchResults()
    return search.invoke(query)

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b

def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    return a / b

# Load all file management tools dynamically
_file_management_classes = [
    CopyFileTool, DeleteFileTool, FileSearchTool, ListDirectoryTool,
    MoveFileTool, ReadFileTool, WriteFileTool
]

file_management_tools = [tool_class() for tool_class in _file_management_classes]
file_management_tools_dict = {
    tool.name.replace(" ", "_").lower(): tool 
    for tool in file_management_tools
}

