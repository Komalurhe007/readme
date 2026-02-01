# job_analysis.py
import re

def extract_skills(text):
    """
    Extract skills from a given text using simple keyword matching.
    You can expand this list with more keywords.
    """
    skills_keywords = ["Python", "Java", "C++", "SQL", "DBMS", "Machine Learning", "Data Analysis", "JavaScript", "HTML", "CSS"]
    found_skills = []

    for skill in skills_keywords:
        if re.search(rf"\b{skill}\b", text, re.IGNORECASE):
            found_skills.append(skill)
    return found_skills

def calculate_relevance(resume_skills, job_skills):
    """
    Compare resume skills with job description skills.
    Returns a relevance score from 0 to 100.
    """
    if not job_skills:
        return 0

    matched = [skill for skill in resume_skills if skill in job_skills]
    score = int((len(matched) / len(job_skills)) * 100)
    return score

# Example usage
if __name__ == "__main__":
    resume_text = "I know Python, SQL, Java and DBMS."
    job_desc = "Looking for a candidate with Python, Java, SQL and Machine Learning skills."
    
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)
    relevance_score = calculate_relevance(resume_skills, job_skills)

    print("Resume Skills:", resume_skills)
    print("Job Skills:", job_skills)
    print("Relevance Score:", relevance_score)
