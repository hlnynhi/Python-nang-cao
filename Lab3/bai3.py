newlist = []
for line in open('D:\\Python\\PythonTH\\Lab3\\alkaline_metals.txt'):
    newlist.append(line.strip())
for line in reversed(newlist):
    print(line)