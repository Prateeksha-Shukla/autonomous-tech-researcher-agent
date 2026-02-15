import os

def save_memory(topic, content):
    os.makedirs("knowledge_repo", exist_ok=True)
    with open(f"knowledge_repo/{topic}.txt", "w", encoding="utf-8") as f:
        f.write(content)
