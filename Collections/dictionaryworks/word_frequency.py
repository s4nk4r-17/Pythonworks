
words=["hai","hello","hai","this","is","hello","hai"]

#word_frequency

word_frequency={w:words.count(w) for w in words }

print(word_frequency)

recurive_words={w:count for w,count in word_frequency.items()if count>1}

print(recurive_words)

non_recurive_words={w:count for w,count in word_frequency.items()if count==1}

print(non_recurive_words)

#most_recursive_word

most_recursive_word = max(word_frequency, key=word_frequency.get)

print(most_recursive_word)