# question_engine.py
import random

questions_bank = {
    "Python": {
        "Easy": ["What is a list in Python?", "How do you create a function in Python?"],
        "Medium": ["Explain Python decorators.", "What is the difference between list and tuple?"],
        "Hard": ["Explain GIL in Python.", "How do you manage memory in Python?"]
    },
    "SQL": {
        "Easy": ["What is SQL?", "What is a primary key?"],
        "Medium": ["Explain JOINs in SQL.", "What is normalization?"],
        "Hard": ["How would you optimize a slow SQL query?", "Explain window functions."]
    },
    "Java": {
        "Easy": ["What is a class in Java?", "Explain Java data types."],
        "Medium": ["Explain inheritance in Java.", "What is an interface?"],
        "Hard": ["Explain Java memory management.", "What is the difference between abstract class and interface?"]
    }
}

def generate_question(skill, difficulty="Easy"):
    """
    Returns one question at a time based on skill and difficulty.
    """
    if skill in questions_bank:
        if difficulty in questions_bank[skill]:
            return random.choice(questions_bank[skill][difficulty])
    return "No question available for this skill."

# Example usage
if __name__ == "__main__":
    print(generate_question("Python", "Medium"))
