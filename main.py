from random import randint
from datetime import datetime
from fastapi import FastAPI, Request
from typing import Optional
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates/')


@app.get('/')
async def home(req: Request):
    return templates.TemplateResponse('home.html', context={
        'request': req,
        'active_page': 'home',
        'name_app': 'Homework 15 FastApi App',
        'link': {
            'whoami': '/whoami/',
            'source_code': '/source_code/',
            'random': '/random/?length=42&specials=1&digits=0',
        }
    })


@app.get('/whoami/')
async def whoami(req: Request):
    user_agent: str = str(req.headers.get('User-Agent'))
    ip_address: str = str(req.client.host)
    server_time: str = str(datetime.now().strftime('%Y.%m.%d %H:%M:%S'))
    return templates.TemplateResponse('whoami.html', context={
        'request': req,
        'active_page': 'whoami',
        'user_agent': user_agent,
        'ip_address': ip_address,
        'server_time': server_time,
    })


@app.get('/source_code/')
async def source_code(req: Request):
    with open(__file__, 'r') as fr:
        lines_file = fr.readlines()
    lines_of_code: list = [line.replace('\n', '') for line in lines_file]
    return templates.TemplateResponse('source_code.html', context={
        'request': req,
        'active_page': 'source_code',
        'lines_of_code': lines_of_code,
    })


@app.get('/random/')
async def random(length: Optional[int] = 16, specials: Optional[int] = 0,
                 digits: Optional[int] = 1, req: Request = None):
    char_set: str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    spec_sym: str = '!"№;%:?*()_+'
    digits_sym: str = '0123456789'
    result: str = ''
    if length > 100 or length <= 0:
        length = 16
    if specials != 0:
        specials = 1
        char_set += spec_sym
    if digits != 0:
        digits = 1
        char_set += digits_sym
    for i in range(length):
        result += char_set[randint(0, len(char_set) - 1)]
    return templates.TemplateResponse('random.html', context={
        'request': req,
        'active_page': 'random',
        'length': length,
        'specials': specials,
        'digits': digits,
        'result': result,
    })
