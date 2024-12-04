

def review(rating):

    if rating<0:

        raise Exception("Too low")
    
    else:
        print("done!")

try:

    review(5)
    
    review(-1)

except Exception as e:

    print(e)

print("hello")

print("hai")

#___________________________________

def vote(age):

    if age<18:

        raise Exception("Invalid age")
    
    else:

        print("Eligible for voting")

try:
    vote(19)

    vote(20)

    vote(17)

except Exception as e:

    print(e)


print("File operation")

print("database commit")

#_____________________________________________________
#use of assert

def poll(age):

    assert age>18,"invalid age"

    print("voted")

try:

    poll(11)

except Exception as e:

    print(e)

#________________________________________________

def review(rating):

    assert rating>0,"Too low"

    assert rating in range(1,11),"too high"

    print("rated")

try:

    review(9)

    review(14)

    review(-1)
    
except Exception as e:

    print(e)

#__________________________________________________






