# Viral Russia News - Automation Complete ✅

## What Was Done Today

### 1. Fixed the Netlify Deployment Issue
- **Problem**: index.html was loading `news-data.json` instead of `viral_russia_news.json`
- **Solution**: Updated the fetch URL in index.html
- **Result**: Site now displays today's news correctly at https://viral-russia-news.netlify.app/

### 2. Created Automated Collection System
Three new files were added to enable daily automation:

#### **`collect_and_generate.py`**
- Automatically scrapes 6 major Russian news outlets
- Identifies stories appearing across multiple outlets
- Calculates viral scores based on cross-outlet coverage
- Generates `public/viral_russia_news.json` with top 15 stories
- Includes retry logic and error handling

#### **`.github/workflows/daily-update.yml`**
- GitHub Actions workflow configuration
- Scheduled to run daily at 6:00 AM UTC (9:00 AM Moscow time)
- Only commits when data actually changes (prevents duplicate pushes)
- Automatically triggers Netlify deployment

#### **Documentation Files**
- `AUTOMATION_SETUP.md`: Complete automation overview
- `GITHUB_ACTIONS_SETUP.md`: Step-by-step setup instructions

## Next Steps (Required)

### To Enable Daily Automation:

You need to manually add the GitHub Actions workflow file because the current GitHub token doesn't have `workflow` scope.

**Follow these steps:**

1. **Go to your repository**: https://github.com/aroga2/viral-russia-news

2. **Create the workflow file**:
   - Click "Add file" → "Create new file"
   - Name it: `.github/workflows/daily-update.yml`
   - Copy the content from the local file (see `GITHUB_ACTIONS_SETUP.md` for full instructions)

3. **Commit the file**

4. **Test it**:
   - Go to Actions tab
   - Click "Run workflow" to test manually
   - Verify it completes successfully

5. **Done!** The workflow will now run automatically every day at 6:00 AM UTC

## How It Works

```
Daily at 6:00 AM UTC
         ↓
GitHub Actions runs collect_and_generate.py
         ↓
Scrapes 6 Russian news outlets
         ↓
Analyzes cross-outlet coverage
         ↓
Calculates viral scores
         ↓
Generates viral_russia_news.json
         ↓
Checks if data changed
         ↓
If changed: Commits and pushes to GitHub
         ↓
Netlify auto-deploys updated site
         ↓
Site shows fresh news!
```

## Key Features

✅ **Fully Automated**: Runs daily without manual intervention
✅ **Smart Updates**: Only commits when data actually changes
✅ **No Duplicates**: Prevents pushing the same data repeatedly
✅ **Cross-Outlet Analysis**: Identifies stories trending across multiple outlets
✅ **Viral Scoring**: Ranks stories by trending potential (0-100)
✅ **Auto-Deploy**: Netlify automatically deploys within minutes
✅ **Free**: Uses GitHub Actions free tier (well within limits)
✅ **Transparent**: All logs available in GitHub Actions tab
✅ **Reliable**: Includes retry logic and error handling

## Monitoring

### Check Automation Status

1. **GitHub Actions Tab**: https://github.com/aroga2/viral-russia-news/actions
   - See all workflow runs
   - View detailed logs
   - Check success/failure status

2. **Email Notifications**: GitHub will email you if a workflow fails

3. **Netlify Dashboard**: See deployment history and status

### Expected Behavior

- **Daily runs**: One workflow execution per day at 6:00 AM UTC
- **Commits**: Only when news data changes (usually daily)
- **Deployments**: Netlify deploys within 1-2 minutes after commit
- **Duration**: Each workflow run takes 2-3 minutes

## Files in Repository

### Core Files
- `public/index.html` - Website interface
- `public/viral_russia_news.json` - News data (auto-updated daily)
- `collect_and_generate.py` - Collection script
- `.github/workflows/daily-update.yml` - Automation workflow (needs manual setup)

### Configuration
- `netlify.toml` - Netlify deployment settings
- `.gitignore` - Git ignore rules

### Documentation
- `README.md` - Project overview
- `AUTOMATION_SETUP.md` - Automation overview
- `GITHUB_ACTIONS_SETUP.md` - Setup instructions
- `AUTOMATION_SUMMARY.md` - This file

## Testing Locally

To test the collection script on your computer:

```bash
# Install dependencies
pip install beautifulsoup4 requests

# Run the script
python3 collect_and_generate.py

# Check output
cat public/viral_russia_news.json
```

## Troubleshooting

### Workflow Not Running

1. Check if workflow file exists in `.github/workflows/`
2. Verify Actions are enabled in repository settings
3. Check the Actions tab for error messages

### No New Data

This is normal if:
- News outlets have the same stories as yesterday
- No significant changes in trending topics
- The script successfully ran but found no changes

### Site Not Updating

1. Check GitHub Actions - did the workflow run successfully?
2. Check Netlify - did it deploy after the commit?
3. Clear browser cache and reload the site

## Cost Analysis

**GitHub Actions**: FREE
- 2,000 minutes/month for public repos
- This workflow uses ~90 minutes/month
- 95% under the free limit

**Netlify**: FREE
- 300 build minutes/month
- ~30 builds/month (one per day)
- 90% under the free limit

**Total Cost**: $0/month 🎉

## Success Metrics

After setup is complete, you should see:

✅ Daily workflow runs in GitHub Actions
✅ Daily commits to `viral_russia_news.json` (when data changes)
✅ Daily Netlify deployments
✅ Fresh news on the website every day
✅ No manual intervention required

## Support

If you encounter issues:

1. Check `GITHUB_ACTIONS_SETUP.md` for detailed setup instructions
2. Review workflow logs in the Actions tab
3. Test the script locally to isolate issues
4. Check if news outlets have changed their HTML structure

---

**Status**: ✅ Automation configured and ready
**Action Required**: Manually add workflow file (see GITHUB_ACTIONS_SETUP.md)
**Estimated Setup Time**: 5 minutes
**Last Updated**: 2025-10-23

