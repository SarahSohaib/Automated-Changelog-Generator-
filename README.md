# Automated Changelog Generator

**Student Name:** Sarah Sohaib
**Registration No:** 23FE10CSE00673
**Course:** CSE3253 DevOps [PE6]
**Semester:** VI (2025–2026)
**Project Type:** Git & Agile
**Difficulty:** Intermediate

---

# Project Overview

## Problem Statement

Software projects require changelogs to track updates, bug fixes, and new features across versions. However, maintaining changelogs manually is time-consuming and often ignored by developers.

This project automates changelog generation by extracting commit history from a Git repository and converting it into a structured Markdown changelog file.

---

# Objectives

* Automatically extract commit history from Git repositories
* Categorize commits using conventional commit prefixes
* Generate a structured Markdown changelog file automatically

---

# Key Features

* Automatic Git commit parsing
* Commit categorization (`feat`, `fix`, `docs`, `chore`, `refactor`)
* Markdown changelog generation
* Lightweight command-line interface
* No external dependencies required

---

# Technology Stack

## Core Technologies

Programming Language: **Python 3**
Framework: **None (CLI Tool)**
Database: **None**

## DevOps Tools

Version Control: **Git**
CI/CD: **GitHub Actions (optional)**

---

# Getting Started

## Prerequisites

* Python 3.8+
* Git installed
* A Git repository with commits

---

## Installation

Clone the repository:

```bash
git clone https://github.com/SarahSohaib/Automated-Changelog-Generator-.git
cd Automated-Changelog-Generator-
```

---

## Run the Generator

Generate a changelog from the repository:

```bash
python src/main.py --repo . --output output/CHANGELOG.md
```

This will analyze the commit history and generate a changelog file.

---

# Project Structure

```
Automated-Changelog-Generator
│
├── src
│   ├── main.py
│   ├── git_parser.py
│   └── changelog_generator.py
│
├── output
│   └── CHANGELOG.md
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

# How It Works

Pipeline:

```
Git Repository
      │
      ▼
Git Log Extraction
      │
      ▼
Commit Parsing
      │
      ▼
Commit Categorization
      │
      ▼
Markdown Changelog Generation
      │
      ▼
CHANGELOG.md Output
```

1. The program extracts commit history using `git log`.
2. Commit messages are parsed and categorized.
3. Categories include Features, Bug Fixes, Documentation, Maintenance, and Others.
4. The commits are formatted into a Markdown changelog.
5. The final file is saved as `CHANGELOG.md`.

---

# Commit Convention

The tool recognizes the following commit prefixes:

| Prefix   | Category         |
| -------- | ---------------- |
| feat     | New feature      |
| fix      | Bug fix          |
| docs     | Documentation    |
| refactor | Code improvement |
| chore    | Maintenance      |

Example commits:

```
feat: add commit categorization logic
fix: handle git log parsing edge cases
docs: update README documentation
```

---

# Example Generated Output

```
# Changelog

## Features
- feat: implement git parser and changelog generator

## Maintenance
- chore: add initial project structure

## Other
- Initial commit
```

---

# Project Challenges

* Parsing Git commit history programmatically
* Categorizing commits reliably using message prefixes
* Generating structured Markdown output

---

# Learnings

* Working with Git commit history programmatically
* Building CLI tools using Python
* Applying DevOps practices to automate documentation

---

# License

This project is licensed under the MIT License.

---

# Contact

Student: **Sarah Sohaib**
Registration No: **23FE10CSE00673**
GitHub: https://github.com/SarahSohaib
