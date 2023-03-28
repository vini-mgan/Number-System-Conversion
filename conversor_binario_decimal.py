
#Binary to decimal conversion

number = int(input())

number = str(number)

#Using list comprehension to turn the str in a list of int digits

digit_list = [int(x) for x in str(number)]

digit_list = digit_list[::-1]

decimal = 0

for n in range(len(digit_list)):

    decimal = decimal + digit_list[n] * 2**n

print(decimal)


