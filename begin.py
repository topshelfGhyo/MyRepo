def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1-num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

print("Welcome To GhyoMetros Choose an Option!")
print("1. Add")
print("2. Subtract")
print("3. Divide")
print("4. Multiply")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    while choice in ("1",'2','3','4'):
        try:
            num1 = float(input('Enter first number '));print(num1)
            num2 = float(input('Enter second number'));print(num2)
        except ValueError:
            print("Invalid Entry Please Try again!")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice =='2':
            print(num1, '-', num2, "=",subtract(num1, num2))
        
        elif choice == '3':
            print(num1,"/",num2, "=", divide(num1, num2))

        elif choice =="4":
            print(num1,"*", num2, multiply(num1, num2))

           



        else:
            print("Invalid Entry!")
            






