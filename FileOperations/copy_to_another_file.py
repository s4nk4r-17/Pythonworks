
# Create a program to copy content from one file to another.

source_file=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\word_count.txt","r")

destination_file=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\destination_file.txt","w")

content=source_file.read()

destination_file.write(content)

source_file.close()

destination_file.close()