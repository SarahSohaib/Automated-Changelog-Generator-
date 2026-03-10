from collections import defaultdict


def categorize_commit(message):
    """
    Categorize commit message based on conventional commit prefix
    """

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


def generate_changelog(commits):
    """
    Generate markdown changelog text
    """

    categorized = defaultdict(list)

    for commit in commits:
        category = categorize_commit(commit["message"])
        categorized[category].append(commit)

    changelog = "# Changelog\n\n"

    for category, items in categorized.items():
        changelog += f"## {category}\n"

        for commit in items:
            line = f"- {commit['message']} ({commit['hash']}) - {commit['author']} [{commit['date']}]\n"
            changelog += line

        changelog += "\n"

    return changelog