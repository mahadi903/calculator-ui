# Calculator in Python

# Function to add two numbers
def add(x, y):
   return x + y

# Function to subtract two numbers
def subtract(x, y):
   return x - y

# Function to multiply two numbers
def multiply(x, y):
   return x * y

# Function to divide two numbers
def divide(x, y):
   if y == 0:
      raise ValueError("Cannot divide by zero!")
   else:
      return x / y

# Take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
   try:
      choice = int(input("Enter choice (1/2/3/4): "))
      if choice in [1, 2, 3, 4]:
         break
      else:
         print("Invalid input")
   except ValueError:
      print("Invalid input")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
   print(num1, "+", num2, "=", add(num1, num2))

elif choice == 2:
   print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == 3:
   print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == 4:
   try:
      print(num1, "/", num2, "=", divide(num1, num2))
   except ValueError as e:
      print("Error:", e)

else:
   print("Invalid input")

