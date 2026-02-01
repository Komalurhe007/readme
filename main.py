# main.py
import time
from job_analysis import extract_skills, calculate_relevance
from question_engine import generate_question
from evaluator import evaluate_answer
from logic import update_difficulty
from report_generator import generate_report

# Sample input
resume_text = input("Enter your resume text: ")
job_desc = input("Enter job description text: ")

resume_skills = extract_skills(resume_text)
job_skills = extract_skills(job_desc)
relevance_score = calculate_relevance(resume_skills, job_skills)

print(f"\nRelevance Score with Job: {relevance_score}/100\n")
print("Identified Resume Skills:", resume_skills)
print("Job Skills:", job_skills)
print("\nStarting Mock Interview...\n")

difficulty = "Easy"
scores_history = []

for i in range(5):
    # pick a random skill
    if resume_skills:
        skill = resume_skills[i % len(resume_skills)]
    else:
        skill = job_skills[i % len(job_skills)]

    question = generate_question(skill, difficulty)
    print(f"Q{i+1} [{difficulty} | Skill: {skill}]: {question}")

    start_time = time.time()
    answer = input("Your Answer: ")
    response_time = time.time() - start_time

    score, feedback = evaluate_answer(question, answer, response_time)
    print(f"Score: {score}/10 | Feedback: {feedback}\n")

    scores_history.append(score)
    difficulty, end = update_difficulty(score, difficulty, scores_history)
    if end:
        print("Interview ended early due to low performance.\n")
        break

report = generate_report(scores_history, resume_skills, job_skills)
print(report)
