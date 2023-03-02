import sqlite3
import requests
import aiohttp
import asyncio

DB_NAME = 'lorem.db'

def create_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS lorem_ipsum
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  text TEXT)''')
    conn.commit()
    conn.close()

def save_text(text):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO lorem_ipsum (text) VALUES (?)", (str(text),))
    conn.commit()
    conn.close()

def get_texts():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM lorem_ipsum")
    rows = c.fetchall()
    conn.close()
    return rows


async def retrieve_lorem_texts(url, num_texts):

    async with aiohttp.ClientSession() as session:
        texts = []

        for _ in range(num_texts):
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    texts.append(data['text'])
                else:
                    print(f'Error: Failed to generate Lorem Ipsum text, status code: {response.status}')
    return texts


