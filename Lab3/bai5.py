from bai4 import skip_header
def smallest_value_skip(reader):
    line = skip_header(reader).strip()
    # Only execute this code, if there is data following the header.
    if line != '':
        smallest = line
    for line in reader:
        line = line.strip()
        if line != '-':
            value = line
            smallest = min(smallest, value)
    return smallest

input_file = open('D:\\Python\\alkaline_metals.txt', 'r')
print(smallest_value_skip(input_file))
input_file.close()