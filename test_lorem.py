import pytest
from client_app import *
from server_app import *

def test_save_text():
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    save_text(text)
    rows = get_texts()
    assert text in rows[-1]

@pytest.mark.asyncio
async def test_generate_text():
    paragraphs = 5
    words = 2
    result = await generate_text(paragraphs, words)
    assert paragraphs == len(result['text'])
    for p in result['text']:
        assert len(p.split()) == words

@pytest.mark.asyncio
async def test_generate_text_invalid_paragraphs():
    paragraphs = -1
    words = 2
    result = await generate_text(paragraphs, words)
    assert 'Invalid input' in result
 


