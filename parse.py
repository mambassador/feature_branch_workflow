from urllib.parse import urlparse, parse_qsl, ParseResult
import re


def parse(query: str) -> dict:
    """Returns a dictionary that contains URL query parameters
    and their values

    Args:
        query(str): The URL that need to be parsed

    Returns:
        parsed_query(dict): query parameters extracted from the URL

    Parameter values that contain addition between two integers
    are interpreted as expression string with '%2B'
    instead of the '+' symbol

    Parameter values which are integers, lists, booleans and none
    are interpreted as Integer, List, Boolean, and None types

    If there are no any query parameters, then an empty dict
    will be returned
    """

    search_add = "".join(re.findall(r'\d+\+\d+', query))
    if search_add:
        query = query.replace('+', '%2B')

    if query.endswith('&'):
        query = query[:-1]

    parsed_url: ParseResult = urlparse(query)

    if not parsed_url.query:
        return {}

    parsed_query = dict(parse_qsl(parsed_url.query,
                                  keep_blank_values=True,
                                  strict_parsing=True))

    for param in parsed_query.keys():
        if parsed_query[param].isnumeric():
            parsed_query[param] = int(parsed_query[param])

        elif parsed_query[param].startswith('[') and parsed_query[param].endswith(']'):
            parsed_query[param] = parsed_query[param][1:-1].split(',')

        elif parsed_query[param].lower() in ('true', 'false'):
            bool_converter = {
                                'true': True, 'false': False,
                                'True': True, 'False': False
                             }
            parsed_query[param] = bool_converter.get(parsed_query[param])

        elif parsed_query[param].lower() in ('none', 'null'):
            parsed_query[param] = None

    return parsed_query
