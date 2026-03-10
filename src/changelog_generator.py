from collections import defaultdict


def categorize_commit(message):
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
    categorized = defaultdict(list)

    for commit in commits:
        category = categorize_commit(commit["message"])
        categorized[category].append(commit)

    changelog = "# Changelog\n\n"

    for category, commit_list in categorized.items():
        changelog += f"## {category}\n"

        for commit in commit_list:
            changelog += f"- {commit['message']} ({commit['hash']})\n"

        changelog += "\n"

    return changelog