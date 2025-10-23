#!/usr/bin/env python3
"""
Automated Viral Russia News Collection Script
Collects news from 6 major Russian outlets, analyzes viral potential, and generates JSON
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta
from collections import defaultdict
import time
import random

# User agent to avoid blocking
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_page(url, max_retries=3):
    """Fetch a webpage with retries"""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=HEADERS, timeout=15)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Attempt {attempt + 1} failed for {url}: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
    return None

def extract_rt_news():
    """Extract news from RT Russian"""
    print("Collecting from RT Russian...")
    html = fetch_page("https://russian.rt.com/")
    if not html:
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    stories = []
    
    # Extract main headlines
    for article in soup.find_all(['article', 'div'], class_=['card', 'article', 'news-item'], limit=15):
        title_elem = article.find(['h2', 'h3', 'a'])
        if title_elem:
            title = title_elem.get_text(strip=True)
            if len(title) > 20:  # Filter out short/invalid titles
                stories.append({
                    'title': title,
                    'outlet': 'RT',
                    'prominence': 'FEATURED' if 'main' in str(article.get('class', [])).lower() else 'NEWS_FEED'
                })
    
    return stories[:10]

def extract_tass_news():
    """Extract news from TASS"""
    print("Collecting from TASS...")
    html = fetch_page("https://tass.ru/")
    if not html:
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    stories = []
    
    for article in soup.find_all(['a', 'div'], class_=['Link', 'news', 'tass'], limit=15):
        title = article.get_text(strip=True)
        if len(title) > 20:
            stories.append({
                'title': title,
                'outlet': 'TASS',
                'prominence': 'TOP_STORY' if 'main' in str(article.get('class', [])).lower() else 'NEWS_FEED'
            })
    
    return stories[:10]

def extract_ria_news():
    """Extract news from RIA Novosti"""
    print("Collecting from RIA Novosti...")
    html = fetch_page("https://ria.ru/")
    if not html:
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    stories = []
    
    for article in soup.find_all(['a', 'div'], class_=['cell-list__item', 'list-item'], limit=15):
        title = article.get_text(strip=True)
        if len(title) > 20:
            stories.append({
                'title': title,
                'outlet': 'RIA',
                'prominence': 'FEATURED'
            })
    
    return stories[:10]

def extract_rg_news():
    """Extract news from Rossiyskaya Gazeta"""
    print("Collecting from Rossiyskaya Gazeta...")
    html = fetch_page("https://rg.ru/")
    if not html:
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    stories = []
    
    for article in soup.find_all(['a', 'div'], class_=['b-material', 'news'], limit=15):
        title = article.get_text(strip=True)
        if len(title) > 20:
            stories.append({
                'title': title,
                'outlet': 'RG',
                'prominence': 'MAIN'
            })
    
    return stories[:10]

def extract_kp_news():
    """Extract news from Komsomolskaya Pravda"""
    print("Collecting from Komsomolskaya Pravda...")
    html = fetch_page("https://www.kp.ru/")
    if not html:
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    stories = []
    
    for article in soup.find_all(['a', 'div'], class_=['styled', 'news'], limit=15):
        title = article.get_text(strip=True)
        if len(title) > 20:
            stories.append({
                'title': title,
                'outlet': 'KP',
                'prominence': 'NEWS_FEED'
            })
    
    return stories[:10]

def extract_lenta_news():
    """Extract news from Lenta.ru"""
    print("Collecting from Lenta.ru...")
    html = fetch_page("https://lenta.ru/")
    if not html:
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    stories = []
    
    for article in soup.find_all(['a', 'div'], class_=['card', 'item'], limit=15):
        title = article.get_text(strip=True)
        if len(title) > 20:
            stories.append({
                'title': title,
                'outlet': 'Lenta',
                'prominence': 'FEATURED'
            })
    
    return stories[:10]

def normalize_title(title):
    """Normalize title for comparison"""
    # Remove extra whitespace, convert to lowercase
    return ' '.join(title.lower().split())

def find_cross_outlet_stories(all_stories):
    """Find stories that appear across multiple outlets"""
    # Group similar stories
    story_groups = defaultdict(list)
    
    for story in all_stories:
        normalized = normalize_title(story['title'])
        # Use first 50 characters as key for grouping
        key = normalized[:50]
        story_groups[key].append(story)
    
    # Find stories with cross-outlet coverage
    cross_outlet_stories = []
    for key, group in story_groups.items():
        if len(group) >= 2:  # At least 2 outlets
            outlets = list(set([s['outlet'] for s in group]))
            cross_outlet_stories.append({
                'title': group[0]['title'],
                'outlets': outlets,
                'count': len(outlets),
                'prominence': group[0]['prominence']
            })
    
    return cross_outlet_stories

def calculate_viral_score(story):
    """Calculate viral score based on cross-outlet coverage"""
    score = 0
    
    # Cross-outlet coverage (0-70 points)
    score += min(story['count'] * 12, 70)
    
    # Prominence bonus (0-20 points)
    prominence_map = {
        'TOP_STORY': 20,
        'FEATURED': 15,
        'MAIN': 12,
        'NEWS_FEED': 8
    }
    score += prominence_map.get(story['prominence'], 5)
    
    # Recency bonus (0-10 points) - assume all are recent
    score += 10
    
    return min(int(score), 100)

def generate_enhanced_story(rank, title, outlets, viral_score):
    """Generate enhanced story data with all required fields"""
    # Determine topic based on keywords
    title_lower = title.lower()
    if any(word in title_lower for word in ['взрыв', 'погиб', 'авария', 'пожар', 'explosion', 'accident']):
        topic = 'Emergency'
    elif any(word in title_lower for word in ['путин', 'трамп', 'политик', 'putin', 'trump', 'politics']):
        topic = 'Politics'
    elif any(word in title_lower for word in ['армия', 'военн', 'дрон', 'military', 'army', 'drone']):
        topic = 'Military'
    elif any(word in title_lower for word in ['эконом', 'санкц', 'economy', 'sanctions']):
        topic = 'Economy'
    else:
        topic = 'Society'
    
    # Estimate VK engagement based on viral score
    if viral_score >= 80:
        vk_engagement = 'VERY_HIGH'
    elif viral_score >= 60:
        vk_engagement = 'HIGH'
    elif viral_score >= 40:
        vk_engagement = 'MEDIUM'
    else:
        vk_engagement = 'LOW'
    
    return {
        'rank': rank,
        'title': title,
        'title_ru': title,  # In real scraping, this would be the original Russian title
        'viral_score': viral_score,
        'outlets': outlets,
        'outlet_count': len(outlets),
        'topic': topic,
        'vk_engagement': vk_engagement,
        'prominence': 'TOP_STORY' if viral_score >= 80 else 'FEATURED',
        'summary': f"This story about '{title}' is trending across {len(outlets)} major Russian news outlets.",
        'summary_ru': f"Эта история о '{title}' в тренде в {len(outlets)} крупных российских новостных изданиях.",
        'why_trending': f"This story is trending because it appears across {len(outlets)} major outlets with a viral score of {viral_score}/100.",
        'why_trending_ru': f"Эта история в тренде, потому что появляется в {len(outlets)} крупных изданиях с вирусным рейтингом {viral_score}/100.",
        'source_urls': [
            f"https://russian.rt.com/" if 'RT' in outlets else None,
            f"https://tass.ru/" if 'TASS' in outlets else None,
            f"https://ria.ru/" if 'RIA' in outlets else None,
            f"https://rg.ru/" if 'RG' in outlets else None,
            f"https://www.kp.ru/" if 'KP' in outlets else None,
            f"https://lenta.ru/" if 'Lenta' in outlets else None
        ],
        'source_urls': [url for url in [
            "https://russian.rt.com/" if 'RT' in outlets else None,
            "https://tass.ru/" if 'TASS' in outlets else None,
            "https://ria.ru/" if 'RIA' in outlets else None,
            "https://rg.ru/" if 'RG' in outlets else None,
            "https://www.kp.ru/" if 'KP' in outlets else None,
            "https://lenta.ru/" if 'Lenta' in outlets else None
        ] if url],
        'date': datetime.now().strftime('%Y-%m-%d'),
        'tags': [topic.lower(), 'trending', 'russia']
    }

def main():
    """Main execution function"""
    print("=" * 80)
    print("VIRAL RUSSIA NEWS - AUTOMATED COLLECTION")
    print("=" * 80)
    print()
    
    # Collect from all outlets
    all_stories = []
    all_stories.extend(extract_rt_news())
    time.sleep(1)  # Be polite to servers
    all_stories.extend(extract_tass_news())
    time.sleep(1)
    all_stories.extend(extract_ria_news())
    time.sleep(1)
    all_stories.extend(extract_rg_news())
    time.sleep(1)
    all_stories.extend(extract_kp_news())
    time.sleep(1)
    all_stories.extend(extract_lenta_news())
    
    print(f"\nTotal stories collected: {len(all_stories)}")
    
    # Find cross-outlet stories
    cross_outlet_stories = find_cross_outlet_stories(all_stories)
    print(f"Cross-outlet stories found: {len(cross_outlet_stories)}")
    
    # Calculate viral scores and rank
    for story in cross_outlet_stories:
        story['viral_score'] = calculate_viral_score(story)
    
    # Sort by viral score
    ranked_stories = sorted(cross_outlet_stories, key=lambda x: x['viral_score'], reverse=True)
    
    # Take top 15
    top_15 = ranked_stories[:15]
    
    # Generate enhanced stories
    enhanced_stories = []
    for i, story in enumerate(top_15, 1):
        enhanced = generate_enhanced_story(
            rank=i,
            title=story['title'],
            outlets=story['outlets'],
            viral_score=story['viral_score']
        )
        enhanced_stories.append(enhanced)
    
    # Generate output JSON
    output = {
        'metadata': {
            'generated_at': datetime.now().isoformat(),
            'collection_period': datetime.now().strftime('%Y-%m-%d'),
            'total_outlets': 6,
            'outlets': [
                {'name': 'RT Russian', 'url': 'https://russian.rt.com/'},
                {'name': 'TASS', 'url': 'https://tass.ru/'},
                {'name': 'RIA Novosti', 'url': 'https://ria.ru/'},
                {'name': 'Rossiyskaya Gazeta', 'url': 'https://rg.ru/'},
                {'name': 'Komsomolskaya Pravda', 'url': 'https://www.kp.ru/'},
                {'name': 'Lenta.ru', 'url': 'https://lenta.ru/'}
            ]
        },
        'stories': enhanced_stories
    }
    
    # Save to file
    output_path = 'public/viral_russia_news.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Successfully generated {output_path}")
    print(f"   Top 15 stories ranked by viral score")
    print("=" * 80)

if __name__ == '__main__':
    main()

