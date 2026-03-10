import subprocess


def get_commits(repo_path="."):
    try:
        command = [
            "git",
            "-C",
            repo_path,
            "log",
            "--pretty=format:%h|%an|%ad|%s",
            "--date=short"
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        commits = []

        for line in result.stdout.split("\n"):
            parts = line.split("|")

            if len(parts) != 4:
                continue

            commits.append({
                "hash": parts[0],
                "author": parts[1],
                "date": parts[2],
                "message": parts[3]
            })

        return commits

    except Exception as e:
        print("Error reading git history:", e)
        return []