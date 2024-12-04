

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\words.txt","r")

for line in f:

    print(line.rstrip("\n"))

f.close()