import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.git_parser import get_commits
from src.changelog_generator import generate_changelog
from pdf_export import export_pdf

st.set_page_config(page_title="Automated Changelog Generator", layout="wide")

st.title("📜 Automated Changelog Dashboard")

repo_path = "."

commits = get_commits(repo_path)

if not commits:
    st.warning("No commits found.")
    st.stop()

# Convert commits to dataframe
df = pd.DataFrame(commits)

# Categorization logic
def categorize(message):
    message = message.lower()
    if message.startswith("feat"):
        return "Features"
    elif message.startswith("fix"):
        return "Bug Fixes"
    elif message.startswith("docs"):
        return "Documentation"
    elif message.startswith("refactor"):
        return "Refactoring"
    elif message.startswith("chore"):
        return "Maintenance"
    else:
        return "Other"

df["category"] = df["message"].apply(categorize)

st.subheader("📊 Commit Statistics")

counts = df["category"].value_counts()

fig, ax = plt.subplots()
ax.pie(counts, labels=counts.index, autopct='%1.1f%%')
ax.set_title("Commit Type Distribution")

st.pyplot(fig)

st.subheader("📜 Live Changelog")

changelog = generate_changelog(commits)
st.markdown(f"```markdown\n{changelog}\n```")

st.subheader("📥 Download Changelog")

pdf_bytes = export_pdf(changelog)

st.download_button(
    label="Download Changelog as PDF",
    data=pdf_bytes,
    file_name="CHANGELOG.pdf",
    mime="application/pdf"
)