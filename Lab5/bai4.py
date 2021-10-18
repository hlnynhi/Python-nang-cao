class Nematode:
    def __init__(self, length, gender, age):
        self.length = length
        self.gender = gender
        self.age = age
    def __str__(self):
        return 'Nematode: length {}mm, gender is {} and age {} days'.format(self.length, self.gender, self.age)
    def __repr__(self):
        return "Nematode({}, {}, {})".format(self.length, self.gender, self.age)
nematode = Nematode(1, 'hermaphrodite', 2)
print(nematode.__str__())
print(nematode.__repr__())