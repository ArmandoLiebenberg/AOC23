file1 = open("p2_text.txt", "r")
Lines = file1.readlines()

limits = {"red":12, "green":13, "blue":14}

total = 0
for line in Lines:
    valid = True
    
    line = line.split(':')
    id = (line[0].split())[1]
    
    games = line[1].split(';')
    for game in games:
        pulls = game.split(',')
        for pull in pulls:
            colors = pull.split(' ')
            colors[2] = colors[2].strip('\n')
            if int(colors[1]) > limits.get(colors[2]):
                valid = False

    if valid:
        total += int(id)

print(total)
