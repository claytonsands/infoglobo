# -*- coding: utf-8 -*-
import scrapy
from parsel import Selector


class InfogloboSpider(scrapy.Spider):
    name = 'infoglobo'
    allowed_domains = ['revistaautoesporte.globo.com']
    start_urls = ['https://revistaautoesporte.globo.com/rss/ultimas/feed.xml']

    def parse(self, response):
        vet = []
        for x in range(0, len(response.xpath("//item"))):
            title = response.xpath("//item/title/text()")[x].get()
            link = response.xpath("//item/link/text()")[x].get()
            #seletor da html contido em description
            sel = Selector(response.xpath("//item/description/text()")[x].get())
            # get cotent and link
            desc_content = sel.xpath("//p").getall()
            #fazer um for aqui para gerar igual ao exemplo quando voltar
            link_img_desc = sel.xpath("//div/img/@src").getall()
            link_a_desc = sel.xpath("//div/ul/li/a/@href").getall()

            vet.append({
                    'item': {
                        'title': title,
                        'link': link,
                        'description': [
                            {
                                'type': 'text',
                                'content': desc_content
                            },
                            {
                                'type': 'image',
                                'content': link_img_desc
                            },
                            {
                                'type': 'links',
                                'content': link_a_desc
                            }
                        ]
                    }
            })
        return {'feed': vet}

#scrapy shell https://revistaautoesporte.globo.com/rss/ultimas/feed.xml
#scrapy runspider crawler\spiders\infoglobo.py -o infoglobo.json