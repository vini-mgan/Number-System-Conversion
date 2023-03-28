number = input("Number \n")

base = int(input("Base: \n"))

digit_list = [str(x) for x in number]

if base == 16:

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


digit_list = digit_list[::-1]

decimal = 0

for d in range(len(digit_list)):

    digit_list[d] = int(digit_list[d])

    decimal = decimal + digit_list[d] * base**d

print(decimal)


