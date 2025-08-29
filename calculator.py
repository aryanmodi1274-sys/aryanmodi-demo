def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
     return "error division by zero"
    return x/y

print("Select The Operation To do:")
print("1.add")
print("2.Subtract")
print("3.multiply")
print("4.Divide")

choice = float(input("Enter Choice:(1/2/3/4): "))
num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))

if choice == 1:
   print("Result:",add(num1,num2))
elif choice == 2:
   print("Result:",substract(num1,num2))
elif choice == 3:
   print("Result:",multiply(num1,num2))
elif choice == 4:
   print("Result:",divide(num1,num2))
else:
   print("invalid input")
