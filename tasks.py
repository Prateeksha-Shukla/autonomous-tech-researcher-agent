from crewai import Task
from agents import researcher, validator, analyst, writer


research_task = Task(
    description="Research the topic: {topic} using web search. Include latest trends and sources.",
    expected_output="Detailed research notes with sources and key facts.",
    agent=researcher
)

validation_task = Task(
    description="Validate the research and remove unreliable or weak information.",
    expected_output="Cleaned and verified research findings.",
    agent=validator
)

analysis_task = Task(
    description="Analyze findings and extract trends, industry impact, and future outlook.",
    expected_output="Analytical insights and trend summary.",
    agent=analyst
)

summary_task = Task(
    description="""
Write a structured report with:

Overview
Latest Developments
Key Companies
Industry Impact
Future Trends
Sources

Topic: {topic}
""",
    expected_output="Final structured technology report.",
    agent=writer,
    output_file="knowledge_repo/{topic}.txt"
)
