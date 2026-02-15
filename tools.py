from dotenv import load_dotenv
load_dotenv()   # ✅ ensure .env is loaded BEFORE Tavily initializes

from langchain_tavily import TavilySearch

search_tool = TavilySearch(max_results=5)
