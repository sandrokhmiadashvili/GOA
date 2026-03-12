nums = [10, 20, 30, 40, 50]

fav = int(input("შემოიტანეთ თქვენი საყვარელი რიცხვი: "))
index = int(input("შემოიტანეთ ინდექსი: "))

if 0 <= index < len(nums):
    nums.insert(index, fav)
    print("სიაში ახლაა:", nums)
else:
    print("invalid index")