text="ABBACB"

character_count={}

for ch in text:

    if ch in character_count:

        character_count[ch]+=1

    else:

        character_count[ch]=1

print(character_count)

#or

ch_count={ch:text.count(ch) for ch in text}

print(ch_count)