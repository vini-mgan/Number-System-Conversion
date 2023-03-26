decimal = float(input())

integer = int(decimal)

fraction = decimal - integer

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