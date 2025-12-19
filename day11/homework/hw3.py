#მომხმარებელს შემოატანინეთ ორი რიცხვი (num1 და num2) და გაიგეთ რა იქნება ნაშთი, პირველი რიცხვის
#მეორეზე გაყოფის შემდეგ

operatiors = input("შეიყვანეთ ოპერატიული (+,-,*,/)")
num = float(input("შეიყვანეთ პირველი რიცხვი:"))
Num1 = float(input("შეიყვანეთ მეორე რიცხვი:" ))
Num2 = float(input("შეიყვანეთ მესამე რივხვი:" ))


if operatiors == "+":
    print(num +Num1 + Num2)

elif operatiors == "-":
    print(num - Num1 - Num2)

elif operatiors =="/":
    print(num / Num1 / Num2)

elif operatiors =="*":
    print(num * Num1 * Num2)