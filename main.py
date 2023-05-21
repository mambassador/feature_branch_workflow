from parse_cookie import parse_cookie

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
