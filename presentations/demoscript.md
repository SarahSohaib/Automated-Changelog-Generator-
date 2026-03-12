# Demo Script

1. Introduce the project
2. Explain the problem of manual changelog maintenance
3. Show the repository structure
4. Explain source code files
5. Run the generator

python src/main.py --repo . --output output/CHANGELOG.md

6. Show generated changelog
7. Conclude with learnings

# Subject to change . Filler Script right now

# Automated Changelog Generator – Demo Script

## 1. Navigate to Project Directory

```bash
cd Automated-Changelog-Generator
```

Explanation: Navigate to the root folder of the project repository.

---

## 2. Show Project Structure

```powershell
tree /F
```

Explanation:
Display the project directory structure including source code, documentation, and output folders.

---

## 3. Show Git Commit History

```bash
git log --oneline
```

Explanation:
Display commit history using concise format.
Notice the conventional commit prefixes like `feat`, `fix`, `docs`, and `chore`.

These prefixes allow the changelog generator to categorize commits automatically.

---

## 4. Run the Changelog Generator

```bash
python src/main.py --repo . --output output/CHANGELOG.md
```

Explanation:
Run the automated changelog generator.

The program will:

1. Read commit history from the Git repository
2. Parse commit messages
3. Categorize commits based on prefixes
4. Generate a Markdown changelog file

---

## 5. Open Generated Changelog

```powershell
code output/CHANGELOG.md
```

Explanation:
Open the generated changelog file to view categorized commits.

Expected sections may include:

* Features
* Bug Fixes
* Documentation
* Maintenance
* Other

---

## 6. Simulate a New Feature Commit

```bash
git commit --allow-empty -m "feat: add demo feature"
```

Explanation:
Create a dummy commit to simulate a new feature being added to the project.

---

## 7. Verify New Commit

```bash
git log --oneline
```

Explanation:
Confirm that the new commit appears in the repository history.

---

## 8. Regenerate the Changelog

```bash
python src/main.py --repo . --output output/CHANGELOG.md
```

Explanation:
Run the generator again to update the changelog with the new commit.

---

## 9. View Updated Changelog

```powershell
code output/CHANGELOG.md
```

Explanation:
The newly added commit should now appear under the **Features** section of the changelog.

---

# Demo Flow Summary

I will run commands in this order during the demo:

1. `tree /F`
2. `git log --oneline`
3. `python src/main.py --repo . --output output/CHANGELOG.md`
4. `code output/CHANGELOG.md`
5. `git commit --allow-empty -m "feat: add demo feature"`
6. `git log --oneline`
7. `python src/main.py --repo . --output output/CHANGELOG.md`
8. `code output/CHANGELOG.md`

---

# Key Points to Mention During Demo

* Tool automates changelog creation
* Uses Git commit history
* Supports conventional commit prefixes
* Generates structured Markdown output
* Demonstrates DevOps automation concepts
