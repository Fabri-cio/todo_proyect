#!/usr/bin/env python3
import time
import os
import psycopg2

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

while True:
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        conn.close()
        break
    except:
        print("Esperando a PostgreSQL...")
        time.sleep(1)

os.system("python manage.py migrate")
os.system("python manage.py runserver 0.0.0.0:8000")
