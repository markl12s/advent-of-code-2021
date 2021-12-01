measurments = measurment_string.split("\n")
increases = 0

for i in range(len(measurments) - 1):
    if measurment[i] < measurment[i + 1]:
        increases += 1

print(increases)
