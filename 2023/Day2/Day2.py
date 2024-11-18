import numpy as py

# # Part 1
res = 0
with open("./input.csv","r") as f:
    for i,line in enumerate(f,start=1):
        games = (map(lambda x:x.split(", "),line.split(": ")[1].split("; ")))
        red = 0
        green = 0
        blue = 0
        for game in games:
            for ball in game:
                num = int(ball[:2])
                color = ball[2:].strip()
                
                # print(num,color)
                if color == "red":
                    red = num if num > red else red
                elif color == "green":
                    green = num if num > green else green
                elif color == "blue":
                    blue = num if num > blue else blue
                
        if red <= 12 and green <= 13 and blue <= 14:
            print(i,red,green,blue)
            res += i
print(res)

# Part 2
res = 0
with open("./input.csv","r") as f:
    for i,line in enumerate(f,start=1):
        games = (map(lambda x:x.split(", "),line.split(": ")[1].split("; ")))
        red = 0
        green = 0
        blue = 0
        for game in games:
            for ball in game:
                num = int(ball[:2])
                color = ball[2:].strip()
                
                # print(num,color)
                if color == "red":
                    red = num if num > red else red
                elif color == "green":
                    green = num if num > green else green
                elif color == "blue":
                    blue = num if num > blue else blue
                
        power = red * green * blue
        print(i,red,green,blue, power)
        res += power
print(res)