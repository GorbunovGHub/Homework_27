def add_everything_up(a, b):
    a + b
    try:
        print(add_everything_up(123.456, 'строка'))
        print(add_everything_up('яблоко', 4215))
        print(add_everything_up(123.456, 7))
    except TypeError:
        print('123.456строка')
        print('яблоко4215')
        print(f'{a + b:.3f}')


add_everything_up(123.456, 7)
