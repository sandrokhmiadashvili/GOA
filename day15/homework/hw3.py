#მომხმარებელს შემოატანინეთ მისი ასაკი და ასევე მისი სახელი, თუ მომხმარებლის სახელი ემთხვევა თქვენს სახელს და ასევე მისი ასაკი ემთხვევა თქვენს სახელს, დაბეჭდეთ "Twins" სხვა შემთხვევაში "Not Twins".
my_name = "Sandro"
my_age = 13

user_name = input("შეიყვანე შენი სახელი: ")
user_age = int(input("შეიყვანე შენი ასაკი: "))


if user_name == my_name and user_age == my_age:
    print("Twins")
else:
    print("Not Twins")
