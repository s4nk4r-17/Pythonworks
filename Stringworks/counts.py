text="pneumonoultramicroscopicsilicovolcanoconsiosis"

#print vowel count
#print consonants


text=text.casefold()

vowel ="aeiou"

vowel_count=0

consonant_count=0

for ch in text:

    if ch in vowel: 

        vowel_count+=1

    else:

        consonant_count+=1

print(f"Vowel count:{vowel_count}")

print(f"Cononant count:{consonant_count}")

