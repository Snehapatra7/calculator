Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(x, y):
...     return x + y
... 
... def subtract(x, y):
...     return x - y
... 
... def multiply(x, y):
...     return x * y
... 
... def divide(x, y):
...     if y == 0:
...         return "Error! Division by zero."
...     return x / y
... 
... def calculator():
...     print("Welcome to the Simple Calculator!")
...     print("Select an operation:")
...     print("1. Addition")
...     print("2. Subtraction")
...     print("3. Multiplication")
...     print("4. Division")
... 
...     while True:
...         choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")
... 
...         if choice == 'q':
...             print("Exiting the calculator. Goodbye!")
...             break
...         
...         if choice in ('1', '2', '3', '4'):
...             try:
...                 num1 = float(input("Enter first number: "))
...                 num2 = float(input("Enter second number: "))
...             except ValueError:
...                 print("Invalid input! Please enter a number.")
...                 continue
...             
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid operation.")
