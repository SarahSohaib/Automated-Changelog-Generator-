import argparse
from git_parser import get_commits
from changelog_generator import generate_changelog


def main():
    # Create CLI argument parser
    parser = argparse.ArgumentParser(
        description="Automated Changelog Generator from Git commit history"
    )

    parser.add_argument(
        "--repo",
        default=".",
        help="Path to the Git repository (default: current directory)"
    )

    parser.add_argument(
        "--output",
        default="CHANGELOG.md",
        help="Output changelog file name"
    )

    args = parser.parse_args()

    # Get commits from repository
    commits = get_commits(args.repo)

    if not commits:
        print("No commits found in repository.")
        return

    # Generate changelog text
    changelog = generate_changelog(commits)

    # Write changelog to file
    with open(args.output, "w", encoding="utf-8") as file:
        file.write(changelog)

    print(f"Changelog generated successfully: {args.output}")


if __name__ == "__main__":
    main()