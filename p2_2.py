file1 = open("p2_text.txt", "r")
Lines = file1.readlines()



total = 0
for line in Lines:
    
    line = line.split(':')
    id = (line[0].split())[1]


    limits = {"red":0, "green":0, "blue":0}
    red = 0
    green = 0
    blue = 0
    
    games = line[1].split(';')
    for game in games:
        pulls = game.split(',')
        for pull in pulls:
            colors = pull.split(' ')
            colors[2] = colors[2].strip('\n')

            if int(colors[1]) > limits[colors[2]]:
                limits[colors[2]] = int(colors[1])

    power = limits["red"] * limits["green"] * limits["blue"]
    print(power)
    total += power

print(total)
