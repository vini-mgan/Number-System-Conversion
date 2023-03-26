
decimal = float(input())

integer = int(decimal)

fraction = decimal - integer

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