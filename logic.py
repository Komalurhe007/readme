# logic.py

def update_difficulty(last_score, current_difficulty, scores_history):
    """
    Adaptive logic:
    - score >=7 → increase difficulty
    - score <=4 → decrease difficulty
    - average <3 after 3 questions → end interview early
    """
    difficulties = ["Easy", "Medium", "Hard"]
    idx = difficulties.index(current_difficulty)

    # Update difficulty
    if last_score >= 7 and idx < 2:
        idx += 1
    elif last_score <= 4 and idx > 0:
        idx -= 1

    # Check if interview should end
    end_interview = False
    if len(scores_history) >= 3 and sum(scores_history[-3:])/3 < 3:
        end_interview = True

    return difficulties[idx], end_interview

# Example usage
if __name__ == "__main__":
    new_diff, end = update_difficulty(2, "Medium", [3,2,1])
    print("New Difficulty:", new_diff)
    print("End Interview?", end)
