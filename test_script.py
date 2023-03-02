import subprocess
import time
from client_app import *
import asyncio

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000
SERVER_URL = f'http://{SERVER_HOST}:{SERVER_PORT}/lorem/'
SERVER_PROCESS = None

def start_server():
    global SERVER_PROCESS
    SERVER_PROCESS = subprocess.Popen(['uvicorn', 'server_app:app', '--host', SERVER_HOST, '--port', str(SERVER_PORT)])
    time.sleep(3)

def stop_server():
    global SERVER_PROCESS
    SERVER_PROCESS.terminate()
    SERVER_PROCESS.wait()
    SERVER_PROCESS = None

def main(paragraphs_num, words_num,  texts_num):
    global SERVER_URL
    SERVER_URL = SERVER_URL+str(paragraphs_num)+"/"+str(words_num)
    try:
        start_server()
        create_table()
        texts = asyncio.run(retrieve_lorem_texts(SERVER_URL,texts_num))
        save_text(texts)
        rows = get_texts()
        print(rows)
    finally:
        stop_server()

if __name__ == '__main__':
    parameters = {
        "paragraphs":1,
        "words":2,
        "texts":100
    }

    main(parameters["paragraphs"],parameters["words"],parameters["texts"])
