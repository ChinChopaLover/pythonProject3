Rome_number = input("Enter rome number: ")

Arabic_number = []

Rome_equals_arabic = {
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

for iteration in range(len(Rome_number)):

    if Rome_number[iteration] in Rome_equals_arabic.keys():

        Arabic_number.append(Rome_equals_arabic[Rome_number[iteration]])

    else:

        print("You enter wrong number")

for i in range(len(Arabic_number) - 1):

    if Arabic_number[i] < (Arabic_number[i+1]):

        Arabic_number[i] = - Arabic_number[i]

        i += 1

print("Eqal arabic number is:",sum(Arabic_number))





