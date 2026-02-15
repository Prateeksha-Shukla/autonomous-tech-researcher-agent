import config  # loads .env first

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from tools import search_tool
from agents import researcher_prompt, validator_prompt, analyst_prompt, writer_prompt
from memory import save_memory
from evaluator import evaluate_quality


llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0.2
)

parser = StrOutputParser()


def run_step(prompt_text, **kwargs):
    prompt = PromptTemplate.from_template(prompt_text)
    chain = prompt | llm | parser
    return chain.invoke(kwargs)


def main():
    topic = input("Enter technology topic: ")

    print("\n🔎 Searching web...")
    search_results = search_tool.run(topic)

    print("\n🤖 Researcher running...")
    research_notes = run_step(researcher_prompt, topic=topic + "\n" + str(search_results))

    print("\n✅ Validator running...")
    validated = run_step(validator_prompt, input=research_notes)

    print("\n📊 Analyst running...")
    analysis = run_step(analyst_prompt, input=validated)

    print("\n✍️ Writer running...")
    report = run_step(writer_prompt, input=analysis)

    print("\n===== FINAL REPORT =====\n")
    print(report)

    save_memory(topic, report)

    score = evaluate_quality(report)
    print(f"\nQuality Score: {score}/15")


if __name__ == "__main__":
    main()
