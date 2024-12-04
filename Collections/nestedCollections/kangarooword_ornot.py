
source_word="CHICKEN"

target_word="HEN"

#step 1 find source_word character count

# create empty dictionary

character_count={}

for ch in source_word:

    if ch in character_count:

        character_count[ch]+=1
    
    else:

        character_count[ch]=1

#or another method

character_count={ch:source_word.count(ch) for ch in source_word}

print(character_count)

kangaroo=True

for ch in target_word:

    if ch in character_count and character_count.get(ch)>0:

        character_count[ch]-=1

        print(ch,character_count)

    else:


        kangaroo=False

if kangaroo:

    print("Kangaroo word")

else:

    print("Not Kangaroo word")