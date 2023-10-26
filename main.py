def roman_to_int(num: str) -> int:

    arabic_number = []

    rome_equals_arabic = {
        'I': 1,
        'i': 1,
        'V': 5,
        'v': 5,
        'X': 10,
        'x': 10,
        'L': 50,
        'l': 50,
        'C': 100,
        'c': 100,
        'D': 500,
        'd': 500,
        'm': 1000,
        'M': 1000,
    }

    for iteration in range(len(num)):

        if num[iteration] in rome_equals_arabic.keys():

            arabic_number.append(rome_equals_arabic[num[iteration]])

        else:

            return -1

    for i in range(len(arabic_number) - 1):

        if arabic_number[i] < (arabic_number[i+1]):

            arabic_number[i] = - arabic_number[i]

            i += 1

    return sum(arabic_number)


print(roman_to_int(num=input("Enter rome number: ")))
