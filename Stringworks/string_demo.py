# #string="sequence of characters"

# #string=> obeject class

# class str:
    
#     attributes
#     methods

# class Bottle:
#     colour:
#     capacity:
#     shape:
#     material

#     def refill():
#         pass
#     def open():
#         pass
#     def close():
#         pass

# #reference_name=ClassName() #object
# pigeon_bottle1=Bottle()
# pigeon_bottle2=Bottle()
# pigeon_bottle3=Bottle()
# pigeon_bottle4=Bottle()

# pigeon_bottle1.open()
# pigeon_bottle2.refill()

# wilton_bottle=Bottle()



# class Fan:

#     colour:str
#     shape:str
#     speed:str
#     motor_type:str

#     def switch_on():
#         pass
#     def swithc_off():
#         pass
#     def rotate():
#         pass  



# class Car:

#     colour:str
#     shape:str
#     variant:str
#     brand:str

#     def start():
#         pass
#     def accelerate():
#         pass
#     def stop():
#         pass

# baleno_car=Car()

# swift_car=Car()

# swift_car.start()
# baleno_car.start()



# text="hello,world,python"

# words=text.split(",")

# print(words)

# text="\n this is a \n line\n"

# print(text)

# new_text=text.strip("\n")
# new_text=text.lstrip("\n")
# new_text=text.rstrip("\n")


# print(new_text)



# text="hello world program"

# new_text=text.replace("o","a",3)

# print(new_text)


# text="python programming"
#     #012345678901234567
#     #string_object[start:end:stop]

# print(text[0:6])
# print(text[7:])
# print(text[: :2])

#to reverse a string

# string="hello"

# revesed_text=string[::-1]

# print(revesed_text)


# text="helloworld"
#     # 0123456789

# print(text.index("o"))



# text="vipinkumar@gmail.com"

# at_index=text.index("@")

# print(text[0:at_index])


#another way

# print(text[0:text.index("@")])

# text="hellopython"
# # output="llehopython"

# first_l=text.index("l")

# second_l=text.index("l",first_l+1)


# output=text[second_l::-1]+text[4:]

# print(output)

# another method

text="hellopython"
#     012345678910

o_index=text.index("o")

reversed_sub_str=text[o_index-1::-1]

balance_sub_str=text[o_index:]

result=reversed_sub_str+balance_sub_str

print(result)