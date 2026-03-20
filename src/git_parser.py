import subprocess

def get_commits(repo_path="."):

    command = [
    "git",
    "-C",
    repo_path,
    "log",
    "--pretty=format:%h|%an|%ad|%s|%p",
    "--date=short"
]

    result = subprocess.run(command, capture_output=True, text=True)

    commits = []

    for line in result.stdout.split("\n"):

        parts = line.split("|")

        if len(parts) != 5:
            continue
        
        is_merge = len(parts[4].split()) > 1

        commits.append({
            "hash": parts[0],
            "author": parts[1],
            "date": parts[2],
            "message": parts[3],
            "is_merge": is_merge
        })

    return commits