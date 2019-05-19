# -*- coding: utf-8 -*-
import scrapy
from parsel import Selector
'''
from lxml.etree import XMLParser
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import XmlXPathSelector
from Dell.items import DellItem
from scrapy.http.request import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CSVFeedSpider
import scrapy.spiders
'''


class InfogloboSpider(scrapy.Spider):
    name = 'infoglobo'
    allowed_domains = ['revistaautoesporte.globo.com']
    start_urls = ['https://revistaautoesporte.globo.com/rss/ultimas/feed.xml']

    def parse(self, response):
        for item in response.xpath("//item"):
            title = item.xpath("//title/text()").extract_first()
            link = item.xpath("//link/text()").extract_first()
            #seletor da html contido em description
            sel = Selector(item.xpath("//description/text()").extract_first())
            # get cotent and link
            desc_content = sel.xpath("//p").getall()
            #fazer um for aqui para gerar igual ao exemplo quando voltar
            link_img_desc = sel.xpath("//div/img/@src").getall()
            link_a_desc = sel.xpath("//div/ul//li/a/@href").getall()

            return {
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
            }

#scrapy shell https://revistaautoesporte.globo.com/rss/ultimas/feed.xml
#scrapy runspider crawler\spiders\infoglobo.py -o infoglobo.json