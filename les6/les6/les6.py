import random

class Homo:
    # height = 170
    # sex = 'w'
    # age = 0
    # weight = 66

    __population = 0

    def __init__(self, height, sex, age, weight, father=None, mother=None):
        self.height = height
        self.sex = sex
        self.age = age
        self.weight = weight
        self._ind = weight / (height**2)
        self.__duble_ind = self._ind ** 2
        self.father = father
        self.mother = mother
        Homo.__population += 1

    def say(self):
        print('HEYYYY')

    def say_duble_ind(self):
        print(self.__duble_ind)

    def population(self):
        print(Homo.__population)

class Human(Homo):

    def __init__(self, height, sex, age, weight, name, surname, father=None, mother=None):
        self.name = name
        self.surname = surname
        super().__init__(height, sex, age, weight, father, mother)

    def say2(self):
        print(self._ind)

    def say(self):
        print(f'my name is {self.name} {self.surname}')

    def reproduction(self, other):
        return Human(20, random.choice(('w', 'm')), 0, 3.600, other.name, self.surname, father=self, mother=other)

if __name__  == '__main__':
    dasha = Human(170, "w", 22, 55, 'Dasha', 'Ivanova')
    petr = Human(180, "m", 25, 75, 'Petr', 'Petrov')
    child = petr.reproduction(dasha)
    print(1)