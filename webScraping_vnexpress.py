from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://vnexpress.net/').text
soup = BeautifulSoup(source, 'lxml')

with open('csv_scrape_vnexpress.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['Headline', 'Summary'])

    for article in soup.find_all('article'):

        headline = article.find(class_='title_news').a.text
        # print(headline)
        try:    
            summary = article.p.text
        except:
            summary = None        
        # print(summary)
        csv_writer.writerow([headline, summary])



