# given  a string print the folllowing: # a.The count of alphabets# b.The count of spaces# c.The count of special characters# d.The count of numbers

text = "On June 5th, 2024, we will celebrate @ our annual event: 'Tech Innovations 2024!'"
alpha_count=0
space_count=0
spec_char_count=0
number_count=0

for char in text:

    if char.isalpha():

        alpha_count+=1

    elif char.isspace():

        space_count+=1

    elif char.isdigit():

        number_count+=1

    else:

        spec_char_count+=1

    
print("Count of alphabets :",alpha_count)
print("Count of number:",number_count)
print("Count of spaces:",space_count)
print("Count of special characters:",spec_char_count)