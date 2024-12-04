
f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\fruits.txt","r")

fruits=[]

for line in f:

    fruits.append(line.rstrip("\n"))#rstrip is done to remove \n at the end of each word

print(fruits)