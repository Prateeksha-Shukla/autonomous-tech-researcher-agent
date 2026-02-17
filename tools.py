from dotenv import load_dotenv
load_dotenv()

from crewai.tools import tool
from langchain_tavily import TavilySearch

# ✅ reduce results to lower token usage
tavily = TavilySearch(max_results=3)

@tool("Web Technology Search")
def search_tool(query: str) -> str:
    """Search latest technology information from the web"""
    results = tavily.run(query)
    return str(results)[:4000]   # ✅ trim long outputs to control tokens
