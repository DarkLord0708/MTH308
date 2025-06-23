def toDecimal(number,base):
    integer = 0
    fraction = 0.0
    i = 0

    while(i<len(number) and number[i]!="."):
        integer = integer*base + (ord(number[i])-ord("A")+10 if "A"<=number[i]<="F" else ord(number[i])-ord("0"))
        i+=1
    if(i<len(number) and number[i]=="."):
        i+=1
        base_power = base
        while(i<len(number)):
            fraction += (ord(number[i])-ord("A")+10 if "A"<=number[i]<="F" else ord(number[i])-ord("0"))/base_power
            base_power*=base
            i+=1

    return integer+fraction

def fromDecimal(number,base):
    integerList = []
    fractionList = []
    integer = int(number)
    fraction = number - integer

    while(integer>0):
        rem = integer%base
        integerList.append(chr(rem-10+ord("A")) if rem>9 else str(rem))
        integer //= base
    integerList.reverse()
    
    i = 0
    while fraction >0.0 and i<10:
        fraction *=base
        digit = int(fraction)
        fractionList.append(chr(digit - 10 + ord('A')) if digit > 9 else str(digit))
        fraction -= digit
        i+=1
    
    if fractionList:
        return "".join(integerList)+"."+"".join(fractionList)
    else:
        return "".join(integerList)

def convert(number,from_base,to_base):
    decimalValue = toDecimal(number,from_base)
    result = fromDecimal(decimalValue,to_base)
    print(f"{number} (base {from_base}) = {result} (base {to_base})")

if __name__ == "__main__":
    number = input("Enter the number: ")
    from_base = int(input("Enter the source base: "))
    to_base = int(input("Enter the target base: "))
    convert(number,from_base,to_base)