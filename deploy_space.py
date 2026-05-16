"""Deploy to Hugging Face Spaces (excludes .venv, .env, caches).

gradio deploy does NOT read .gitignore or .hfignore — use this script instead:
    uv run python deploy_space.py
"""

import os

from huggingface_hub import HfApi

SPACE_ID = os.environ.get("HF_SPACE_ID", "DylanPerera1/Personal-Chat-Bot")
REPO_DIR = os.path.dirname(os.path.abspath(__file__))

IGNORE_PATTERNS = [
    ".venv",
    ".venv/**",
    "**/.venv/**",
    "venv",
    "venv/**",
    ".git",
    ".git/**",
    "**/__pycache__/**",
    "**/*.py[cod]",
    ".DS_Store",
    ".cursor/**",
    ".pytest_cache/**",
    ".mypy_cache/**",
    ".ruff_cache/**",
    "memory.db*",
    "*.db",
    "deploy_space.py",
]


def main() -> None:
    api = HfApi()
    api.upload_folder(
        repo_id=SPACE_ID,
        repo_type="space",
        folder_path=REPO_DIR,
        ignore_patterns=IGNORE_PATTERNS,
        commit_message="Deploy app",
    )



if __name__ == "__main__":
    main()
