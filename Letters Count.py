sentence= input("Enter a sentence : ").lower()
letter ={}
for i in sentence:
    letter[i] = sentence.count(i)
print(letter)
