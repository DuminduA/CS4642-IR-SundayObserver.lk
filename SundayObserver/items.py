# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SundayobserverItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class FullArticleItem(scrapy.Item):
    image = scrapy.Field()
    title = scrapy.Field()
    title_byline = scrapy.Field()
    body = scrapy.Field()
    date = scrapy.Field()
    comments = scrapy.Field()
    link = scrapy.Field()
    author = scrapy.Field()

class SummaryArticleItem(scrapy.Item):
    image = scrapy.Field()
    title = scrapy.Field()
    title_byline = scrapy.Field()
    body = scrapy.Field()
    date = scrapy.Field()
    comments = scrapy.Field()
    link = scrapy.Field()

class EditorialItem(scrapy.Item):
    image = scrapy.Field()
    title = scrapy.Field()
    title_byline = scrapy.Field()
    body = scrapy.Field()
    date = scrapy.Field()
    comments = scrapy.Field()
    link = scrapy.Field()

