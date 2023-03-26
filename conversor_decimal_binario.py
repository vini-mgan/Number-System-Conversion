
decimal = float(input())

integer = int(decimal)

fraction = decimal - integer

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