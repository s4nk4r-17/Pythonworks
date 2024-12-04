# Write a Python program to filter a dictionary, 
# keeping only items withvalues greater
#  than 50 using dictionary comprehension.

scores={"Arya":40,"Rick":44,"Sam":31,"Remya":54,"Vinod":55}

filtered_score={key:value for key,value in scores.items() if value>50}

print(filtered_score)