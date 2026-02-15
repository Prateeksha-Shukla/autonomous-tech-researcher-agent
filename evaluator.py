def evaluate_quality(text):
    score = 0
    if len(text) > 800:
        score += 5
    if "Sources" in text:
        score += 5
    if "Future" in text:
        score += 5
    return score
