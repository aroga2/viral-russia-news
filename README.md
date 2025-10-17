# Viral Russia News

Daily analysis of the top 15 most viral news stories from major Russian media outlets.

## Overview

This project automatically collects and analyzes trending news stories from 6 major Russian media sources:
- RT Russian
- TASS
- RIA Novosti
- Rossiyskaya Gazeta
- Komsomolskaya Pravda
- Lenta.ru

## Features

- **Automated Daily Updates**: Scheduled task runs daily at 10:00 AM Moscow time
- **Viral Score Algorithm**: Ranks stories based on cross-outlet coverage, homepage prominence, recency, and social media engagement
- **Bilingual Content**: All stories include both English and Russian translations
- **Detailed Analysis**: Each story includes summary, context, and "Why Trending" explanation

## Data Structure

The `public/viral_russia_news.json` file contains:
- Collection metadata (timestamp, period, outlets)
- Top 15 ranked stories with:
  - Title (English & Russian)
  - Viral score (0-100)
  - Summary and analysis
  - Source outlets
  - Topic tags
  - VK engagement metrics

## Deployment

This site is deployed on Netlify and automatically updates daily via scheduled task.

## License

Data collected from public news sources. Analysis and presentation by Manus AI.

