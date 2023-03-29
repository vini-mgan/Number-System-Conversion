

number_o = input("Number to be converted: \n")

number_d = 0

base_o = int(input("Original  base: \n"))

base_d = int(input("Conversion base: \n"))

def hexa():

    if base_o == 16:

        for d in range(len(digit_list)):


            if digit_list[d] == 'A':
                digit_list[d] = '10'

            elif digit_list[d] == 'B':
                digit_list[d] = '11'

            elif digit_list[d] == 'C':
                digit_list[d] = '12'

            elif digit_list[d] == 'D':
                digit_list[d] = '13'

            elif digit_list[d] == 'E':
                digit_list[d] = '14'

            elif digit_list[d] == 'F':
                digit_list[d] = '15'


def naming(base):

    global base_name

    if base == 2:
        base_name = "binário"

    elif base == 8:
        base_name = "octal"

    elif base == 16:
        base_name = "hexadecimal"


if base_d == base_o:
    print("\nAs bases são iguais")

#CONVERSION FROM DECIMAL TO OTHER NUMBER SYSTEMS

elif base_o == 10:

    digit_list = [int(x) for x in str(number_o)]

    for p in range(len(digit_list)):

        number_d = number_d + digit_list[p]*base_o**p

    naming(base_d)

    print(f"\n{number_o} em decimal é igual a {number_d} em {base_name}")


#CONVERSION FROM OTHER NUMBER SYSTEMS TO DECIMAL

elif base_o != 10 and base_d == 10:

    digit_list = [str(x) for x in number_o]

    hexa()

    digit_list = digit_list[::-1]

    for p in range(len(digit_list)):

        digit_list[p] = int(digit_list[p])

        number_d = number_d + digit_list[p] * base_o**p


    naming(base_o)

    print (f"\n{number_o} em {base_name} é igual a {number_d} em decimal")


#CONVERSION BETWEEN BINARY, OCTAL AND HEXADECIMAL

elif base_o != 10 and base_d != 10:

    digit_list = [str(x) for x in str(number_o)]

    hexa()

    digit_list = digit_list [::-1]

    #conversion to decimal

    decimal = 0

    for p in range(len(digit_list)):

        digit_list[p] = int(digit_list[p])

        decimal = decimal + digit_list[p]*base_o**p


    #conversion from decimal to the destination base

    digit_list_d = []

    while decimal > 0:

        digit_list_d.append(decimal%base_d)

        decimal = int((decimal - decimal%base_d) / base_d)


    digit_list_d = digit_list_d[::-1]

    number_d = ''

    for digit in digit_list_d:
        digitstring = str(digit)
        number_d += '' + digitstring

    
    naming(base_o)

    print (f"{number_o} em {base_name}  é igual a:")

    naming(base_d)
           
    print(f"{number_d} em {base_name}")


else:
    print("\nInput inválido. Apenas conversões entre decima, hexadecimal, binário e octal")