
# === User Configuration ===
GITHUB_TOKEN="ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Replace with your actual token
GITHUB_USERNAME="your_username"                 # e.g., hulklee1
REPO_NAME="your_repo"                           # e.g., AI_SoC

# === Construct GitHub URL with token ===
GITHUB_URL="https://${GITHUB_USERNAME}:${GITHUB_TOKEN}@github.com/${GITHUB_USERNAME}/${REPO_NAME}.git"

# === Initialize Git if not already a repo ===
if ! git rev-parse --is-inside-work-tree &>/dev/null; then
  echo "Not a Git repository. Initializing..."
  git init
  git branch -M main
fi

# === Get current branch name ===
BRANCH=$(git branch --show-current)
echo "Current branch: $BRANCH"

# === Add files ===
if [ $# -gt 0 ]; then
  echo "Adding specified files: $@"
  git add "$@"
else
  echo "Adding all changes"
  git add .
fi

# === Get commit message ===
read -p "Enter commit message (leave blank for auto message): " msg
if [ -z "$msg" ]; then
  msg="Auto commit: $(date '+%Y-%m-%d %H:%M:%S')"
fi
git commit -m "$msg"

# === Reset remote origin with token-authenticated URL ===
git remote remove origin 2>/dev/null
git remote add origin "$GITHUB_URL"

# === Push to GitHub ===
git push -u origin "$BRANCH"

