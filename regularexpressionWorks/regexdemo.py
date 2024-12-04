

from re import finditer

text="abababbaab"
#     0123456789
# pattern="ab"

#[(0,ab),(2,ab),(4,ab),(8,ab)]
#[(start.group)]


matcher=finditer("ab",text)
#pattern(pattern,text) 

for m in matcher:

    print(m.start(),m.group(), end=" ")
#_________________________________

# to print ba and its group

match=finditer("ba",text)

for m in match:

    print(m.start(),m.group())

#_________________________________________________

text="fatcatrunsveryfasttocatchtherat"

match=finditer("(at)",text)

for obj in match:

    print(obj.groups())

    print(obj.start(),obj.group())

