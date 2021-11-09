def say_hi(lang):
    if lang == 'es':
        print('¡Hola!')
    elif lang == 'pl':
        print('Siemka!')
    elif lang == 'fr':
        print('Bonjour!')
    elif lang == 'en':
        print('Hello!')
    else:
        print('🙊')


say_hi('es')
say_hi('pl')
say_hi('fr')
say_hi('en')
say_hi('xx')
