names = {"Sandro", "Giorgi", "Nika"}

name = input("შეიყვანე სახელი: ")

if name in names:
    print("ეს სახელი არის სეტში და აღარ დაემატება")
else:
    names.add(name)
    print(names)