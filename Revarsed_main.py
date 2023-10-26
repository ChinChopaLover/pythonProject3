def int_to_roman(num: int) -> str:
    rome_number = []
    thousand = {
        1: 'M',
        2: 'MM',
        3: 'MMM',
        4: 'MMMM'
    }
    hundred = {
        1: 'C',
        2: 'CC',
        3: 'CCC',
        4: 'CD',
        5: 'D',
        6: 'DC',
        7: 'DCC',
        8: 'DCCC',
        9: 'CM'
    }
    tens = {
        1: 'X',
        2: 'XX',
        3: 'XXX',
        4: 'XL',
        5: 'L',
        6: 'LX',
        7: 'LXX',
        8: 'LXXX',
        9: 'XC'
    }
    ones = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX'
    }
    a_n_str = str(num)
    for i in range(len(a_n_str)):
        rome_number.append(a_n_str[i])
    if len(a_n_str) > 4:
        return "Out of range of numbers"
    if len(rome_number) == 4:
        rome_number[0] = thousand[int(rome_number[0])]
        rome_number[1] = hundred[int(rome_number[1])]
        rome_number[2] = tens[int(rome_number[2])]
        rome_number[3] = ones[int(rome_number[3])]
        solution = ''.join(rome_number)
        return solution
    elif len(rome_number) == 3:
        rome_number[0] = hundred[int(rome_number[0])]
        rome_number[1] = tens[int(rome_number[1])]
        rome_number[2] = ones[int(rome_number[2])]
        solution = ''.join(rome_number)
        return solution
    elif len(rome_number) == 2:
        rome_number[0] = tens[int(rome_number[0])]
        rome_number[1] = ones[int(rome_number[1])]
        solution = ''.join(rome_number)
        return solution
    else:
        rome_number[0] = ones[int(rome_number[0])]
        solution = ''.join(rome_number)
        return solution


print(int_to_roman(num=int(input('Etner number: '))))
