from django.http import HttpResponse
from random import randint
from django.shortcuts import render


def my_random(request):
    try:
        # length: int = int(request.values.get('length', 0))
        length: int = int(request.GET.get("length"), 0)
    except Exception:
        length = 0
    try:
        # specials: int = int(request.values.get('specials', 0))
        # specials: int = int(request.values.get('specials', 0))
        specials: int = int(request.GET.get("specials"), 0)
    except Exception:
        specials = 0
    try:
        # digits: int = int(request.values.get('digits', 0))
        # digits: int = int(request.values.get('digits', 0))
        digits: int = int(request.GET.get("digits"), 0)
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
            result += english_sym[randint(0, len(english_sym) - 1)]
    return HttpResponse("""
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title> RANDOM PAGE </title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Ubuntu+Mono&display=swap" rel="stylesheet">
        <style>
        * {
            font-family: 'Ubuntu Mono', monospace;
        }
        a:link, a:active, a:visited {
            text-decoration: none;
            color: #000000;
        }
        a:hover {
            text-decoration: underline;
            color: #0000FF;
        }
        </style>
    </head>
<body>
    <p align="center">
    RANDOM PAGE<br />
    <a href="/"> <- MAIN PAGE </a><br />
    Generated dataset: <b>""" + english_sym + """</b><br />
    Length of str: <b>""" + str(length) + """</b><br />
    Special characters: <b>""" + str(bool(specials)) + """</b><br />
    Include the numbers: <b>""" + str(bool(digits)) + """</b><br />
    Result: <b>""" + result + """</b>
    </p>
</body>
</html>
    """)
