import os
import subprocess
import pandas as pd
import streamlit as st

# Page setup
st.set_page_config(
    page_title="Automated Resume Screening Tool",
    layout="wide"
)

st.title("Automated Resume Screening Tool")

# Create folders automatically
os.makedirs("resumes", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# Job Description
job_description = st.text_area(
    "Enter Job Description",
    height=200,
    value="""
Python Developer required with:
- Python
- SQL
- Machine Learning
- FastAPI
- Pandas
- Data Analysis
"""
)

# Save JD automatically
with open("job_description.txt", "w", encoding="utf-8") as f:
    f.write(job_description)

# Upload resumes
uploaded_files = st.file_uploader(
    "Upload Resume Files",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

# Auto save uploaded files
if uploaded_files:

    for uploaded_file in uploaded_files:

        save_path = os.path.join(
            "resumes",
            uploaded_file.name
        )

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

    st.success("Resumes Uploaded Successfully")

# Run screening button
if st.button("Run ATS Screening"):

    try:

        result = subprocess.run(
            ["python", "main.py"],
            capture_output=True,
            text=True
        )

        st.success("Resume Screening Completed")

        st.text(result.stdout)

    except Exception as e:

        st.error(f"Execution Error: {e}")

# Show results automatically
csv_path = "outputs/ranking_report.csv"

if os.path.exists(csv_path):

    try:

        df = pd.read_csv(csv_path)

        if not df.empty:

            st.subheader("Resume Ranking Results")

            st.dataframe(
                df,
                use_container_width=True
            )

            shortlisted = df[
                df["Decision"] == "Shortlisted"
            ]

            rejected = df[
                df["Decision"] == "Rejected"
            ]

            st.subheader("Shortlisted Candidates")

            st.dataframe(
                shortlisted,
                use_container_width=True
            )

            st.subheader("Rejected Candidates")

            st.dataframe(
                rejected,
                use_container_width=True
            )

        else:

            st.warning("CSV file is empty.")

    except Exception as e:

        st.error(f"CSV Loading Error: {e}")

else:

    st.info("Upload resumes and click 'Run ATS Screening'")