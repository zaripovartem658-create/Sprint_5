class ValidData:
    user_name = 'Ильин Виталий'
    login = 'testtestov1999@yandex.ru'
    password = '123456'

class InvalidData:
    invalid_emails = [
        'test1@yanru', 'test2yan.ru', 'te st3@yan.ru', 'test4@ya n.ru',
        '@yan.ru', 'test6@.ru', 'test7@yan.'
    ]
    short_passwords = ['1', '12345']
