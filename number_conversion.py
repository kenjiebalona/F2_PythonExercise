def decToBinary(dec):
    if dec == 0:
        return '0'
    binary = ''
    while dec > 0:
        remainder = dec % 2
        binary = str(remainder) + binary
        dec = dec // 2
    return binary

def binaryToN(bin, base):
    if base == 10:
        decimal = 0
        binary = str(bin)
        length = len(binary)
        for i in range(length):
            decimal += int(binary[length - 1 - i]) * (2 ** i)
        return decimal
    else:
        decimal = 0
        binary = str(bin)
        length = len(binary)
        for i in range(length):
            decimal += int(binary[length - 1 - i]) * (2 ** i)
        if base == 8:
            return oct(decimal)
        elif base == 16:
            return hex(decimal)

def decToOctal(dec):
    if dec == 0:
        return '0'
    octal = ''
    while dec > 0:
        remainder = dec % 8
        octal = str(remainder) + octal
        dec = dec // 8
    return octal

def decToHex(dec):
    if dec == 0:
        return '0'
    hex_chars = "0123456789ABCDEF"
    hexa = ''
    while dec > 0:
        remainder = dec % 16
        hexa = hex_chars[remainder] + hexa
        dec = dec // 16
    return hexa

def main():
    decimal = 69

    binary_result = decToBinary(decimal)
    decimal_result = binaryToN(binary_result, 10)
    octal_result = decToOctal(decimal)
    hexadecimal_result = decToHex(decimal)

    print(f"Decimal: {decimal_result}")
    print(f"Binary: {binary_result}")
    print(f"Octal: {octal_result}")
    print(f"Hexadecimal: {hexadecimal_result}")

main()