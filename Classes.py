class Student:
    name = 'Student1'
    address='line1/nline2/ncity/nstate'

    def __init__(self, name, add):
        self.name=name
        self.address=add


k = Student('student1', 'add1')

print getattr(k, 'name')
print k.name

setattr(k, 'name', 'student2')

print k.name

## Inheritance

class Shape:
    test = 'test'
    def area(selfself):
        print "Shape area"

        def __str__(self):
        return "Shape_" + self.test

class Square(Shape):
    __side=None
    def setSide(self,side):
        self.__side=side

    def getSide(self):
        return self.__side
    def area(self):
        print "Square area"
        return self.side * self.side

class Rangle(Square,Shape,):
    def area1(self):
        print "Rangle area"
        return self.width * self.height


# a=Shape()
# a.area()


s=Rangle()
s.side=5
s