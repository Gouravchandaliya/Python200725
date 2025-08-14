from random import randint
class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, fro, to):
        print(f"{self.trainNo} from {fro} to {to}")
        

    def getStatus(self):
        print(f"{self.trainNo}")

    def getFare(self, fro, to):
        print(f"{self.trainNo} from {fro} to {to} is {randint(222, 5555)}")


t = Train(12330)
t.book("rampur", "Delhi")
t.getFare("rampur", "Delhi")
t.getStatus()