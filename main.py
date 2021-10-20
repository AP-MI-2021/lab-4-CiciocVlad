def read():
    numere = input('lista numere: ')
    return [float(x) for x in numere.split(' ')]


def partea_intreaga(lista):
    return list(map(int, lista))


def apartenenta(lista, low, high):
    return list(filter(lambda x: x > low and x < high, lista))


def partea_fractionara_divizor(lista):
    return list(filter(lambda x: int(str(x).split('.')[1]) % int(x) == 0 and int(x) != x, lista))


def turn_to_string(lista):
    objects = {'-': 'minus', '.': 'virgula', '1': 'unu', '2': 'doi', '3': 'trei',
    '4': 'patru', '5': 'cinci', '6': 'sase', '7': 'sapte', '8': 'opt', '9': 'noua', '0': 'zero'}
    return list(map(lambda x: ''.join(map(lambda y: objects[y], str(x if x != int(x) else int(x)))), lista))


def menu():
    print('1. citire floats')
    print('2. parte intreaga')
    print('3. apartenenta la interval')
    print('4. partea intreaga este divizor la partea fractionara')
    print('5. inlocuire cu string')
    print('6. exit')
    return input('your option: ')


def main():
    lista = []
    while (option := menu()) != '6':
        if option == '1':
            lista = read()
        elif option == '2':
            print(partea_intreaga(lista))
        elif option == '3':
            low = int(input('lower value: '))
            high = int(input('higher value: '))
            print(apartenenta(lista, low, high))
        elif option == '4':
            print(partea_fractionara_divizor(lista))
        elif option == '5':
            print(turn_to_string(lista))
        else:
            print('invalid option...')


if __name__ == '__main__':
    main()
