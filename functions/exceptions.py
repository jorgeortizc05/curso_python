import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Erro: Invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError: #Si divido para cero
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")