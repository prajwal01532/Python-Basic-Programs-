class Sample:
    def get(self):
        self.name = input("Enter Your Name:")  # Store the input in an instance variable

    def display(self):
        print(f"My Name is {self.name}")  # Access the instance variable


obj = Sample()
obj.get()
obj.display()
