import os
import psycopg2

url = "dbname='SendIT' host='localhost'\
                port='5432' user='postgres' password='1234'"
                
db_url = os.getenv('DATABSE_URL')               
con = psycopg2.connect(url)
cur = con.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS users(
    userID serial PRIMARY KEY,
    name varchar(50) NOT NULL,
    email varchar(40) NOT NULL,
    password varchar(80) NOT NULL,
    role varchar(10) NOT NULL
)
""")

cur.execute(""" CREATE TABLE IF NOT EXISTS orders(
    parcelID serial PRIMARY KEY,
    sender_name varchar(50) NOT NULL,
    sender_email varchar(40) NOT NULL,
    pick_up varchar(150) NOT NULL,
    drop_off varchar(150) NOT NULL,
    recipient_name varchar(50) NOT NULL,
    weight int NOT NULL,
    cost int NOT NULL,
    status varchar(40) NOT NULL,
    current_location varchar(150) NOT NULL
)
""")

con.commit()

