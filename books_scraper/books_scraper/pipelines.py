# import psycopg2
# from datetime import date
# from secrets import psql_params
#
#
# class BooksScraperPipeline(object):
#
#     def open_spider(self, spider):
#         try:
#             self.connection = psycopg2.connect(**psql_params)
#         except:
#             raise ConnectionError("Unable to connect to database.")
#
#         self.cursor = self.connection.cursor()
#
#     def close_spider(self, spider):
#         self.cursor.close()
#         self.connection.close()
#
#     def process_item(self, item, spider):
#         pass