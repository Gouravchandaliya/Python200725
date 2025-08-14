class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    

p = Programmer("Sohan", 120000, 233234)
print(p.name, p.salary, p.pin)