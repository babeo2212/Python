from bs4 import BeautifulSoup
import requests
import csv
import re
import datetime

def etsy_spider(url, max_pages):

    titles = []
    urls = []
    
    with open('spider_etsy.csv', 'w', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['Titles', 'URL'])

    t1 = datetime.datetime.now()
    print('Start Crawling...')

    url_check = url + '&page=1#items'
    source = requests.get(url_check).text
    soup = BeautifulSoup(source, 'lxml')
    ul_check = soup.findAll('ul', class_='wt-action-group wt-list-inline wt-flex-no-wrap  wt-flex-no-wrap wt-pt-xl-2 wt-pb-xl-4')

    # Check if shop has 2 or more pages:
    if ul_check == []:
        max_pages = 1

    for page in range(1, max_pages+1):
        url_run = url +'&page=' + str(page) +'#items'
        source = requests.get(url_run).text
        soup = BeautifulSoup(source, 'lxml') 

        links = []
        pattern = re.compile(r'https?://(www.etsy.com/listing/)\d*') 
        for a in soup.findAll('a'):  
            if re.search(pattern, str(a.get('href'))):
                links.append(str(a.get('href')))
        
        for link in links:
            for a in soup.findAll('a', {'href' : link}):
                titles.append(str(a.get('title')))
        
        for url_go in links:
            source = requests.get(url_go).text
            soup = BeautifulSoup(source, 'lxml')
            for img in soup.findAll('img', class_='wt-max-width-full wt-horizontal-center wt-vertical-center carousel-image wt-rounded'):
                if img.get('src') != None:
                    urls.append(str(img.get('src')))

        with open('spider_etsy.csv', 'a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(zip(titles, urls))
    
    t2 = datetime.datetime.now()
    
    d = t2 - t1
    print(f'Time completed: {d}.')
    print('Crawling Completed.')

url = input('Nhập links hộ bố: ')
max_pages = int(input('Nhập số trang cần kiếm hộ bố: '))

etsy_spider(url, max_pages)


