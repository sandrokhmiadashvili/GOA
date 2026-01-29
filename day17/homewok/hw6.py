numbers = [5, -3, 0, 7, -1, 0, 4]

positive = 0
negative = 0

for num in numbers:
    if num > 0:
        positive += num
    elif num < 0:
        negative += 1
    else:
        print("zero")

print(positive)
print(negative)
