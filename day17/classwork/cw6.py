numbers = [7, 10, 12, 15, 18, 21, 32, 43, 56, 70, 83]
jami = 0
for num in numbers:
    if num % 2 == 0:
        jami += num
print(jami)