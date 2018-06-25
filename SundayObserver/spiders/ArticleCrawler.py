# -*- coding: utf-8 -*-
import scrapy
from SundayObserver.items import SummaryArticleItem


class ArticlecrawlerSpider(scrapy.Spider):
    name = 'ArticleCrawler'
    allowed_domains = ['sundayobserver.lk']

    def start_requests(self):
        start_urls = ['http://sundayobserver.lk/', "http://www.sundayobserver.lk/news",
                      "http://www.sundayobserver.lk/sections/issues-0",
                      "http://www.sundayobserver.lk/sections/opinion", "http://www.sundayobserver.lk/editorial",
                      "http://www.sundayobserver.lk/columns",
                      "http://www.sundayobserver.lk/world", "http://www.sundayobserver.lk/sports",
                      "http://www.sundayobserver.lk/business",
                      "http://www.sundayobserver.lk/features", "http://www.sundayobserver.lk/spectrum",
                      "http://www.sundayobserver.lk/junior"]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)



    def parse_article(self, response):
        print("")

    def parse(self, response):

        item = SummaryArticleItem()
        item["image"] = response.css("div.views-field.views-field-field-image "
                                     "div.field-content a img::attr(src)").extract()
        item["title"] = response.css("div.views-field.views-field-title "
                                     "span.field-content a::text").extract()
        item["title_byline"] = response.css('div.views-field.views-field-field-title-byline '
                                            'div.field-content::text').extract()
        item["body"] = response.css('div.views-field.views-field-body span.field-content::text').extract()
        item["date"] = response.css('div.views-field.views-field-nothing '
                                    'span.field-content span.pdate::text').extract()
        item["comments"] = response.css('div.views-field.views-field-nothing '
                                        'span.field-content span.ccount::text').extract()
        item["link"] = response.css('div.views-field.views-field-title span.field-content a::attr(href)').extract()

        return item