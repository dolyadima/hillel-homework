class Url:
    """ Base class for Url"""

    def __init__(self, scheme='', authority='', path=None, query=None, fragment=''):
        self.scheme: str = scheme
        self.authority: str = authority
        self.path: list = path
        self.query: dict = query
        self.fragment: str = fragment

    def __eq__(self, other):
        return self.__str__() == str(other)

    def __str__(self):
        self.final_url: str = ''

        if self.scheme != '':
            self.final_url += self.scheme + '://'

        if self.authority != '':
            self.final_url += self.authority

        if self.path is not None and \
                isinstance(self.path, list) and \
                len(self.path) > 0:
            self.final_url += '/' + '/'.join(self.path)

        if self.query is not None and \
                isinstance(self.query, dict) and \
                len(self.query) > 0:
            self.final_url += '?'
            for key, value in self.query.items():
                self.final_url += f'{key}={value}&'
            self.final_url = self.final_url[:-1]

        if self.fragment != '':
            self.final_url += '#' + self.fragment

        return self.final_url


class HttpsUrl(Url):
    """ class Https Url """

    def __init__(self, authority='', path=None, query=None, fragment=''):
        super().__init__('https', authority, path, query, fragment)


class HttpUrl(Url):
    """ class Http Url """

    def __init__(self, authority='', path=None, query=None, fragment=''):
        super().__init__('http', authority, path, query, fragment)


class GoogleUrl(HttpsUrl):
    """ class Https Google """

    def __init__(self, path=None, query=None, fragment=''):
        super().__init__('google.com', path, query, fragment)


class WikiUrl(HttpsUrl):
    """ class Https Wikipedia """

    def __init__(self, path=None, query=None, fragment=''):
        super().__init__('wikipedia.org', path, query, fragment)


assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'
