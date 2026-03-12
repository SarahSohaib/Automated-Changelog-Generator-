# Design Document

## System Overview

The Automated Changelog Generator extracts commit history from a Git repository and converts it into a structured Markdown changelog.

## Architecture

Pipeline:

Git Repository
↓
Commit Extraction (git_parser.py)
↓
Commit Categorization
↓
Markdown Generation
↓
CHANGELOG.md

## Components

main.py
CLI entry point that runs the generator.

git_parser.py
Extracts commit history using git log.

changelog_generator.py
Formats commits into structured markdown sections.