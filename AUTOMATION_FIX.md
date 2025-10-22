# Automation Fix Documentation

**Date**: 2025-10-22  
**Issue**: Website displaying old data instead of newly collected news  
**Status**: ✅ RESOLVED

## Problem Identified

The website was showing yesterday's news data even after successfully collecting and pushing today's data to GitHub. 

### Root Cause

**File Naming Mismatch**: 
- The `index.html` file was configured to load `viral_russia_news.json`
- The new data collection script was generating `news-data.json`
- Result: Website loaded old data from the legacy filename

## Solutions Implemented

### 1. Updated index.html (Commit: fb10d72)
Changed the JSON file reference in the website:
```javascript
// Before:
const response = await fetch('viral_russia_news.json');

// After:
const response = await fetch('news-data.json');
```

### 2. Updated generate_json.py (Commit: 61e97e4)
Modified the JSON generation script to create **both** files for backward compatibility:
```python
# Save to BOTH filenames for compatibility
# 1. New filename (news-data.json)
with open('public/news-data.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

# 2. Legacy filename (viral_russia_news.json) - for backward compatibility
with open('public/viral_russia_news.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
```

### 3. Created Automated Update Script (run_daily_update.sh)
A comprehensive bash script that handles the complete daily workflow:

**Features:**
- Pulls latest changes from GitHub
- Runs news collection (placeholder for actual scraping)
- Executes analysis and scoring
- Generates **both** JSON files
- Commits and pushes changes with proper timestamps
- Provides detailed progress logging

**Usage:**
```bash
cd /home/ubuntu/viral-russia-news
./run_daily_update.sh
```

## File Structure

```
viral-russia-news/
├── public/
│   ├── index.html              # Website (loads news-data.json)
│   ├── news-data.json          # Primary data file (new)
│   ├── viral_russia_news.json  # Legacy data file (for compatibility)
│   └── ...
├── analyze_news.py             # Story analysis and viral scoring
├── generate_json.py            # JSON generation (dual output)
├── run_daily_update.sh         # Complete automation script
└── AUTOMATION_FIX.md           # This documentation
```

## Benefits of Dual File Approach

1. **Backward Compatibility**: Old systems referencing `viral_russia_news.json` continue working
2. **Forward Compatibility**: New systems can use the cleaner `news-data.json` filename
3. **Zero Downtime**: No risk of the website breaking during transitions
4. **Flexibility**: Either filename can be used without issues

## Deployment Status

**GitHub Repository**: ✅ Updated  
**Latest Commits**:
- `61e97e4` - Add automated daily update script with dual JSON file support
- `dc2181f` - Update both JSON files with today's news data
- `fb10d72` - Fix: Update index.html to load news-data.json

**Netlify**: Auto-deployment triggered  
**Expected**: Website will show fresh data within 1-3 minutes of push

## Future Automation

For scheduled daily updates, use one of these approaches:

### Option 1: Cron Job (Linux/Mac)
```bash
# Add to crontab (runs daily at 10:00 AM Moscow time = 07:00 UTC)
0 7 * * * cd /home/ubuntu/viral-russia-news && ./run_daily_update.sh >> logs/daily_update.log 2>&1
```

### Option 2: GitHub Actions
Create `.github/workflows/daily-update.yml`:
```yaml
name: Daily News Update
on:
  schedule:
    - cron: '0 7 * * *'  # 07:00 UTC daily
  workflow_dispatch:  # Allow manual trigger

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run daily update
        run: ./run_daily_update.sh
```

### Option 3: Manus Scheduled Task
Use the Manus scheduling feature to run this workflow daily at a specified time.

## Verification Checklist

After each update, verify:
- [ ] Both JSON files updated with same timestamp
- [ ] GitHub commit successful
- [ ] Netlify deployment triggered
- [ ] Website displays new data (check collection date)
- [ ] All 15 stories present with correct rankings
- [ ] Viral scores calculated correctly

## Troubleshooting

### Issue: Website still shows old data
**Solution**: Check browser cache, hard refresh (Ctrl+Shift+R)

### Issue: JSON files not updating
**Solution**: Verify `temp_analysis_results.json` exists and contains data

### Issue: Git push fails
**Solution**: Check GitHub token is valid, pull latest changes first

### Issue: Netlify not deploying
**Solution**: Verify GitHub-Netlify connection in Netlify dashboard

## Contact

For issues or questions about this automation:
- Check GitHub repository: https://github.com/aroga2/viral-russia-news
- Review commit history for recent changes
- Examine Netlify deployment logs

---
*Last Updated: 2025-10-22 09:32 UTC*

