from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')
with open ('source_file.txt', 'w') as f:
    f.write(source)
# with open('csv_scrape.csv', 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(['Headline', 'Summary', 'Video link'])

#     for article in soup.find_all('article'):

#         # print(article.prettify())

#         headline = article.h2.a.text
#         # print(headline)

#         summary = article.find('div', class_='entry-content').p.text
#         # print(summary)
        
#         try: 
#             vid_src = article.find('iframe', class_='youtube-player')['src'] #vid_src attrs is a dict
#             vid_id = vid_src.split('/')[4].split('?')[0]
#             yt_link = f'https://www.youtube.com/watch?v={vid_id}'
#         except Exception as e:
#             yt_link = None

#         # print(yt_link)

#         csv_writer.writerow([headline,summary,yt_link])
