# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GraniceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    zemlja = scrapy.Field()
    ulazak = scrapy.Field()
    opis = scrapy.Field()
    azurirano = scrapy.Field()
