class Constructor:
    def __init__(self,name):
        self.name=name

    def print_name(self):
        print(f"The name is:{self.name}")

cons=Constructor("Prajwal")#here constructor is used...
cons.print_name()