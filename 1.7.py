first = int(input("First number: "))
operation = input("Operation: ")
second = int(input("Second number: "))
if second == 0 and operation == "/":
        print("error")
elif operation == "+":
    print(first + second)
elif operation == "-":
    print(first - second)
elif operation == "*":
    print(first * second)
elif operation == "/":
    print(first / second)

