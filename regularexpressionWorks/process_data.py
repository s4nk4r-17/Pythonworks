
from re import findall

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\regularexpressionWorks\\data.txt")

content=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

dates=findall(pattern,content)

for date in dates:

    print(date)

