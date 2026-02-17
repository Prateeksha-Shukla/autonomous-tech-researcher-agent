from crewai import Crew
from tasks import research_task, validation_task, analysis_task, writing_task
from agents import researcher, validator, analyst, writer


def run_research_pipeline(topic):

    crew = Crew(
        agents=[researcher, validator, analyst, writer],
        tasks=[research_task, validation_task, analysis_task, writing_task],
        verbose=True
    )

    result = crew.kickoff(inputs={"topic": topic})

    # ✅ convert CrewOutput to string safely
    result_text = str(result)

    # save report
    with open("knowledge_repo/latest_report.txt", "w", encoding="utf-8") as f:
        f.write(result_text)

    return result_text


if __name__ == "__main__":
    topic = input("Enter technology topic: ")
    output = run_research_pipeline(topic)
    print("\n===== FINAL REPORT =====\n")
    print(output)
