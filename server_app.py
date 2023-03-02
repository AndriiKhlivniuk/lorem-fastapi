from fastapi import FastAPI
from lorem_text import lorem
import asyncio
import random

app = FastAPI()

async def generate_lorem_ipsum(paragraphs, words_count):
    for _ in range(paragraphs):
        words = lorem.paragraph().split()
        while len(words) < words_count:
            words.extend(lorem.paragraph().split())
        yield ' '.join(words[:words_count])

async def generate_text(paragraphs, words):
    if paragraphs<0 or words<0:
        return {'Invalid input'}
    texts = []
    async for text in generate_lorem_ipsum(paragraphs, words):
        texts.append(text)
    return {'text': texts}

@app.get('/lorem/{paragraphs}/{words}')
async def get_text(paragraphs: int, words: int):    
    return await generate_text(paragraphs, words)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
