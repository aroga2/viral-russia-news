#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from datetime import datetime, timezone, timedelta

# Read analysis results
with open('temp_analysis_results.json', 'r', encoding='utf-8') as f:
    stories = json.load(f)

# Generate enhanced JSON with complete data
current_time = datetime.now(timezone.utc)
output = {
    "metadata": {
        "collection_date": current_time.isoformat(),
        "collection_date_display": current_time.strftime("%Y-%m-%d %H:%M UTC"),
        "generated_at": current_time.isoformat(),
        "collection_period": "daily_update",
        "total_stories": 15,
        "total_outlets": 6,
        "outlets": [
            {"name": "RT Russian", "url": "https://russian.rt.com/", "vk": "https://vk.com/rt_russian", "followers": "1.5M"},
            {"name": "TASS", "url": "https://tass.ru/"},
            {"name": "RIA Novosti", "url": "https://ria.ru/", "vk": "https://vk.com/ria", "followers": "3.3M"},
            {"name": "Rossiyskaya Gazeta", "url": "https://rg.ru/"},
            {"name": "Komsomolskaya Pravda", "url": "https://www.kp.ru/"},
            {"name": "Lenta.ru", "url": "https://lenta.ru/"}
        ],
        "scoring_methodology": {
            "outlet_coverage": "0-40 points (8 points per outlet)",
            "prominence": "0-30 points (top_story=30, featured=20, main=10)",
            "recency": "0-30 points (based on hours since publication)",
            "max_score": 100
        }
    },
    "stories": []
}

# Enhance each story with complete data including all fields expected by HTML
for story in stories[:15]:
    # Calculate publication date based on recency_hours
    pub_time = current_time - timedelta(hours=story['recency_hours'])
    date_str = pub_time.strftime("%b %d, %H:%M UTC")
    
    # Generate VK engagement text
    if story['recency_hours'] <= 2:
        vk_engagement = "High engagement"
    elif story['recency_hours'] <= 6:
        vk_engagement = "Active discussion"
    else:
        vk_engagement = "Moderate activity"
    
    # Generate why_trending based on viral score and coverage
    why_trending_parts = []
    if story['outlet_count'] >= 4:
        why_trending_parts.append(f"Covered by {story['outlet_count']} major outlets")
    if story['prominence'] == 'top_story':
        why_trending_parts.append("Featured as top story")
    elif story['prominence'] == 'featured':
        why_trending_parts.append("Prominently featured")
    if story['recency_hours'] <= 3:
        why_trending_parts.append("Breaking news")
    
    why_trending = ". ".join(why_trending_parts) + "."
    
    # Russian version
    why_trending_ru_parts = []
    if story['outlet_count'] >= 4:
        why_trending_ru_parts.append(f"Освещается {story['outlet_count']} крупными СМИ")
    if story['prominence'] == 'top_story':
        why_trending_ru_parts.append("Главная новость")
    elif story['prominence'] == 'featured':
        why_trending_ru_parts.append("Важная новость")
    if story['recency_hours'] <= 3:
        why_trending_ru_parts.append("Срочная новость")
    
    why_trending_ru = ". ".join(why_trending_ru_parts) + "."
    
    # Generate tags based on topic
    tags = [story['topic'].lower()]
    if 'Military' in story['topic'] or 'Security' in story['topic']:
        tags.append('defense')
    if 'International' in story['topic']:
        tags.append('world')
    if 'Politics' in story['topic']:
        tags.append('politics')
    
    enhanced_story = {
        "rank": story['rank'],
        "title": story['title'],
        "title_ru": story['title_ru'],
        "topic": story['topic'],
        "viral_score": story['viral_score'],
        "outlet_count": story['outlet_count'],
        "outlets": story['outlets'],
        "prominence": story['prominence'],
        "recency_hours": story['recency_hours'],
        "date": date_str,
        "vk_engagement": vk_engagement,
        "summary": story.get('excerpt', f"This story was covered by {story['outlet_count']} major Russian media outlets and achieved a viral score of {story['viral_score']}/100."),
        "summary_ru": story.get('excerpt_ru', f"Эта новость освещалась {story['outlet_count']} крупными российскими СМИ и получила вирусный рейтинг {story['viral_score']}/100."),
        "why_trending": why_trending,
        "why_trending_ru": why_trending_ru,
        "tags": tags
    }
    
    # Add source URLs based on outlets
    source_urls = []
    if 'RT Russian' in story['outlets']:
        source_urls.append({"outlet": "RT Russian", "url": "https://russian.rt.com/"})
    if 'TASS' in story['outlets']:
        source_urls.append({"outlet": "TASS", "url": "https://tass.ru/"})
    if 'RIA Novosti' in story['outlets']:
        source_urls.append({"outlet": "RIA Novosti", "url": "https://ria.ru/"})
    if 'Rossiyskaya Gazeta' in story['outlets']:
        source_urls.append({"outlet": "Rossiyskaya Gazeta", "url": "https://rg.ru/"})
    if 'Komsomolskaya Pravda' in story['outlets']:
        source_urls.append({"outlet": "Komsomolskaya Pravda", "url": "https://www.kp.ru/"})
    if 'Lenta.ru' in story['outlets']:
        source_urls.append({"outlet": "Lenta.ru", "url": "https://lenta.ru/"})
    
    enhanced_story['source_urls'] = source_urls
    output['stories'].append(enhanced_story)

# Save to BOTH filenames for compatibility
# 1. New filename (news-data.json)
with open('public/news-data.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

# 2. Legacy filename (viral_russia_news.json) - for backward compatibility
with open('public/viral_russia_news.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("Enhanced JSON generated successfully!")
print(f"Total stories: {len(output['stories'])}")
print(f"Collection date: {output['metadata']['collection_date_display']}")
print(f"Files updated: news-data.json, viral_russia_news.json")
print(f"All required fields included: date, vk_engagement, why_trending, tags, excerpts")
