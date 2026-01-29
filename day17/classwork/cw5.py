names = ["Sandro","Nika","luka","deme"]
username = input("Enter your name: ")
count = 0
for name in names:
    if name == username:
        print("username")
        count = count + 1
print(count)
