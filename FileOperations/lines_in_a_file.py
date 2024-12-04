# Write a Python program that reads a file and 
# prints the total number of lines in the file

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\word_count.txt","r")

line_count=0 

for line in f:

    line_count+=1

print(line_count)