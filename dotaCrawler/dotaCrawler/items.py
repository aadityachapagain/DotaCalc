# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Heros(scrapy.Item):
    type = ['Strength', 'Agility', 'Intelligence']
    name = scrapy.Field()
    img_link = scrapy.Field()
    ability = scrapy.Field()
    Roles = scrapy.Field()
    Bad_against = scrapy.Field()
    Good_against = scrapy.Field()
    Work_well_with = scrapy.Field()

