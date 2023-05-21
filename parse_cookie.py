from http.cookies import SimpleCookie
import urllib.parse


def parse_cookie(cookie_string: str) -> dict:
    """Returns a dictionary that contains cookie parameters
    and their values

    Args:
        cookie_string(str): the cookie that need to be parsed

    Returns:
        cookies(dict): cookies extracted from the cookie string

    If the cookie string contains the '?' symbol which is forbidden
    to use with cookies this symbol it will be deleted

    Parameter values which are integers, booleans and none
    are interpreted as Integer, Boolean, and None type

    If there are no any query parameters, then an empty dict
    will be returned

    Percent encoding is used for special characters
    or symbols that have reserved meanings in URLs
    """
    if '?' in cookie_string:
        cookie_string = cookie_string.replace('?', '')

    cookie = SimpleCookie()
    cookie.load(cookie_string)

    cookies = {k: v.value for k, v in cookie.items()}

    for param in cookies.keys():
        cookies[param] = urllib.parse.unquote(cookies[param])

        if cookies[param].isnumeric():
            cookies[param] = int(cookies[param])

        elif cookies[param].lower() in ('true', 'false'):
            bool_converter = {'true': True, 'false': False,
                              'True': True, 'False': False
                              }
            cookies[param] = bool_converter.get(cookies[param])

        elif cookies[param].lower() in ('none', 'null'):
            cookies[param] = None

    return cookies
