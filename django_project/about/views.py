from django.http import HttpResponse
from datetime import datetime
from html import escape
from django.shortcuts import render


def main(request):
    return HttpResponse("""
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title> ABOUT PAGE </title>
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
    ABOUT PAGE<br />
    <a href="/"> <- MAIN PAGE </a><br />
    <a href="whoami/"> WHOAMI -> </a><br />
    <a href="source_code/"> SOURCE_CODE -> </a>
    </p>
</body>
</html>
    """)


def whoami(request):
    user_agent: str = str(request.headers.get('User-Agent'))
    ip_address: str = str(request.META.get('REMOTE_ADDR'))
    # ip_address: str = '8.8.8.8'
    server_time: str = str(datetime.now().strftime('%H:%M:%S'))
    return HttpResponse("""
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title> WHOAMI PAGE </title>
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
    WHOAMI PAGE<br />
    <a href="/about/"> <- ABOUT PAGE </a><br />
    Your browser: <b>""" + user_agent + """</b><br />
    Your ip address: <b>""" + ip_address + """</b><br />
    Server time: <b>""" + server_time + """</b>
    </p>
</body>
</html>
    """)


def source_code(request):
    with open(__file__, 'r') as fr:
        lines_file = fr.readlines()
    code_of_script = escape("".join(lines_file))
    return HttpResponse("""
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title> SOURCE_CODE PAGE </title>
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
    SOURCE_CODE PAGE<br />
    <a href="/about/"> <- ABOUT PAGE </a><br />
<pre>""" + code_of_script + """</pre>
    </p>
</body>
</html>
    """)
