# Given a dictionary where the keys are student names
# and the values are their scores, 
# write a program to calculate the average score.

student_score={"Arya":80,"Rick":74,"Sam":68}

total_score=sum(student_score.values())

num_students=len(student_score)

avg_score=total_score/num_students

print(avg_score)

