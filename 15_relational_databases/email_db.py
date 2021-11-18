import sqlite3
from get_yes_no_answer import get_yes_no_answer

connection = sqlite3.connect('email_db.sqlite')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Friends (email TEXT, name TEXT)')

while True:
    print('Add friends to the database!')
    friend_email = input('Enter email: ')
    friend_name = input('Enter name: ')

    try:
        cursor.execute('INSERT INTO Friends (email, name) VALUES (?, ?)', (friend_email, friend_name))
    except sqlite3.Error as error:
        print(error)

    shouldContinue = get_yes_no_answer('Add another one? (y/n): ', 'y', 'n')
    if shouldContinue:
        continue
    else:
        connection.commit()
        break

rows = cursor.execute('SELECT * FROM Friends')

for row in rows:
    print(row[0] + ' - ' + row[1])

cursor.close()
