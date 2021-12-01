measurments = measurment_string.split("\n")
increases = 0

for i in range(len(measurments) - 3):
    window_a = int(measurments[i]) + int(measurments[i + 1]) + int(measurments[i + 2])
    window_b = int(measurments[i + 1]) + int(measurments[i + 2]) + int(measurments[i + 3])

    if window_a < window_b:
        increases += 1

print(increases)
