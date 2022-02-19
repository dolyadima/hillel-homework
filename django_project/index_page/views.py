from django.http import HttpResponse
from django.shortcuts import render


def index_page(request):
    return HttpResponse("""
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title> MAIN PAGE </title>
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
    MAIN PAGE<br />
    <a href="/about/"> ABOUT -> </a><br />
    <a href="/random/?length=16&specials=0&digits=1"> RANDOM -> </a><br /><br />
    
    <a href="/admin/"> (ADMIN) </a>
    </p>
</body>
</html>
    """)
