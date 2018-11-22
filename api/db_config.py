import os
import psycopg2

url = "dbname='TestSendIt' host='localhost' port='5432' user='postgres' password='1234'"

db_url = os.getenv('DATABSE_URL')               
con = psycopg2.connect(db_url)
cur = con.cursor()

class  DbConfig():
	
	def create_tables(self):
			cur.execute(""" CREATE TABLE IF NOT EXISTS users(
				userID serial PRIMARY KEY,
				name varchar(50) NOT NULL,
				email varchar(40) NOT NULL,
				password varchar(80) NOT NULL,
				role varchar(10) NOT NULL
			)
			""")
			con.commit()
			cur.execute(""" CREATE TABLE IF NOT EXISTS orders(
				parcelID serial PRIMARY KEY,
				sender_name varchar(50) NOT NULL,
				sender_email varchar(40) NOT NULL,
				pick_up varchar(150) NOT NULL,
				drop_off varchar(150) NOT NULL,
				recipient_name varchar(50) NOT NULL,
				weight varchar(10) NOT NULL,
				cost int NOT NULL,
				status varchar(40) NOT NULL,
				current_location varchar(150) NOT NULL
			)
			""")
			con.commit()
			return "Tables created"

	def destroy_tables(self):
		cur.execute("DROP TABLE IF EXISTS users CASCADE")
		con.commit()
		cur.execute("DROP TABLE IF EXISTS orders CASCADE")
		con.commit()
		return "Tables destroyed"



