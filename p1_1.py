file1 = open("p1_text.txt", "r")
Lines = file1.readlines()

total = 0
for line in Lines:
	numbers = []

	for character in line:
		if character.isnumeric():
			numbers.append(int(character))
		
	total += 10 * numbers[0]
	total += numbers[-1]
    
print(total)