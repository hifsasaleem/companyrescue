import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup

# scraper = cloudscraper.create_scraper(delay=3)
n = 1
last = 70
for i in range(n, last+1):
    url = f"https://www.companyrescue.co.uk/guides-knowledge/news/{n}/"
    print(f"\033[1;33;40m Data SCRAPING from : {url} \n")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    divs = soup.find_all("div", {"class": "details"})
    for div in divs:
        try:
            a = div.h2.a.get("href")
            url = "https://www.companyrescue.co.uk" + a
            print(url)
            row = [url]
            with open('www.companyrescue.co.uk.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(row)
        except:
            pass
    n = n+1

file_name = "www.companyrescue.co.uk.csv"
file_name_output = "companyrescue_urls.csv"
df = pd.read_csv(file_name, sep="\t or ,")
df.drop_duplicates(subset=None, inplace=True)
df.to_csv(file_name_output, index=False)
