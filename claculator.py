a = float(input("enter first number : "))
op = input("choese +,-,*,/,% : ")
b = float(input("enter second number : "))
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("not divisible by zero")
elif op == "%":
    print(a % b)
else:
    print("invalid opreator")
