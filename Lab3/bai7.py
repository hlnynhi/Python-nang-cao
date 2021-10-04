def read_molecule(reader):
    content = []
    for line in reader:
        if not line.startswith('CMNT'):
            if not line.isspace():
                content.append(line.strip())
    for line in content:
        print(line)
    