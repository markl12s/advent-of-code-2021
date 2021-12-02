movements = input_string.split("\n")
split_movements = []
forward = 0
up = 0
down = 0

depth = 0
aim = 0

for i in range(len(movements)):
    split_movements.append(movements[i].split(' '))

    if split_movements[i][0] == 'forward':
        forward += int(split_movements[i][1])
        depth += int(split_movements[i][1]) * aim
    else:
        if split_movements[i][0] == 'up':
            up += int(split_movements[i][1])
        elif split_movements[i][0] == 'down':
            down += int(split_movements[i][1])

    aim = down - up


horizontal = forward

solution = horizontal * depth
print(solution)
