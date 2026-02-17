from crewai import Task
from agents import researcher, validator, analyst, writer


research_task = Task(
    description="Research the topic: {topic} using web search and gather latest technology insights with sources.",
    expected_output="Raw research findings with key facts and references",
    agent=researcher
)

validation_task = Task(
    description="Validate and clean the research findings. Remove weak or duplicate info.",
    expected_output="Validated and reliable research points",
    agent=validator
)

analysis_task = Task(
    description="Analyze validated findings and extract trends, impacts, and industry relevance.",
    expected_output="Analytical insights and trend summary",
    agent=analyst
)

writing_task = Task(
    description="Write a structured professional technology report with sections and summary.",
    expected_output="Final structured technology report",
    agent=writer
)
