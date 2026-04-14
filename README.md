# AdSync

AI-powered tool that personalizes landing pages based on ad creatives.

The idea: when someone clicks an ad and lands on your page, the page should feel like a continuation of that ad. This tool automates that — you give it your ad image and landing page URL, and it modifies the page to match the ad's messaging, colors, and CTA.

## What it does

- **Analyzes the ad** using Gemini Vision (extracts headline, CTA, colors, tone, USPs)
- **Scrapes the landing page** (fetches HTML, resolves all relative URLs) 
- **Personalizes the page** using CRO principles:
  - Message match — page headline reflects the ad's headline
  - CTA alignment — button text matches the ad's call-to-action
  - Color continuity — accent colors shift to match the ad's palette
  - Trust signals — adds urgency/offer elements from the ad
  - Hero section enhancement

The output is the *same* page, not a new one — just enhanced for conversion.

## Setup

```bash
# create venv and install deps
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# add your gemini api key
cp .env.example .env
# edit .env with your key (get one at https://aistudio.google.com/apikey)

# run
uvicorn main:app --reload --port 8000
```

Then open http://localhost:8000

## Project Structure

```
├── main.py              # FastAPI entry point
├── app/
│   ├── config.py        # env vars, constants
│   ├── scraper.py       # landing page scraper
│   ├── analyzer.py      # Gemini Vision ad analysis
│   ├── personalizer.py  # CRO personalization engine
│   └── routes.py        # API endpoints
├── static/
│   ├── index.html       
│   ├── style.css        
│   └── app.js           
├── requirements.txt
└── .env
```

## Tech stack

- Python / FastAPI
- Google Gemini 2.0 Flash (vision + text)
- BeautifulSoup for scraping
- Vanilla HTML/CSS/JS frontend

## Notes / Assumptions

- Ad creative should be an image (PNG/JPG/WebP)
- Landing page needs to be publicly accessible (no auth walls)
- Personalization focuses on text + inline styles — doesn't modify JS behavior
- Works best on marketing/product pages; complex SPAs might not scrape well
