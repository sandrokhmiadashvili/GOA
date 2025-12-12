#დაწერე პროგრამა რომელიც შეასრულებს რიხვების გაყოფას მაგრამ წილადის ნაცვლად ინტეჯერს გამოიტანს
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