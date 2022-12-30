class Person:

    def __init__(self, n, surn, patr, bd, s):
        self.name = n
        self.surname = surn
        self.patronymic = patr
        self.birthday = bd
        self.sex = s

    def __getattr__(self, attr_name):
        return 'Unknown'

    def __setattr__(self, attr_name, attr_val):
        self.__dict__[attr_name] = attr_val


class Employee(Person):

    def __init__(self, n, surn, patr, bd, s, spec, pos, sal, exp):
        Person.__init__(self, n, surn, patr, bd, s)
        self.specialty = spec
        self.position = pos
        self.salary = sal
        self.experience = exp

    def __str__(self):
        return f'Full name - {self.surname} {self.name} {self.patronymic}, specialty - {self.specialty}, ' \
               f'position - {self.position}, salary - {self.salary} hrn, experience - {self.experience} years'


class Org:

    instances = []

    def __init__(self, n, exp):

        self.name = n
        self.experience = exp

    def __add__(self, empl):
        self.instances.append(empl)
        empl.organization = self.name

    def __str__(self):
        for empl in self.instances:
            print(empl)
        return f'\nOrg name - {self.name}, minimal experience - {self.experience} years, number of employees - ' \
               f'{len(self.instances)}, number of experienced employees - {self.num_experienced()}'

    def num_experienced(self):
        num = 0
        for empl in self.instances:
            if empl.experience >= self.experience:
                num += 1
        return num




if __name__ == '__main__':
    o1 = Org("BigOrg", 5)
    p1 = Employee("Dmytro", "Shevchenko", "Romanovych", "23.07.1993", "Male", "072", "financial manager", 15000, 7)
    o1 + p1
    #Changed name
    p1.name = "Pavlo"
    #Display some attributes
    print(p1.name)
    print(p1.sex)
    print(p1.mother_name)
    print(p1.organization)
    print(p1.salary, '\n')
    #Add new employees
    p2 = Employee("Halyna", "Kravchuk", "Ivanivna", "19.04.1997", "Female", "075", "marketing", 13000, 3)
    p3 = Employee("Stepan", "Kovalchuk", "Stepanovych", "02.05.1989", "Male", "073", "main manager", 18000, 11)
    p4 = Employee("Olga", "Petrenko", "Vasylivna", "14.11.1994", "Female", "056", "brand ambassador", 15000, 8)
    o1 + p2
    o1 + p3
    o1 + p4
    #Display all employees
    print(o1)
