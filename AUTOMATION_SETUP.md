# Viral Russia News - Automation Setup

## Overview

This repository is configured to automatically collect and update viral Russia news daily using GitHub Actions.

## How It Works

### Daily Automated Collection

1. **Schedule**: GitHub Actions runs every day at 6:00 AM UTC (9:00 AM Moscow time)
2. **Collection**: The script collects news from 6 major Russian outlets:
   - RT Russian
   - TASS
   - RIA Novosti
   - Rossiyskaya Gazeta
   - Komsomolskaya Pravda
   - Lenta.ru

3. **Analysis**: 
   - Identifies stories appearing across multiple outlets
   - Calculates viral scores based on cross-outlet coverage
   - Ranks top 15 stories by viral potential

4. **Update**: 
   - Generates `public/viral_russia_news.json` with fresh data
   - Only commits if the data has changed (prevents duplicate pushes)
   - Automatically deploys to Netlify

### Files

- **`.github/workflows/daily-update.yml`**: GitHub Actions workflow configuration
- **`collect_and_generate.py`**: Main collection and analysis script
- **`public/viral_russia_news.json`**: Output JSON file consumed by the website
- **`public/index.html`**: Website that displays the news

### Manual Trigger

You can manually trigger the workflow:

1. Go to your GitHub repository
2. Click on "Actions" tab
3. Select "Daily Viral Russia News Update"
4. Click "Run workflow"

### Monitoring

Check the GitHub Actions tab to monitor:
- Workflow execution status
- Collection logs
- Any errors or failures

### Change Detection

The workflow includes smart change detection:
- Compares new data with existing `viral_russia_news.json`
- Only commits and pushes if there are actual changes
- Prevents pushing the same data repeatedly

### Troubleshooting

If the automation fails:

1. **Check GitHub Actions logs**: Go to Actions tab and review the failed workflow
2. **Website blocking**: Some outlets may block automated requests - the script includes retries and delays
3. **Dependencies**: Ensure `beautifulsoup4` and `requests` are properly installed (handled automatically)

### Local Testing

To test the collection script locally:

```bash
# Install dependencies
pip install beautifulsoup4 requests

# Run the script
python3 collect_and_generate.py

# Check the output
cat public/viral_russia_news.json
```

### Customization

**Change collection time**: Edit `.github/workflows/daily-update.yml`:
```yaml
schedule:
  - cron: '0 6 * * *'  # Change to your preferred time (UTC)
```

**Adjust number of stories**: Edit `collect_and_generate.py`:
```python
top_15 = ranked_stories[:15]  # Change 15 to desired number
```

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     GitHub Actions                          │
│  (Runs daily at 6:00 AM UTC)                               │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              collect_and_generate.py                        │
│  • Scrapes 6 Russian news outlets                          │
│  • Identifies cross-outlet stories                         │
│  • Calculates viral scores                                 │
│  • Generates JSON with top 15 stories                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         public/viral_russia_news.json                       │
│  (Only committed if changed)                                │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   Git Push to GitHub                        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              Netlify Auto-Deploy                            │
│  (Triggered by GitHub push)                                 │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         https://viral-russia-news.netlify.app               │
│  (Live website with updated news)                           │
└─────────────────────────────────────────────────────────────┘
```

## Benefits

✅ **Fully Automated**: No manual intervention required
✅ **Smart Updates**: Only pushes when data actually changes
✅ **Reliable**: Includes retry logic and error handling
✅ **Fast Deployment**: Netlify automatically deploys within minutes
✅ **Transparent**: All logs available in GitHub Actions
✅ **Free**: Uses GitHub Actions free tier (2,000 minutes/month)

## Next Steps

1. **Enable GitHub Actions**: Ensure Actions are enabled in your repository settings
2. **Monitor First Run**: Check the Actions tab after the first scheduled run
3. **Verify Netlify**: Confirm Netlify deploys automatically after each push
4. **Customize**: Adjust collection time, number of stories, or outlets as needed

---

**Last Updated**: 2025-10-23  
**Automation Status**: ✅ Active

