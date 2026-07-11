# sentence = " I  love     python  tooooooo  much. "

sentence = "I     am learning      python   programming    language        ."
raw_data = sentence.split(" ")

words = []
for text in raw_data:
    if text:
        words.append(text)


clean_data = " ".join(words)
print(" Dirty Data: ", sentence)
print(" Clean Data: ", clean_data)