def decimal_to_binary(i):
    binary = bin(i).replace("0b", "")
    return binary


def decimal_to_octal(i):
    octal = 0
    return octal


def decimal_to_hexadecimal(i):
    hexadecimal = 0
    return hexadecimal


def print_formatted(n):
    max_binary_number_length = len(decimal_to_binary(n))
    for i in range(n):
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
