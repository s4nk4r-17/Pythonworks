
# Create a program that appends user input to an existing file
#  and then displays the entire content of the file.

user_input=input("Enter the text:")

f1=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\inputfromuser.txt","a")

f1.write(user_input+ "\n")

f1.close()

f2=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\inputfromuser.txt","r")

content=f2.read()

print(content)

f2.close()