# Setting Up GitHub Actions for Automated Daily Updates

## Why Manual Setup is Needed

The GitHub Personal Access Token used for this repository doesn't have the `workflow` scope, which is required to create or modify GitHub Actions workflows programmatically. You need to add the workflow file manually through the GitHub web interface.

## Step-by-Step Instructions

### Step 1: Create the Workflow Directory

1. Go to your repository: https://github.com/aroga2/viral-russia-news
2. Click on "Add file" → "Create new file"
3. In the filename field, type: `.github/workflows/daily-update.yml`
   - GitHub will automatically create the directories

### Step 2: Copy the Workflow Content

Copy and paste this entire content into the file:

```yaml
name: Daily Viral Russia News Update

on:
  schedule:
    # Run every day at 6:00 AM UTC (9:00 AM Moscow time)
    - cron: '0 6 * * *'
  workflow_dispatch: # Allow manual trigger

jobs:
  update-news:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install beautifulsoup4 requests
      
      - name: Run news collection script
        run: |
          python3 collect_and_generate.py
      
      - name: Check for changes
        id: check_changes
        run: |
          git diff --quiet public/viral_russia_news.json || echo "changed=true" >> $GITHUB_OUTPUT
      
      - name: Commit and push if changed
        if: steps.check_changes.outputs.changed == 'true'
        run: |
          git config user.name "GitHub Actions Bot"
          git config user.email "actions@github.com"
          git add public/viral_russia_news.json
          git commit -m "Auto-update: Viral Russia News - $(date +'%Y-%m-%d')"
          git push
      
      - name: No changes detected
        if: steps.check_changes.outputs.changed != 'true'
        run: |
          echo "No changes detected in viral_russia_news.json - skipping commit"
```

### Step 3: Commit the File

1. Scroll down to "Commit new file"
2. Add commit message: "Add GitHub Actions workflow for daily news updates"
3. Click "Commit new file"

### Step 4: Verify Setup

1. Go to the "Actions" tab in your repository
2. You should see "Daily Viral Russia News Update" workflow listed
3. Click on it to see the workflow details

### Step 5: Test the Workflow

**Manual Test:**
1. In the Actions tab, click on "Daily Viral Russia News Update"
2. Click "Run workflow" button (top right)
3. Select the branch (main)
4. Click "Run workflow"
5. Watch the workflow execute in real-time

**Automatic Schedule:**
- The workflow will run automatically every day at 6:00 AM UTC
- Check back tomorrow to verify it ran successfully

## What the Workflow Does

1. **Runs Daily**: Automatically executes at 6:00 AM UTC (9:00 AM Moscow time)
2. **Collects News**: Scrapes 6 major Russian news outlets
3. **Analyzes**: Identifies cross-outlet stories and calculates viral scores
4. **Updates**: Generates fresh `viral_russia_news.json` file
5. **Smart Commit**: Only commits if the data has actually changed
6. **Auto-Deploy**: Netlify automatically deploys the updated site

## Monitoring

### Check Workflow Status

1. Go to Actions tab
2. See all workflow runs with their status (✅ success, ❌ failed)
3. Click on any run to see detailed logs

### Email Notifications

GitHub will email you if a workflow fails. You can customize this in:
- Settings → Notifications → Actions

## Troubleshooting

### Workflow Not Showing Up

- Make sure the file is in `.github/workflows/` directory
- File must have `.yml` or `.yaml` extension
- Check the Actions tab is enabled in repository settings

### Workflow Fails

Common issues:
1. **Website blocking**: Some outlets may block automated requests
2. **Rate limiting**: Too many requests in short time
3. **HTML structure changed**: Websites update their structure

Check the workflow logs in the Actions tab for specific error messages.

### No Changes Committed

This is normal! The workflow only commits when:
- New stories are found
- Viral scores change significantly
- Story rankings change

If the news is the same as yesterday, no commit will be made.

## Alternative: Update GitHub Token

If you want to manage workflows programmatically in the future:

1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Click on your token or create a new one
3. Enable these scopes:
   - ✅ `repo` (full control)
   - ✅ `workflow` (update workflows)
4. Update the token in your local git configuration

## Cost

GitHub Actions is **free** for public repositories with generous limits:
- 2,000 minutes/month for free accounts
- This workflow uses ~2-3 minutes per run
- Running daily = ~90 minutes/month
- Well within free tier limits

---

**Need Help?**
- Check GitHub Actions documentation: https://docs.github.com/en/actions
- Review workflow logs in the Actions tab
- Test manually using "Run workflow" button

