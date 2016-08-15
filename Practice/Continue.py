numbersTaken = [2, 4, 6, 8, 10]

print("Here are the numbers that are still available:")

for n in range(1, 16):
    if n in numbersTaken:
        continue
    print(n)