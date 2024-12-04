# Write a program to take input from the user and write it to a file. 
# Then, read the content from the file and display it.

data_from_user=input("Enter the text:")

f1=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\inputfromuser.txt","w")

for text in data_from_user:

    f1.write(text)

f1.close()

f2=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\inputfromuser.txt","r")

for line in f2:

    print(line.rstrip("\n"))


