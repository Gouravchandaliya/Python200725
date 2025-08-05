p1 = "sf"
p2 = "sedf"
p3 = "fsd"
p4="fsasw"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")
else:
    print("this comment is not a spam")