from flask import Flask, request
from datetime import datetime
from html import escape
from random import randint

app = Flask(__name__)


@app.route('/')
def my_main():
    return '<a href="./whoami">whoami</a><br />' \
           '<a href="./source_code">source_code</a><br />' \
           '<a href="./random?length=42&specials=1&digits=0">random</a><br />' \
           'Homework 4 Flask Application'


@app.route('/whoami')
def my_whoami():
    ip_address: str = str(request.remote_addr)
    user_agent: str = str(request.headers.get('User-Agent'))
    server_time: str = str(datetime.now().strftime('%H:%M:%S'))

    return f'<a href="./">&lt;--- back...</a><br />' \
           f'Your ip: {ip_address}<br />' \
           f'Your browser: {user_agent}<br />' \
           f'Server time: {server_time}'


@app.route('/source_code')
def my_source_code():
    with open(__file__, 'r') as fr:
        lines_file = fr.readlines()
    code_of_script = escape("".join(lines_file))

    return f'<a href="./">&lt;--- back...</a><br />' \
           f'<pre>{code_of_script}</pre>'


@app.route('/random')
def my_random():
    try:
        length: int = int(request.values.get('length', 0))
    except Exception:
        length = 0
    try:
        specials: int = int(request.values.get('specials', 0))
    except Exception:
        specials = 0
    try:
        digits: int = int(request.values.get('digits', 0))
    except Exception:
        digits = 0

    english_sym: str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    spec_sym: str = '!"№;%:?*()_+'
    digits_sym: str = '0123456789'
    result: str = 'Error: incorrect data or length out of range'

    if 0 < length <= 100:
        if specials != 0:
            specials = 1
            english_sym += spec_sym
        if digits != 0:
            digits = 1
            english_sym += digits_sym
        result = ''
        for i in range(length):
            result += english_sym[randint(0, len(english_sym)-1)]

    return f'<a href="./">&lt;--- back...</a><br />' \
           f'Generated dataset: [{english_sym}]<br />' \
           f'Length_of_str: {length}<br />' \
           f'Special_characters: {bool(specials)}<br />' \
           f'Include_the_numbers: {bool(digits)}<br /><br />' \
           f'Result: {result}'


app.run(debug=True)
