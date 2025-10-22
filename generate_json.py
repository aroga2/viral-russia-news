#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from datetime import datetime, timezone

# Read analysis results
with open('temp_analysis_results.json', 'r', encoding='utf-8') as f:
    stories = json.load(f)

# Generate enhanced JSON with complete data
output = {
    "metadata": {
        "collection_date": datetime.now(timezone.utc).isoformat(),
        "collection_date_display": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
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

# Enhance each story with complete data
for story in stories[:15]:
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
        "summary": f"This story was covered by {story['outlet_count']} major Russian media outlets and achieved a viral score of {story['viral_score']}/100.",
        "summary_ru": f"Эта новость освещалась {story['outlet_count']} крупными российскими СМИ и получила вирусный рейтинг {story['viral_score']}/100."
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
