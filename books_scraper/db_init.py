import psycopg2
from secrets import psql_params
from websites_names import websites


def reset_tables():
	init_commands = (
		"""
		DROP TABLE IF EXISTS books
		""",
		"""
		DROP TABLE IF EXISTS websites
		""",
		"""
		CREATE TABLE websites (
			website_id SERIAL PRIMARY KEY,
			name TEXT,
			url TEXT
		)
		""",
		"""
		CREATE TABLE books (
			book_id SERIAL PRIMARY KEY,
			name TEXT NOT NULL,
			author TEXT NOT NULL,
			description TEXT,
			price INT,
			link TEXT,
			website_id INT,
			CONSTRAINT website_id FOREIGN KEY (website_id) REFERENCES websites (website_id)
		)
		"""
	)
	
	conn = psycopg2.connect(**psql_params)
	curr = conn.cursor()
	
	for command in init_commands:
		curr.execute(command)
	
	for name, url in websites.items():
		curr.execute("INSERT INTO websites (name, url) VALUES (%s, %s)",
					 (name, url))
			
	print("Base de datos creada!")
	
	conn.commit()
	curr.close()
	conn.close()


if __name__ == "__main__":
	reset_tables()