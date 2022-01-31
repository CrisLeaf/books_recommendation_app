import scrapy
from books_scraper.items import BooksScraperItem
from scrapy.loader import ItemLoader
from books_scraper.spiders.urls import categories_urls


class FeriachilenaSpider(scrapy.Spider):
	name = "feriachilena"
	start_urls = ["https://feriachilenadellibro.cl/categoria-producto/arquitectura-y-urbanismo/"]
	
	def parse(self, response, **kwargs):

		for book in response.xpath(".//div[@class='astra-shop-summary-wrap']"):
			item_link = book.xpath(".//a[@class='ast-loop-product__link']/@href").get()
			yield response.follow(url=item_link, callback=self.parse_item)
			
		try:
			next_page = response.xpath(".//a[@class='next page-numbers']/@href").get()
		except:
			next_page = None
			
		if next_page is not None:
			yield response.follow(url=next_page, callback=self.parse)
	
	def parse_item(self, response):
		loader = ItemLoader(item=BooksScraperItem(), selector=response)
		loader.add_xpath("name", ".//h1[@class='product_title entry-title']/text()")
		loader.add_xpath("author", ".//div[@class='woocommerce-product-details__short-description']/p")
		loader.add_xpath("link", "head/link[@rel='canonical']/@href")
		loader.add_xpath("price", ".//p[@class='price']/span/bdi/text()")
		loader.add_value("website", "feriachilena")
		
		yield loader.load_item()