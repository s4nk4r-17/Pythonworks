
text="ABABBCCDDE"

character_frequency={ch:text.count(ch) for ch in text}

print(character_frequency)

non_recursive_elements={ch:count for ch,count in character_frequency.items() if count==1}

print(non_recursive_elements)

#another method

for ch,count in character_frequency.items():

    if count==1:

        print(ch)