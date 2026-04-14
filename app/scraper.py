import re
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from app.config import BROWSER_HEADERS, SCRAPE_TIMEOUT

def _make_absolute(soup, base_url):
    for tag in soup.find_all(["img", "script", "link", "source", "video", "audio"]):
        for attr in ("src", "href", "data-src", "poster"):
            val = tag.get(attr)
            if not val: continue
            if val.startswith(("http://", "https://", "data:", "#")): continue
            if val.startswith("//"):
                tag[attr] = "https:" + val
            else:
                tag[attr] = urljoin(base_url, val)

    for tag in soup.find_all("a"):
        href = tag.get("href")
        if href and not href.startswith(("http", "data:", "#", "mailto:", "tel:", "javascript:")):
            tag["href"] = urljoin(base_url, href)

    for tag in soup.find_all(["img", "source"]):
        srcset = tag.get("srcset")
        if not srcset: continue
        fixed_parts = []
        for part in srcset.split(","):
            part = part.strip()
            if not part: continue
            tokens = part.split()
            if tokens and not tokens[0].startswith(("http", "data:")):
                tokens[0] = urljoin(base_url, tokens[0])
            fixed_parts.append(" ".join(tokens))
        tag["srcset"] = ", ".join(fixed_parts)

    for tag in soup.find_all(style=True):
        tag["style"] = _fix_css_urls(tag["style"], base_url)

    for style_tag in soup.find_all("style"):
        if style_tag.string:
            style_tag.string = _fix_css_urls(style_tag.string, base_url)

def _fix_css_urls(css_text, base_url):
    def _replacer(m):
        url = m.group(1).strip("'\" ")
        if not url.startswith(("http", "data:")):
            url = urljoin(base_url, url)
        return f'url("{url}")'
    return re.sub(r'url\(([^)]+)\)', _replacer, css_text)

def scrape_page(url: str) -> dict:
    """
    Fetch a landing page using browser-like headers.
    """
    # Sessions can sometimes help with CSRF/Cookies that sites like Blue Bottle check
    session = requests.Session()
    resp = session.get(url, headers=BROWSER_HEADERS, timeout=SCRAPE_TIMEOUT)
    
    if resp.status_code == 403:
        raise Exception("Access Denied (403). This site blocks automated scraping. Try a different URL like stripe.com or linear.app.")
        
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "lxml")
    _make_absolute(soup, url)

    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    
    meta_desc = ""
    meta_tag = soup.find("meta", attrs={"name": "description"})
    if meta_tag:
        meta_desc = meta_tag.get("content", "")

    headings = []
    for h in soup.find_all(["h1", "h2", "h3"]):
        text = h.get_text(strip=True)
        if text: headings.append({"tag": h.name, "text": text})

    ctas = []
    for el in soup.find_all(["button", "a"]):
        text = el.get_text(strip=True)
        if not text or len(text) > 50: continue
        classes = " ".join(el.get("class", [])).lower()
        if el.name == "button" or any(kw in classes for kw in ("btn", "button", "cta")):
            ctas.append(text)

    return {
        "html": str(soup),
        "title": title,
        "meta_description": meta_desc,
        "headings": headings[:10],
        "ctas": ctas[:8],
        "url": url,
    }
