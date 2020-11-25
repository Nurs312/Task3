# while True:
#     msg = input('Напишите "Привет" что бы продолжить.')
#     if msg == 'привет':
off_lis = {
    1: 'google_kazakstan.txt',
    2: 'google_paris.txt',
    3: 'google_uar.txt',
    4: 'google_kyrgystan.txt',
    5: 'google_san_francisco.txt',
    6: 'google_germany.txt',
    7: 'google_moscow.txt',
    8: 'google_sweden.txt'
}
choice = input(f"""Привет. Выберите сервер: \n'1)google_kazakstan.txt',
    '2)google_paris.txt',
    '3)google_uar.txt',
    '4)google_kyrgystan.txt',
    '5)google_san_francisco.txt',
    '6)google_germany.txt',
    '7)google_moscow.txt',
    '8)google_sweden.txt'
: """)
complaint = input('Напишите ваш отзыв: ')
for k, v in off_lis.items():
    try:
        if int(choice) == k:
            with open(f'{v}', 'a') as file:
                file.writelines(complaint)
    except ValueError:
        if choice == v:
            with open(f'{v}', 'a') as file:
                file.writelines(complaint)
