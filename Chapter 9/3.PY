f = open("file1.txt")


lines = f.readlines()
print(lines)

f.close()


string = "Hey Jd bhai How are you "
f = open("file1.txt", "a")

f.write(string)

f.close()