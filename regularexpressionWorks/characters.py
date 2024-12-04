from re import finditer

text="I have 3 cars,2 bike and 1-Cycle"

pattern="\w"    #[a-zA-Z0-9]-alphanumerics

pattern="\W"    #[a-zA-Z0-9]-exclude alphanumerics

pattern="\d"    #"[0-9]" -digits 

pattern="\D"    #"[^0-9]" -exclude digits

pattern="\s"    #"[ ]"-incude space

pattern="\S"    #"[^ ]"-exlude space


matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),"==>",obj.group())