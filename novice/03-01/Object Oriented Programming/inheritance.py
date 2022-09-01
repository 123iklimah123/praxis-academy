class SchoolMember:
    '''represent any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''tell my details.'''
        print('name:"{}" age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(initialized teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''represents a student'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('mrs. ikaaa', 40, 30000)
s = Student('kala', 25, 75)

print()

members = [t, s]
for member in members:
    member.tell()