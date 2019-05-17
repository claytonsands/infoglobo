import scrapy

url = 'https://revistaautoesporte.globo.com/rss/ultimas/feed.xml'
access_url = requests.get(url=url).text
con
print(access_url)


scrapy genspider infoglobo https://revistaautoesporte.globo.com/rss/ultimas/feed.xml
