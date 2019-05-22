# -*- coding: utf-8 -*-
import scrapy
from parsel import Selector
from bs4 import BeautifulSoup
from pymongo import MongoClient


class InfogloboSpider(scrapy.Spider):
    name = 'infoglobo'
    allowed_domains = ['revistaautoesporte.globo.com']
    start_urls = ['https://revistaautoesporte.globo.com/rss/ultimas/feed.xml']

    def parse(self, response):
        client = MongoClient()
        db = client.crawler
        tag_description = []
        feed = []
        for x in range(0, len(response.xpath("//item"))):
            title = response.xpath("//item/title/text()")[x].get()
            link = response.xpath("//item/link/text()")[x].get()
            html = Selector(response.xpath("//item/description/text()")[x].get())
            tag_a_desc = html.xpath("//div/ul/li/a/@href").getall()

            soup = BeautifulSoup(html.get(), "html.parser")
            for tag in soup.find_all(['img', 'p']):
                if tag.name == 'img':
                    tag_description.append({
                        'type': 'image',
                        'content': tag.get('src')
                    })
                else:
                    tag_description.append({
                        'type': 'text',
                        'content': tag.text
                    })
            tag_description.append({
                'type': 'links',
                'content': tag_a_desc
            })
            feed.append({
                    'item': {
                        'title': title,
                        'link': link,
                        'description': tag_description
                    }
                })
        result = {'feed': feed}
        db.feed.insert(result)
        return result

#scrapy shell https://revistaautoesporte.globo.com/rss/ultimas/feed.xml
#scrapy runspider crawler\spiders\infoglobo.py -o infoglobo.jsonlines