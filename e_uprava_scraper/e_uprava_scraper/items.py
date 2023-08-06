# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OpenAppointmentItem(scrapy.Item):
    date = scrapy.Field()
    location = scrapy.Field()
    time = scrapy.Field()
