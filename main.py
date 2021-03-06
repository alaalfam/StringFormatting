def decimal_to_binary(i):
    binary = bin(i).replace("0b", "")
    return binary


def decimal_to_octal(i):
    octal = ""
    while i != 0:
        octal = str(i % 8) + octal
        i = int(i / 8)
    return octal


def decimal_to_hexadecimal(i):
    hexadecimal = ""
    while i != 0:
        if i % 16 < 10:
            hexadecimal = chr(i % 16 + 48) + hexadecimal
        else:
            hexadecimal = chr(i % 16 + 55) + hexadecimal
        i = int(i / 16)
    return hexadecimal


def print_formatted(n):
    max_binary_number_length = len(decimal_to_binary(n))
    for i in range(1, n+1):
        binary_number = decimal_to_binary(i)
        decimal_number = i
        octal_number = decimal_to_octal(i)
        hexadecimal_number = decimal_to_hexadecimal(i)
        str_line = str(decimal_number).rjust(max_binary_number_length) + " " + str(octal_number).rjust(
            max_binary_number_length) + " " + str(
            hexadecimal_number).rjust(max_binary_number_length) + " " + str(binary_number).rjust(
            max_binary_number_length)
        print(str_line)
    pass


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
