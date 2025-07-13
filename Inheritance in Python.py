class Grandparent:
    def Pop(self):
     print("This is grandparent class")

class Parent(Grandparent):#Parent is inherited from grandparent class
    def show(self):
        print("This is Parent class ")

class Child(Grandparent):
    def display(self):
        print("This is child Class")

#Parent object is created
paren=Parent()
paren.Pop()
paren.show()
#Child Object is created
chil=Child()
chil.Pop()
chil.display()



