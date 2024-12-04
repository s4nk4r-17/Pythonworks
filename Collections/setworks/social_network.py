
users=['rahul','rohit','kohli','rishab','sanju','pandya','siraj']

rahul_followers=['rohit','kohli','rishab','rahul']

sanju_follower=['sanju','kohli','rohit']

#mutual_friends=[]

#follow_suggestions=["sanju",'pandya','siraj']

users_set=set(users)

# rahul_followers_set=set(rahul_followers)

# follow_suggestions=users_set.difference(rahul_followers_set)

# print(follow_suggestions)

# or another method

follow_suggestion=set(users).difference(set(rahul_followers))

print(follow_suggestion)

mutual_friends=set(sanju_follower).intersection(set(rahul_followers))

print(mutual_friends)