# quotes-scraper-dashboard
Scrape Data Of Quotes
📊 Quotes Scraper Dashboard

A Python-based project that scrapes inspirational quotes from the web and presents them in an interactive dashboard using Streamlit.

This project demonstrates web scraping, data cleaning, and data visualization in one workflow—ideal for showcasing Data Science & Web Scraping skills.

🚀 Features

🔎 Web Scraper – Extracts quotes, authors, and tags from a website

🧹 Data Cleaning – Saves clean data into a CSV file with UTF-8 encoding

📈 Interactive Dashboard – Visualizes quotes data (authors, tags, frequency) with Streamlit

💾 Export Data – Saves scraped data in a reusable CSV format

⚙️ Installation

Clone the repo and set up a virtual environment:

git clone https://github.com/ttabish56/quotes-scraper-dashboard.git
cd quotes-scraper-dashboard

# create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# install requirements
pip install -r requirements.txt

▶️ Usage
1️⃣ Run the scraper
python scraper.py


Scraped quotes will be saved into quotes.csv.

2️⃣ Launch the dashboard
streamlit run dashboard.py


Open the provided local URL in your browser

Explore quotes by authors, tags, and statistics

📊 Example Output

Scraper Output (CSV):

Quote	Author	Tags
“Life is what happens...”	John Lennon	life, inspiration
“Be yourself...”	Oscar Wilde	motivation

Dashboard Preview:
👉 (Add screenshot here after running Streamlit)

🛠️ Tech Stack

Python 3.x

BeautifulSoup / Requests – Web scraping

Pandas – Data cleaning & CSV handling

Streamlit – Interactive dashboard

🎯 Why This Project Matters

This project is designed to highlight:

✅ End-to-end workflow (Scraping → Cleaning → Visualization)

✅ Skills in Python, Data Processing, Dashboards

✅ Practical use-case for Data Science Interviews

📌 Future Improvements

Add database support (SQLite / MongoDB)

Implement scheduled scraping (cron jobs)

Deploy dashboard on Streamlit Cloud / Heroku
