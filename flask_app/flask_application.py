from flask import Flask, request, render_template
from datetime import datetime
from html import escape
from random import randint

app = Flask(__name__)


@app.route('/')
def my_main():
    return render_template('index.html', name='Main', active='main')


@app.route('/whoami/')
def my_whoami():
    ip_address: str = str(request.remote_addr)
    user_agent: str = str(request.headers.get('User-Agent'))
    server_time: str = str(datetime.now().strftime('%H:%M:%S'))
    return render_template('whoami.html',
                           name='Whoami',
                           active='whoami',
                           ip_ad=ip_address,
                           us_ag=user_agent,
                           se_ti=server_time)


@app.route('/source_code/')
def my_source_code():
    with open(__file__, 'r') as fr:
        lines_file = fr.readlines()
    code_of_script = escape("".join(lines_file))
    return render_template('source_code.html',
                           name='Source code',
                           active='source_code',
                           co_sc=code_of_script)


@app.route('/random/')
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
    return render_template('random.html',
                           name='Random',
                           active='random',
                           english_sym=english_sym,
                           length=length,
                           specials=bool(specials),
                           digits=bool(digits),
                           result=result)


app.run(debug=True, host='0.0.0.0')
