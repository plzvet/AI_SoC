read -p "Please enter a commit messag : " msg

git add .
git commit -m "$msg"
git push origin main
