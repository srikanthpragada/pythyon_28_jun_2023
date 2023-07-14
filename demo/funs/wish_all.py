def wish(*names, msg='Hi'):
    for n in names:
        print(msg, n)


wish('Scott', 'Mark', 'Tom', msg='Hello')
wish('Bill', "Larry")
