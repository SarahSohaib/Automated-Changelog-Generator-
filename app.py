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

# Ensure 'is_merge' column exists (safety)
if "is_merge" not in df.columns:
    df["is_merge"] = False

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

# Apply categorization
df["category"] = df["message"].apply(categorize)

# Override category for merge commits
df.loc[df["is_merge"], "category"] = "Merges"

# 🔹 Display merge metric
st.subheader("📊 Commit Statistics")

merge_count = int(df["is_merge"].sum())
st.metric("Merge Commits", merge_count)

# Pie chart
counts = df["category"].value_counts()

if counts.empty:
    st.warning("Not enough data to generate statistics.")
else:
    fig, ax = plt.subplots()
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%')
    ax.set_title("Commit Type Distribution")
    st.pyplot(fig)

# Live changelog
st.subheader("📜 Live Changelog")

changelog = generate_changelog(commits)
st.markdown(f"```markdown\n{changelog}\n```")

# Download PDF
st.subheader("📥 Download Changelog")

pdf_bytes = export_pdf(changelog)

st.download_button(
    label="Download Changelog as PDF",
    data=pdf_bytes,
    file_name="CHANGELOG.pdf",
    mime="application/pdf"
)