# text="hello"
# reversed_txt=text[::-1]
# print("palindrome" if reversed_txt==text else "not palindrome" )

#another method

text="malayalam"
#index=01234
#lenght=12345
reversed_str=""

length=len(text)-1

for i in range(length,-1,-1):
   
    reversed_str+=text[i]

print(reversed_str)

if reversed_str==text:

    print("palindrome")

else:

    print("not palindrome")

#another method 

# text=input("Enter text:")

# reversed_text=text[: :-1]

# if text==reversed_text:

#     print("palindrome")

# else:

#     print('not palindrome')