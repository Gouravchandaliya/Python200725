f = open("filee.txt")
c = f.read()
if("Twinkle" in c):
    print("Twinkle is present in the c")

else:
    print("Twinkle is not present in the c")
f.close()