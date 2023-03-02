# lorem-fastapi

<h2>Start application</h2><br>
<ul>
<li>pip3 install -r requirements.txt </li>

<li>In order to change words, paragraphs and texts count, change variable "parameters" in main function of test_script.py file.</li>

<li>python3 test_script.py  (this will: 1. start the server 2. client send request to the server  3. server generate lorem text with given parameters 4. client save texts to db 5. get all texts from the db)</li>

</ul>
<h2>Run tests</h2><br>
pytest test_lorem.py (this will test: client - save text to db, get text from db. server - generate text with valid input, generate text with invalid input)