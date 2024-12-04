#print pangram if there is every english albhabet


text="The quick brown fox jumps over the lazy dog"

text=text.casefold()

is_pangram=True 

alphabet="abcdefghijklmnopqrstuvwxyz"

for ch in alphabet:
    
    if ch not in text:

        is_pangram=False

        break        

print(is_pangram)