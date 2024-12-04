
student_data={
    "hari":[45,40,35],
    "vipin":[34,40,45],
    "vinay":[45,40,35],
    "bijoy":[33,38,35],
    "anvin":[32,30,40]
}

#index=1 hari's avg mark
#index=2 anvin's avg mark

index=int(input("Enter the index number:"))

for i,element in enumerate(student_data):

    if i+1==index:

        marks=student_data.get(element)

        avg=sum(marks)/len(marks)

        print(avg)


#creating a dictionary of names corresponing to average marks

average_score={}

for student,marks in student_data.items():

    avg_score=sum(marks)/len(marks)

    average_score[student]=avg_score

print(average_score)    #{'hari': 40.0, 'vipin': 39.666666666666664, 'vinay': 40.0, 'bijoy': 35.333333333333336, 'anvin': 34.0}

student_average_score={student:sum(marks)/len(marks)for student,marks in student_data.items()}

print(student_average_score)    #{'hari': 40.0, 'vipin': 39.666666666666664, 'vinay': 40.0, 'bijoy': 35.333333333333336, 'anvin': 34.0}




