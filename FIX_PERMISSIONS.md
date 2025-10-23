# Fix GitHub Actions Permissions - 403 Error

## The Problem

```
remote: Permission to aroga2/viral-russia-news.git denied to github-actions[bot].
fatal: unable to access 'https://github.com/aroga2/viral-russia-news/': The requested URL returned error: 403
```

This means GitHub Actions doesn't have permission to push commits to your repository. This is a **repository settings issue**, not a workflow file issue.

## The Solution

You need to enable write permissions for GitHub Actions in your repository settings.

## Step-by-Step Fix

### 1. Go to Repository Settings

1. Navigate to: https://github.com/aroga2/viral-russia-news
2. Click on **"Settings"** tab (top right, near Insights)
3. In the left sidebar, scroll down to **"Actions"** section
4. Click on **"General"** under Actions

### 2. Update Workflow Permissions

Scroll down to the **"Workflow permissions"** section (near the bottom of the page).

You'll see two radio button options:

- ⚪ **Read repository contents and packages permissions** (currently selected)
- ⚪ **Read and write permissions**

**Select:** ✅ **"Read and write permissions"**

### 3. Enable Actions to Create Pull Requests (Optional)

Below the radio buttons, you'll see a checkbox:

☑️ **Allow GitHub Actions to create and approve pull requests**

You can leave this unchecked (not needed for this workflow).

### 4. Save Changes

Click the green **"Save"** button at the bottom of the section.

### 5. Test the Workflow Again

1. Go to the **"Actions"** tab
2. Click on **"Daily Viral Russia News Update"**
3. Click **"Run workflow"** button (top right)
4. Select **"main"** branch
5. Click **"Run workflow"**
6. Wait for it to complete - should now succeed! ✅

## Visual Guide

Here's what you're looking for in Settings:

```
Settings → Actions → General → Workflow permissions

┌─────────────────────────────────────────────────────┐
│ Workflow permissions                                 │
│                                                      │
│ ⚪ Read repository contents and packages            │
│    permissions                                       │
│                                                      │
│ ✅ Read and write permissions                       │
│    (SELECT THIS ONE)                                 │
│                                                      │
│ ☐ Allow GitHub Actions to create and approve       │
│   pull requests                                      │
│                                                      │
│ [Save]                                              │
└─────────────────────────────────────────────────────┘
```

## Why This Happens

By default, GitHub sets Actions to **read-only** for security. Since your workflow needs to:
- Collect news data
- Generate JSON file
- **Commit changes**
- **Push to repository**

It needs **write permissions** to push commits back to the repository.

## Alternative Solution: Use Personal Access Token

If you prefer not to give Actions write permissions, you can use a Personal Access Token instead:

### 1. Create a Personal Access Token

1. Go to GitHub Settings (your profile, not repository)
2. Developer settings → Personal access tokens → Tokens (classic)
3. Generate new token with `repo` scope
4. Copy the token

### 2. Add Token as Repository Secret

1. Go to repository Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `PAT_TOKEN`
4. Value: (paste your token)
5. Click "Add secret"

### 3. Update Workflow to Use Token

Change the checkout step in `.github/workflows/daily-update.yml`:

```yaml
- name: Checkout repository
  uses: actions/checkout@v4
  with:
    token: ${{ secrets.PAT_TOKEN }}  # Use PAT instead of GITHUB_TOKEN
    fetch-depth: 0
```

## Recommended Approach

**Use the repository settings fix** (Option 1) because:
- ✅ Simpler - just one setting change
- ✅ No token management needed
- ✅ Token won't expire
- ✅ Standard practice for automated workflows
- ✅ Scoped to this repository only

## After Fixing

Once you enable write permissions, the workflow will:

1. ✅ Run successfully
2. ✅ Collect news from 6 outlets
3. ✅ Generate `viral_russia_news.json`
4. ✅ Commit changes to repository
5. ✅ Push to GitHub
6. ✅ Trigger Netlify deployment
7. ✅ Update your live site

## Verification

After running the workflow successfully, you should see:

- ✅ Green checkmark in Actions tab
- ✅ New commit from `github-actions[bot]` in commit history
- ✅ Updated `viral_russia_news.json` file
- ✅ Netlify deployment triggered
- ✅ Fresh news on your website

## Quick Checklist

- [ ] Go to Settings → Actions → General
- [ ] Scroll to "Workflow permissions"
- [ ] Select "Read and write permissions"
- [ ] Click "Save"
- [ ] Go to Actions tab
- [ ] Run workflow manually
- [ ] Verify it succeeds with green checkmark
- [ ] Check that new commit appears in repository
- [ ] Verify Netlify deploys
- [ ] Check website shows updated news

---

**This is the final fix needed!** Once you enable write permissions, everything will work automatically.

