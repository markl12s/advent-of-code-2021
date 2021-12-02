movements = input_string.split("\n")
split_movements = []
forward = 0
up = 0
down = 0

for i in range(len(movements)):
    split_movements.append(movements[i].split(' '))

    if split_movements[i][0] == 'forward':
        forward += int(split_movements[i][1])
    else:
        if split_movements[i][0] == 'up':
            up += int(split_movements[i][1])
        elif split_movements[i][0] == 'down':
            down += int(split_movements[i][1])


horizontal = forward
depth = down - up

solution = horizontal * depth
print(solution)
