# Q1) Write the algorithm and code for converting a) Decimal numbers to
# Binary numbers, b) Hexa decimals to Binary numbers, c) Octal numbers to
# Hexa decimals and d) Hexa to Octal.

def toDecimal(number, base):
    # we take number as a string
    int_part = 0
    frac_part = 0
    i = 0
    l = len(number)
    while(i<l and number[i]!="."):
        int_part = int_part*base + (ord(number[i])-ord("A")+10 if ord(number[i])>ord("9") else ord(number[i])-ord("0"))
        i+=1
    if(i<l and number[i]=="."):
        i+=1
        base_power = base
        while(i<l):
            frac_part += (ord(number[i])-ord("A")+10 if ord(number[i])>ord("9") else ord(number[i])-ord("0"))/base_power
            base_power*=base
            i+=1
    return int_part+frac_part

def fromDecimal(number,base):
    int_list = []
    frac_list = []
    int_part = int(number)
    frac_part = number-int_part

    while(int_part>0):
        rem = int_part%base
        int_part = int_part//base
        int_list.append(chr(rem-10+ord("A")) if rem>9 else str(rem))
    int_list.reverse()

    i = 0
    while(i<10 and frac_part>0.0): # calculating for 10 digit precision
        frac_part = frac_part*base
        digit = int(frac_part)
        frac_list.append(chr(digit - 10 + ord("A")) if digit >9 else str(digit))
        frac_part = frac_part-digit
        i+=1
    
    if frac_list:
        return "".join(int_list)+"."+"".join(frac_list)
    else:
        return "".join(int_list)

def convert(number,from_base,to_base):
    decimal_form = toDecimal(number,from_base)
    result = fromDecimal(decimal_form,to_base)
    print(f"{number} (base {from_base}) = {result} (base {to_base})")

n = input("Enter the number: ")
from_base = int(input("Enter the base in which the number is given: "))
to_base = int(input("Enter the base in which you want the result: "))
convert(n,from_base,to_base)




# Q2) In a decimal computing set up, derive the Machine Epsilon for symmetric
# round off error.
def machineEpsilon():
    epsilon = 1.0
    while (1.0 + epsilon>1.0):
        epsilon = epsilon/2
    return epsilon*2

print(f"Machine epsilon in python is {machineEpsilon()}")