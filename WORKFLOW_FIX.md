# GitHub Actions Workflow Fix

## Problem

The workflow failed with exit code 128, which indicates a Git permission error. This happens because GitHub Actions needs explicit permission to push commits back to the repository.

## Solution

The workflow needs two key fixes:

### 1. Add Permissions Block

Add this at the top of the workflow file (after the `on:` section):

```yaml
permissions:
  contents: write  # Required to push commits
```

### 2. Update Git Configuration

Change the git config to use the GitHub Actions bot account:

```yaml
git config --local user.name "github-actions[bot]"
git config --local user.email "github-actions[bot]@users.noreply.github.com"
```

## How to Fix

### Option 1: Update the Existing Workflow File

1. Go to your repository: https://github.com/aroga2/viral-russia-news
2. Navigate to `.github/workflows/daily-update.yml`
3. Click the pencil icon (Edit) in the top right
4. Add the `permissions:` block after line 7 (after the `workflow_dispatch:` line):

```yaml
name: Daily Viral Russia News Update

on:
  schedule:
    - cron: '0 6 * * *'
  workflow_dispatch:

permissions:
  contents: write  # Add this block

jobs:
  update-news:
    # ... rest of the file
```

5. Scroll down to the "Commit and push if changed" step
6. Update the git config lines:

```yaml
- name: Commit and push if changed
  if: steps.check_changes.outputs.changed == 'true'
  run: |
    git config --local user.name "github-actions[bot]"
    git config --local user.email "github-actions[bot]@users.noreply.github.com"
    git add public/viral_russia_news.json
    git commit -m "Auto-update: Viral Russia News - $(date +'%Y-%m-%d %H:%M UTC')"
    git push
```

7. Click "Commit changes..." in the top right
8. Add commit message: "Fix: Add permissions for GitHub Actions to push commits"
9. Click "Commit changes"

### Option 2: Replace with Fixed Version

Alternatively, delete the current workflow file and create a new one with the complete fixed version (see the full YAML below).

## Complete Fixed Workflow

Here's the complete corrected workflow file:

```yaml
name: Daily Viral Russia News Update

on:
  schedule:
    # Run every day at 6:00 AM UTC (9:00 AM Moscow time)
    - cron: '0 6 * * *'
  workflow_dispatch: # Allow manual trigger

permissions:
  contents: write  # Required to push commits

jobs:
  update-news:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          fetch-depth: 0
      
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
        continue-on-error: false
      
      - name: Check for changes
        id: check_changes
        run: |
          if git diff --quiet public/viral_russia_news.json; then
            echo "changed=false" >> $GITHUB_OUTPUT
            echo "No changes detected in viral_russia_news.json"
          else
            echo "changed=true" >> $GITHUB_OUTPUT
            echo "Changes detected in viral_russia_news.json"
          fi
      
      - name: Commit and push if changed
        if: steps.check_changes.outputs.changed == 'true'
        run: |
          git config --local user.name "github-actions[bot]"
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git add public/viral_russia_json
          git commit -m "Auto-update: Viral Russia News - $(date +'%Y-%m-%d %H:%M UTC')"
          git push
      
      - name: No changes detected
        if: steps.check_changes.outputs.changed != 'true'
        run: |
          echo "✅ No changes detected - skipping commit"
```

## Testing After Fix

1. Go to Actions tab
2. Click "Daily Viral Russia News Update"
3. Click "Run workflow"
4. Wait for it to complete
5. Should see ✅ green checkmark

## What Changed

| Before | After | Why |
|--------|-------|-----|
| No `permissions:` block | Added `permissions: contents: write` | Grants workflow permission to push |
| `user.name "GitHub Actions Bot"` | `user.name "github-actions[bot]"` | Uses official bot account |
| `user.email "actions@github.com"` | `user.email "github-actions[bot]@users.noreply.github.com"` | Uses official bot email |
| Simple git diff check | Improved check with output messages | Better debugging |

## Common Issues

### Still Getting Exit Code 128?

- Check that you added the `permissions:` block in the right place
- Verify the workflow file has no YAML syntax errors
- Make sure you're using `github-actions[bot]` exactly as shown

### Workflow Runs But Doesn't Commit?

- This is normal if the news data hasn't changed
- Check the workflow logs - should say "No changes detected"
- The workflow only commits when `viral_russia_news.json` actually changes

### Collection Script Fails?

- Some news sites may block automated requests
- Check the "Run news collection script" step in the logs
- The script includes retry logic but may occasionally fail

---

**After applying this fix, the workflow should run successfully and automatically update your site daily!**

