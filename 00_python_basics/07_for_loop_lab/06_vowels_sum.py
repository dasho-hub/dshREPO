prompt = input()
index = 0
length = len(prompt)
sum = 0

for letter in range(index, length):
    if prompt[letter] == "a":
        sum += 1
    elif prompt[letter] == "e":
        sum += 2
    elif prompt[letter] == "i":
        sum += 3
    elif prompt[letter] == "o":
        sum += 4
    elif prompt[letter] == "u":
        sum += 5
print(sum)