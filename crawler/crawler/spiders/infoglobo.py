# -*- coding: utf-8 -*-
import scrapy


class InfogloboSpider(scrapy.Spider):
    name = 'infoglobo'
    allowed_domains = ['revistaautoesporte.globo.com']
    start_urls = ['https://revistaautoesporte.globo.com/rss/ultimas/feed.xml']

    def parse(self, response):
        for item in response.xpath("//item"):
            title = item.xpath("//title/text()").extract_first()
            link = item.xpath("//link/text()").extract_first()
            for itens in item.xpath("//description"):
                itens.xpath("//")

            yield {
                'item': {
                    'title': title,
                    'link': link,
                    'description': [
                        {
                            'type': 'text',
                            'content': 'conteudo da tag'
                        },
                        {
                            'type': 'image',
                            'content': 'url da imagem'
                        },
                        {
                            'type': 'links',
                            'content': ['urls dos links', ...]
                        }
                    ]
                }
            }

#scrapy shell https://revistaautoesporte.globo.com/rss/ultimas/feed.xml