#NUMBER SYSTEM CONVERSOR
#Vinícius Martins Galindo Andrade

from tkinter import *
 
#Defining the button command

def retrieve():
    global number_o
    global base_o
    global base_d
    number_o = entry1.get()
    base_o = int(entry2.get())
    base_d = int(entry3.get())
    
#Setting window and receiving inputs

root = Tk()
#root.geometry("400x400")
root.title("Conversor entre sistemas numericos")

frame = Frame(root)
frame.pack()

label1 = Label(frame, text = "Insert the value to convert")
label1.pack()

entry1 = Entry(frame, width = 20)
entry1.insert(0, 'Number')
entry1.pack(padx=5, pady=5)

label2 = Label(frame, text = "Insert the original number system")
label2.pack()

entry2 = Entry(frame, width = 20)
entry2.insert(0, 'Original Base')
entry2.pack(padx=5, pady=5)

label3 = Label(frame, text = "Insert the destiny number system")
label3.pack()

entry3 = Entry(frame, width = 20)
entry3.insert(0, 'Conversion Base')
entry3.pack(padx=5, pady=5)

Button = Button(frame, text = "Submit", command = retrieve)
Button.pack(padx = 5, pady = 5)

root.eval('tk::PlaceWindow . center')
root.mainloop()

#Searching for invalid inputs

digit_list = [str(x) for x in number_o]

digit_list = digit_list[::-1]

bases = [2, 8, 10, 16]

bin_value = ['0', '1']
octa_values = ['0', '1', '2', '3', '4', '5', '6', '7']
hexa_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

for digit in digit_list:

    if base_o == 2 and digit not in bin_value:

        print(f"{digit} isn't a valid algarism for a decimal number")

        exit()

    elif base_o == 8 and digit not in octa_values:

        print(f"{digit} isn't a valid algarism for an octal number")

        exit()

    elif  base_o == 16 and digit not in hexa_values:

        print(f"{digit} isn't a valid algarism for an hexadecimal number")

        exit()

number_d = 0

#Function for the treatment of decimal values

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

    elif base_o ==10 and base_d == 16:

        for a in range(len(digit_list)):

            if digit_list[a] == 10:
                digit_list[a] = 'A'

            elif digit_list[a] == 11:
                digit_list[a] = 'B'

            elif digit_list[a] == 12:
                digit_list[a] = 'C'

            elif digit_list[a] == 13:
                digit_list[a] = 'D'


            elif digit_list[a] == 14:
                digit_list[a] = 'E'

            elif digit_list[a] == 15:
                digit_list[a] = 'F'   

#Function for defining the number system name

def naming(base):

    global base_name

    if base == 2:
        base_name = "binário"

    elif base == 8:
        base_name = "octal"

    elif base == 16:
        base_name = "hexadecimal"

#IN CASE THE BASES ARE THE SAME

if base_d == base_o:
    print("\nAs bases são iguais")

#IN CASE THE BASES ARE NOT SUPORTED

elif base_o not in bases or base_d not in bases:

    print("\nInput inválido. Apenas conversões entre decimal, hexadecimal, binário e octal")

#CONVERSION FROM DECIMAL TO OTHER NUMBER SYSTEMS

elif base_o == 10:

    decimal = int(number_o)

    digit_list = []

    while decimal != 0:

        digit_list.append(decimal%base_d)

        decimal = int( (decimal - decimal%base_d)/16 )

    digit_list = digit_list[::-1]

    hexa()

    number_d = ''

    for digit in digit_list:
        digitstring = str(digit)
        number_d += '' + digitstring


    naming(base_d)

    print(f"\n{number_o} em decimal é igual a {number_d} em {base_name}")


#CONVERSION FROM OTHER NUMBER SYSTEMS TO DECIMAL

elif base_o != 10 and base_d == 10:

    hexa()

    for p in range(len(digit_list)):

        digit_list[p] = int(digit_list[p])

        number_d = number_d + digit_list[p] * base_o**p


    naming(base_o)

    print (f"\n{number_o} em {base_name} é igual a {number_d} em decimal")


#CONVERSION BETWEEN BINARY, OCTAL AND HEXADECIMAL

elif base_o != 10 and base_d != 10:

    hexa()

    #conversion to decimal

    decimal = 0

    for p in range(len(digit_list)):

        digit_list[p] = int(digit_list[p])

        decimal = decimal + digit_list[p]*base_o**p


    #conversion from decimal to the destination base

    digit_list_d = []

    while decimal > 0:
 
        hexa()

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
