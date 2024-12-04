
from json import load

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\employee.json")

data=load(f)

for emp in data:

    print(emp)