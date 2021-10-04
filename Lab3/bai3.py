newlist = []
for line in open('D:\\Python\\alkaline_metals.txt'):
    newlist.append(line.strip())
for line in reversed(newlist):
    print(line)