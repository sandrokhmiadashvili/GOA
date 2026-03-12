numbers = [1,2,3,4,5,6,7,8,9,10]

index = int(input("შეიყვანე ინდექსი (1-5): "))

value = numbers[index]
numbers.remove(value)

numbers.insert(0, "change")

print(numbers)