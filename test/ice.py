import pprint

ice = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

print(ice[0][2])
count = 0
x, y = 0, 0

while True:
    for x in range(4):
        for y in range(5):
            print(x, y)
            if ice[x][y] == 0:
                temp_x = x
                temp_y = y
                break
        break


    ice[temp_x][temp_y] = 2
    print(temp_x, temp_y)

    while x < len(ice) and y < len(ice[0]):
        if(ice[x][y+1] == 0 and ice[x+1][y] == 0):
            ice[x][y+1] = 2
            ice[x+1][y] = 2
            y += 1
        elif(ice[x+1][y] == 0):
            ice[x+1][y] = 2
            x += 1
        elif(ice[x][y+1] == 0):
            ice[x][y+1] = 2
        else:
            count += 1
            print(count)
            break