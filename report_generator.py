# report_generator.py

def generate_report(scores, resume_skills, job_skills):
    """
    Generates a final interview report
    """
    final_score = int(sum(scores)/len(scores)*10)  # convert avg to 0-100
    strengths = [skill for skill in resume_skills if skill in job_skills]
    weaknesses = [skill for skill in job_skills if skill not in resume_skills]

    if final_score >= 75:
        category = "Strong"
    elif final_score >= 50:
        category = "Average"
    else:
        category = "Needs Improvement"

    report = f"""
    FINAL INTERVIEW REPORT
    ----------------------
    Final Score: {final_score}/100
    Strengths: {', '.join(strengths) if strengths else 'None'}
    Weaknesses: {', '.join(weaknesses) if weaknesses else 'None'}
    Skill-wise Performance: {scores}
    Interview Readiness: {category}
    """
    return report

# Example usage
if __name__ == "__main__":
    report = generate_report([7,8,6], ["Python","SQL"], ["Python","SQL","Java"])
    print(report)
