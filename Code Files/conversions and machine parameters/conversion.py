import math

# Function to convert a fractional number from any base to decimal
def to_decimal(number: str, base: int) -> float:
    integer_part = 0
    fractional_part = 0.0
    i = 0

    # Process the integer part
    while i < len(number) and number[i] != '.':
        integer_part = integer_part * base + (ord(number[i]) - ord('A') + 10 if 'A' <= number[i] <= 'Z' else ord(number[i]) - ord('0'))
        i += 1

    # If there's a fractional part, process it
    if i < len(number) and number[i] == '.':
        i += 1
        base_power = base
        while i < len(number):
            fractional_part += (ord(number[i]) - ord('A') + 10 if 'A' <= number[i] <= 'Z' else ord(number[i]) - ord('0')) / base_power
            base_power *= base
            i += 1

    return integer_part + fractional_part

# Function to convert a decimal number to any base
def from_decimal(number: float, base: int) -> str:
    integer_part = []
    fractional_part = []
    integer = int(number)
    fractional = number - integer

    # Process the integer part
    while integer > 0:
        remainder = integer % base
        integer_part.append(chr(remainder - 10 + ord('A')) if remainder > 9 else str(remainder))
        integer //= base
    integer_part.reverse()

    # Process the fractional part
    i = 0
    while fractional > 0.0 and i < 10:  # Limit to 10 fractional digits
        fractional *= base
        digit = int(fractional)
        fractional_part.append(chr(digit - 10 + ord('A')) if digit > 9 else str(digit))
        fractional -= digit
        i += 1

    # Combine integer and fractional parts
    if fractional_part:
        return ''.join(integer_part) + '.' + ''.join(fractional_part)
    else:
        return ''.join(integer_part)

# Main function to convert numbers
def convert(number: str, from_base: int, to_base: int):
    decimal_value = to_decimal(number, from_base)
    result = from_decimal(decimal_value, to_base)
    print(f"{number} (base {from_base}) = {result} (base {to_base})")

# Example usage
if __name__ == "__main__":
    number = input("Enter the number: ")
    from_base = int(input("Enter the source base: "))
    to_base = int(input("Enter the target base: "))

    convert(number, from_base, to_base)
