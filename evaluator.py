# evaluator.py
def evaluate_answer(question, answer, response_time):
    """
    Evaluate answer based on:
    - correctness (keyword match)
    - clarity (length/format)
    - response time
    Returns score (0-10) and feedback
    """
    score = 0
    feedback = []

    # Simple correctness check
    keywords = [word for word in question.split() if len(word) > 3]
    match_count = sum([1 for kw in keywords if kw.lower() in answer.lower()])
    
    score += min(match_count, 5)  # max 5 points

    # Clarity
    if len(answer.split()) > 3:
        score += 2
    else:
        feedback.append("Answer too short, needs more detail.")

    # Time usage
    if response_time < 30:
        score += 3
    else:
        feedback.append("Too slow, try to answer quicker.")

    score = min(score, 10)
    if score >= 7:
        feedback.append("Good answer!")
    elif score >= 4:
        feedback.append("Average answer, can improve.")
    else:
        feedback.append("Poor answer, needs improvement.")

    return score, " ".join(feedback)

# Example usage
if __name__ == "__main__":
    q = "What is a list in Python?"
    ans = "A list is a collection that can hold multiple items."
    score, fb = evaluate_answer(q, ans, 20)
    print("Score:", score)
    print("Feedback:", fb)
