from crewai import Agent
from tools import search_tool

MODEL = "groq/llama-3.1-8b-instant"

researcher = Agent(
    role="Technology Research Specialist",
    goal="Search and gather latest technology information",
    backstory="Expert at finding accurate tech info from the web",
    tools=[search_tool],
    llm=MODEL,
    max_iter=2,
    max_retry_limit=1,
    verbose=True
)

validator = Agent(
    role="Fact Validator",
    goal="Validate and clean research findings",
    backstory="Removes unreliable info",
    llm=MODEL,
    max_iter=2,
    max_retry_limit=1,
    verbose=True
)

analyst = Agent(
    role="Technology Analyst",
    goal="Analyze trends and impacts",
    backstory="Understands industry trends",
    llm=MODEL,
    max_iter=2,
    max_retry_limit=1,
    verbose=True
)

writer = Agent(
    role="Technical Report Writer",
    goal="Write structured technology reports",
    backstory="Creates professional summaries",
    llm=MODEL,
    max_iter=2,
    max_retry_limit=1,
    verbose=True
)
