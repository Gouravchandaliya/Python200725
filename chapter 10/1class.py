class employee:
    name = "Harry"
    age = 29
    salary = 120000

    def getInfo(self):
        print(f"{self.age} {self.salary}")

    def __init__(self):
        print("I am creating a object") 

harry = employee()
harry.name = "Nikhil"
print(harry.name, harry.age, harry.salary)
harry.age = 23
harry.getInfo()