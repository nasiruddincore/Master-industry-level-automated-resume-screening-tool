import os
import pandas as pd

from src.extractor import extract_text
from src.cleaner import clean_text
from src.matcher import calculate_similarity

# Auto create folders
os.makedirs("resumes", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

JOB_DESCRIPTION = """
Python Developer required with skills in:
Python
SQL
Machine Learning
FastAPI
Pandas
Data Analysis
"""

job_description = clean_text(JOB_DESCRIPTION)

results = []

resume_folder = "resumes"

resume_files = os.listdir(resume_folder)

valid_files = [
    file for file in resume_files
    if file.endswith(".pdf") or file.endswith(".docx")
]

if len(valid_files) == 0:

    print("\nNo resumes found inside resumes folder.\n")

else:

    for resume_file in valid_files:

        file_path = os.path.join(
            resume_folder,
            resume_file
        )

        print(f"Processing: {resume_file}")

        resume_text = extract_text(file_path)

        if resume_text.strip() == "":
            continue

        cleaned_resume = clean_text(resume_text)

        score = calculate_similarity(
            job_description,
            cleaned_resume
        )

        decision = (
            "Shortlisted"
            if score >= 50
            else "Rejected"
        )

        results.append({
            "Resume": resume_file,
            "Score": score,
            "Decision": decision
        })

    if len(results) > 0:

        df = pd.DataFrame(results)

        df = df.sort_values(
            by="Score",
            ascending=False
        )

        output_file = "outputs/ranking_report.csv"

        df.to_csv(
            output_file,
            index=False
        )

        print("\nResume Screening Completed\n")

        print(df)

    else:

        print("\nNo valid resume data extracted.\n")