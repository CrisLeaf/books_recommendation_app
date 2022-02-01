import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def clean_spaces(string):
    string = string.replace("\n\r", " ")
    string = string.replace("\r\n", " ")
    string = string.replace("\n", " ")
    string = string.replace("\t", " ")
    string = string.replace("\r", " ").strip()
    return string

def clean_uper(string):
    return string.lower()

def clean_price_characters(value):
    value = value.replace("$", "")
    value = value.replace(",", "")
    value = value.replace(".", "").strip()
    return value

class BooksScraperItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(remove_tags, clean_uper, clean_spaces),
                        output_processor=TakeFirst())
    author = scrapy.Field(input_processor=MapCompose(remove_tags, clean_uper, clean_spaces),
                          output_processor=TakeFirst())
    description = scrapy.Field(input_processor=MapCompose(remove_tags, clean_uper, clean_spaces),
                               output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags, clean_price_characters),
                         output_processor=TakeFirst())
    link = scrapy.Field(input_processor=MapCompose(), output_processor=TakeFirst())
    website = scrapy.Field()