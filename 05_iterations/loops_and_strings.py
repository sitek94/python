def spell_banana():
    print('Spelling "banana":')
    banana = 'banana'
    index = 0
    while index < len(banana):
        print(banana[index])
        index += 1


spell_banana()


def spell_cookies():
    print('Spelling "cookies":')
    for letter in 'cookies':
        print(letter)


spell_cookies()


def print_and_count_vowels(word):
    all_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0

    print('Vowels in word "' + word + '"')

    for letter in word:
        if letter in all_vowels:
            print(letter)
            count += 1

    print('Count:', count)


print_and_count_vowels('mercedes')
