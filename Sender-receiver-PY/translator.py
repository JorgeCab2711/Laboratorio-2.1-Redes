def string_to_binary(input_string):
    binary = ''.join(format(ord(char), '08b') for char in input_string)
    return binary

def binary_to_string(binary_string):
    binary_values = binary_string.split(' ')
    ascii_string = ''.join(chr(int(binary, 2)) for binary in binary_values)
    return ascii_string

