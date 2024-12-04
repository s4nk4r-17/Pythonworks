#create dictionary employee with keys eid,name,salary,department,experience

employee={"eid":1232,"name":"vinod","salary":35000,"department":"hr","experience":5}

print(employee)

#add contact ad 3567890

employee["contact"]=3567890

print(employee)

#if experience>=5years update employee salary as current_salary+10000 else current_salary+5000


if employee["experience"]>=5:

    employee["salary"]+=10000

else:

    employee["salary"]+=5000

print(employee)

#add role as SDF if exp>5 else add role as JDE

if employee["experience"]>=5:

    employee["role"]="SDE"

else:

    employee["role"]="JDE"

print(employee)