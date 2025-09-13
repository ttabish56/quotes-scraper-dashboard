# scraper_quotes.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser

BASE_URL = "https://quotes.toscrape.com/"

HEADERS = {
    "User-Agent": "DemoScraper/1.0 (+https://your-github-or-email.example)"
}

def allowed_to_scrape(base_url, user_agent="*"):
    rp = RobotFileParser()
    rp.set_url(urljoin(base_url, "robots.txt"))
    try:
        rp.read()
        return rp.can_fetch(user_agent, base_url)
    except Exception:
        # If robots.txt not retrievable, be conservative and continue only for demos
        return True

def get_soup(session, url):
    resp = session.get(url, timeout=10)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "lxml")

def parse_quotes_from_soup(soup):
    quotes = []
    for q in soup.find_all("div", class_="quote"):
        text = q.find("span", class_="text").get_text(strip=True)
        author = q.find("small", class_="author").get_text(strip=True)
        tag_elems = q.find_all("a", class_="tag")
        tags = [t.get_text(strip=True) for t in tag_elems]
        quotes.append({
            "quote": text,
            "author": author,
            # join tags so CSV stays simple; will split later for analysis
            "tags": "|".join(tags)
        })
    return quotes

def scrape_all_quotes(base_url):
    if not allowed_to_scrape(base_url):
        raise SystemExit("Scraping disallowed by robots.txt")

    sess = requests.Session()
    sess.headers.update(HEADERS)
    url = base_url
    all_quotes = []
    page = 1

    while True:
        print(f"Scraping page {page}: {url}")
        soup = get_soup(sess, url)
        quotes = parse_quotes_from_soup(soup)
        if not quotes:
            break
        all_quotes.extend(quotes)

        # find next page
        next_li = soup.find("li", class_="next")
        if next_li and next_li.find("a"):
            next_href = next_li.find("a")["href"]
            url = urljoin(base_url, next_href)
            page += 1
            time.sleep(random.uniform(1.0, 2.5))  # polite delay
        else:
            break

    return all_quotes

if __name__ == "__main__":
    data = scrape_all_quotes(BASE_URL)
    df = pd.DataFrame(data)
    df.to_csv("quotes.csv", index=False, encoding="utf-8-sig")
    print("Saved", len(df), "quotes to quotes.csv")

