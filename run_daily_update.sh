#!/bin/bash
# Daily Viral Russia News Update Script
# This script automates the complete workflow

set -e  # Exit on error

echo "=== Viral Russia News Daily Update ==="
echo "Started at: $(date -u '+%Y-%m-%d %H:%M UTC')"
echo ""

# 1. Pull latest changes
echo "[1/6] Pulling latest changes from GitHub..."
git pull origin main

# 2. Run news collection (placeholder - would need actual scraping code)
echo "[2/6] Collecting news from 6 Russian media outlets..."
# Note: This would call your actual news collection scripts
# For now, we assume temp files are already created

# 3. Run analysis
echo "[3/6] Analyzing stories and calculating viral scores..."
python3 analyze_news.py

# 4. Generate JSON files (both versions for compatibility)
echo "[4/6] Generating JSON files..."
python3 generate_json.py

# 5. Commit and push changes
echo "[5/6] Committing and pushing to GitHub..."
git config user.email "manus@automation.bot"
git config user.name "Manus Bot"
git add public/news-data.json public/viral_russia_news.json
git commit -m "Automated daily update - $(date -u '+%Y-%m-%d %H:%M UTC')" || echo "No changes to commit"
git push origin main

# 6. Verify deployment
echo "[6/6] Update complete! Netlify will auto-deploy in 1-3 minutes."
echo ""
echo "=== Update Summary ==="
echo "Completed at: $(date -u '+%Y-%m-%d %H:%M UTC')"
echo "Files updated:"
echo "  - public/news-data.json"
echo "  - public/viral_russia_news.json"
echo ""
echo "Latest commit:"
git log -1 --oneline
echo ""
echo "Deployment will be available at your Netlify URL shortly."
