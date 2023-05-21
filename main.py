from parse import parse
from parse_cookie import parse_cookie


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse('http://example.com?name=John&age=15') == {'name': 'John', 'age': 15}
    assert parse('http://example.com?name=John&surname=Doe&age=') == {'name': 'John', 'surname': 'Doe', 'age': ''}
    assert parse('http://example.com?name=John&surname=&age=15') == {'name': 'John', 'surname': '', 'age': 15}
    assert parse('http://example.com?name=John&alive=false') == {'name': 'John', 'alive': False}
    assert parse('http://example.com?name=John&alive=true') == {'name': 'John', 'alive': True}
    assert parse('http://example.com?name=none&age=15&') == {'name': None, 'age': 15}

    assert parse('http://example.com/?fullname=John%20Doe&address=Kyiv%2fUkraine') == {
                 'fullname': 'John Doe', 'address': 'Kyiv/Ukraine'
                 }

    assert parse('http://example.com/?fullname=Apple%20Iphone&camera=48+12') == {
                 'fullname': 'Apple Iphone', 'camera': '48+12'
                 }

    assert parse('https://example.com/path?name=Branch&products=[Journeys,Email,Universal%20Ads]') == {
                 'name': 'Branch',
                 'products': ['Journeys', 'Email', 'Universal Ads']
                 }

    assert parse('http://example.com?name=John&age=15&skills=[python,django,flask]') == {
                 'name': 'John',
                 'age': 15,
                 'skills': ['python', 'django', 'flask']
                 }

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': 28}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': 28}

    assert parse_cookie('name=Dima=User;age=28;;;;;') == {'name': 'Dima=User', 'age': 28}
    assert parse_cookie('name=Dima=User;rate=$28') == {'name': 'Dima=User', 'rate': '$28'}
    assert parse_cookie('name=Dima=User;rate!=$28') == {'name': 'Dima=User', 'rate!': '$28'}
    assert parse_cookie('name=iphone;camera=48+2;') == {'name': 'iphone', 'camera': '48+2'}
    assert parse_cookie('?name=Dima&;children=none') == {'name': 'Dima&', 'children': None}

    assert parse_cookie('name=Dima=User;age=28;children=none') == {
                        'name': 'Dima=User', 'age': 28, 'children': None
                        }

    assert parse_cookie('name=Dima=User;age=28;alive=true') == {
                        'name': 'Dima=User', 'age': 28, 'alive': True
                        }

    assert parse_cookie('name=Dima=User;age=28;alive=False') == {
                        'name': 'Dima=User', 'age': 28, 'alive': False
                        }

    assert parse_cookie('name=Dima=User;system=os:linux,browser:chrome;') == {
                        'name': 'Dima=User',
                        'system': 'os:linux,browser:chrome'
                        }

    assert parse_cookie('fullname=John%20Doe;address=Kyiv%2fUkraine;') == {
                        'fullname': 'John Doe', 'address': 'Kyiv/Ukraine'
                        }
