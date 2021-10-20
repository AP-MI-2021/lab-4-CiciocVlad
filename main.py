def read():
    # citeste o lista de numere separate prin spatiu
    # return: lista de floats
    numere = input('lista numere: ')
    return [float(x) for x in numere.split(' ')]


def partea_intreaga(lista):
    # param: lista - o lista de float
    # return: o lista formata din partea intreaga a elementelor din lista initiala
    return list(map(int, lista))


def test_partea_intreaga():
    # functie de test pentru partea_intreaga
    assert partea_intreaga([1.3, 3.4, 14.2, -8.9]) == [1, 3, 14, -8]
    assert partea_intreaga([-6, -9.4, 10.0]) == [-6, -9, 10]
    assert partea_intreaga([5, -4]) == [5, -4]


def apartenenta(lista, low, high):
    # param: lista - o lista de float
    # param: low - limita inferioara (float)
    # param: high - limita superioara (float)
    # return: numerele din lista care apartin intervalului deschis (low, high)
    return list(filter(lambda x: x > low and x < high, lista))


def test_apartenenta():
    # functie de test pentru apartenenta
    assert apartenenta([1, 2, 3, 4, 5, 6, 7], 2, 7) == list(range(3, 7))
    assert apartenenta([-10, -4.5, -3.2, 6, 5], -4, 7) == [-3.2, 6, 5]
    

def partea_intreaga_divizor(lista):
    # param: lista - lista de float
    # return: o lista formata doar din numerele la care partea intreaga este divizor al partii fractionare
    return list(filter(lambda x: int(str(x).split('.')[1]) % int(x) == 0 and int(x) != x, lista))


def test_partea_intreaga_divizor():
    # functie test pentru partea_fractionara_divizor
    assert partea_intreaga_divizor([8.8, -3.3, 8.9]) == [8.8, -3.3]
    assert partea_intreaga_divizor([3.9, 2.3, 2.4, 1.5]) == [3.9, 2.4, 1.5]


def turn_to_string(lista):
    # param: lista - lista de float
    # return: lista formata din string-uri care descriu caracter cu caracter elementele din lista initiala
    objects = {'-': 'minus', '.': 'virgula', '1': 'unu', '2': 'doi', '3': 'trei',
    '4': 'patru', '5': 'cinci', '6': 'sase', '7': 'sapte', '8': 'opt', '9': 'noua', '0': 'zero'}
    return list(map(lambda x: ''.join(map(lambda y: objects[y], str(x if x != int(x) else int(x)))), lista))


def test_turn_to_string():
    # functie test pentru turn_to_string
    assert turn_to_string([1.1, -2.3, 14]) == ['unuvirgulaunu', 'minusdoivirgulatrei', 'unupatru']
    assert turn_to_string([11]) == ['unuunu']


def menu():
    # print menu
    # return: a string representing desired option
    print('1. citire floats')
    print('2. parte intreaga')
    print('3. apartenenta la interval')
    print('4. partea intreaga este divizor la partea fractionara')
    print('5. inlocuire cu string')
    print('6. exit')
    return input('your option: ')


def main():
    # main function
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
            print(partea_intreaga_divizor(lista))
        elif option == '5':
            print(turn_to_string(lista))
        else:
            print('invalid option...')


if __name__ == '__main__':
    test_partea_intreaga()
    test_apartenenta()
    test_partea_intreaga_divizor()
    test_turn_to_string()
    main()
