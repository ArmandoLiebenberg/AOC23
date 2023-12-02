import re

file1 = open("p1_text.txt", "r")
Lines = file1.readlines()

words = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

total = 0
for line in Lines:
    numbers = []

    for count, character in enumerate(line):

        for word in words:
            if word in line[count:] and line[count:].index(word) == 0:
                numbers.append(words.get(word))

        if character.isnumeric():
            numbers.append(int(character))

    total += 10 * numbers[0]
    total += numbers[-1]
    
print(total)
