

decimal = float(input("Decimal base number to be converted: "))

base = int(input("Conversion base: "))

integer = int(decimal)

fraction = decimal - integer

if base == 2:

    #INTEGER PART CONVERSION

    binary = []

    while integer > 0:

        binary.append(integer%2)

        integer = int((integer - integer%2) / 2)

    binary = binary[::-1]

    mystring = ''

    for bit in binary:
        bitstring = str(bit)
        mystring += '' + bitstring

    #FRACTIONAL PART CONVERSION

    binary_fraction = []

    while True:

        fraction = fraction * 2

        binary_fraction.append(int(fraction))

        if fraction == 0:
            break

        fraction = fraction - int(fraction)

    mystring_fraction = ''

    for bit in binary_fraction:
        bitstring = str(bit)
        mystring_fraction += '' + bitstring

    #PRINT RESULTS

    print(f"{decimal} em decimal é igual a {mystring}.{mystring_fraction} em binário")

elif base == 8:

    #INTEGER PART CONVERSION

    octal = []

    while integer > 0:

        octal.append(int(integer%8))

        integer = (integer - integer%8) / 8

    octal = octal[::-1]

    octal_str = ''

    for oct_digit in octal:
        oct_digit_str = str(oct_digit)
        octal_str += '' + oct_digit_str

    #FRCATIONAL PART CONVERTION

    octal_f = []

    while True:

        fraction = fraction * 8

        octal_f.append(int(fraction))

        fraction = fraction - int(fraction)

        if fraction == 0 :
            break

    octal_f_str = ''

    for octal_f_digit in octal_f:
        octal_f_digit_str = str(octal_f_digit)
        octal_f_str += '' + octal_f_digit_str


    print(f"{decimal} em decimal é igual a {octal_str}.{octal_f_str} em octal")

elif base == 16:

    #INTEGER PART CONVERSION

    hexa = []

    while integer > 0:

        hexa.append(int(integer%16))

        integer = (integer - integer%16)/16

    hexa = hexa[::-1]


    for a in range(len(hexa)):

        if hexa[a] == 10:
            hexa[a] = 'A'

        elif hexa[a] == 11:
            hexa[a] = 'B'

        elif hexa[a] == 12:
            hexa[a] = 'C'

        elif hexa[a] == 13:
            hexa[a] = 'D'


        elif hexa[a] == 14:
            hexa[a] = 'E'

        elif hexa[a] == 15:
            hexa[a] = 'F'

    hexa_str = ''

    for hexadigit in hexa:
        hexadigit_str = str(hexadigit)
        hexa_str += '' + hexadigit_str

    #FRACTIONAL PART CONVERTION

    hexa_f = []

    while True:

        fraction = fraction * 16

        hexa_f.append(int(fraction))

        if fraction == 0:
            break

        fraction = fraction - int(fraction)

    for a in range(len(hexa_f)):

        if hexa_f[a] == 10:
            hexa_f[a] = 'A'

        elif hexa_f[a] == 11:
            hexa_f[a] = 'B'

        elif hexa_f[a] == 12:
            hexa_f[a] = 'C'

        elif hexa_f[a] == 13:
            hexa_f[a] = 'D'


        elif hexa_f[a] == 14:
            hexa_f[a] = 'E'

        elif hexa_f[a] == 15:
            hexa_f[a] = 'F'

    hexa_f_str = ''

    for hexa_f_digit in hexa_f:
        hexa_f_digit_str = str(hexa_f_digit)
        hexa_f_str += '' + hexa_f_digit_str

    print(f"{decimal} em decimal é igual a {hexa_str}.{hexa_f_str} em hexadecimal")
