import psycopg2
import os


class BooksScraperPipeline(object):
    
    def open_spider(self, spider): # <- spider parameters is needed
        try:
            self.connection = psycopg2.connect(host=os.environ["DATABASE_HOST"],
                                               user=os.environ["DATABASE_USER"],
                                               password=os.environ["DATABASE_PASSWORD"],
                                               dbname=os.environ["DATABASE_NAME"])
        except:
            raise ConnectionError("Unable to connect to database.")
        
        self.cursor = self.connection.cursor()
    
    def close_spider(self, spider): # <- spider parameters is needed
        self.cursor.close()
        self.connection.close()
    
    def process_item(self, item, spider): # <- spider parameters is needed
        try:
            self.cursor.execute("SELECT website_id FROM websites WHERE name=%s",
                                (item["website"][0], ))
            website_id = self.cursor.fetchall()[0][0]

            self.cursor.execute(
                "INSERT INTO books (name, author, description, price, link, website_id) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (item["name"], item["author"], item["description"], int(item["price"]),
                 item["link"], website_id)
            )
            self.connection.commit()
        
        except:
            self.connection.rollback()
            raise
        return item