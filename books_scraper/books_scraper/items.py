import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags
from books_scraper.spiders.clean_functions import (
    clean_special_characters, clean_spaces, clean_uper, clean_price_characters
)


class BooksScraperItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(remove_tags, clean_special_characters,
                                                   clean_uper, clean_spaces),
                        output_processor=TakeFirst())
    author = scrapy.Field(input_processor=MapCompose(remove_tags, clean_special_characters,
                                                     clean_uper, clean_spaces),
                          output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags, clean_price_characters),
                         output_processor=TakeFirst())
    link = scrapy.Field(input_processor=MapCompose(), output_processor=TakeFirst())
    website = scrapy.Field()
    