#polymorphism-perform a single task in different way
# 2 types -method overloading and method overriding

#method overloading(same method name and different number of parameters)

class Operations:

    def add(self,num1,num2):

        print(num1+num2)

    def add(self,num1,num2,num3):

        print(num1+num2+num3)

opj_instance=Operations()

opj_instance.add(2,3,4)

opj_instance.add(10,12)

#python doesn't support method overloading,since last
# definition will override previous ones

#eventhough we can overcome this limitation using (*args)