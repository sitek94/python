file_name = None

while True:
    file_name = input('Enter file name: ')

    if file_name == 'exit':
        print('Exiting...')
        print('See you! 👋')
        quit()

    file_handle = None

    try:
        file_handle = open(file_name)
    except FileNotFoundError:
        print('File "' + file_name + '" does not exist! 💣')
        print('Try again!')
        continue

    count = 0
    for line in file_handle:
        print(line.rstrip())
        count += 1

    print('There were', count, 'lines in "' + file_name + '" file.')
