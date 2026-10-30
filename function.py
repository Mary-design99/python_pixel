def grett():
    print("Welcome to moringa")
    grett()
def student(name,age):
    print(f"my name is{name} i am {age} years old")
    student("Mercy", 20)
def add_numbers(a,b):
    return a+b
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
results=add_numbers(num1,num2)
print(f"the sum is {results}")
#create a program that gives 10% discount
def calculate_discount(amount):
    discount=0.1*amount
    final_price=amount-discount
    return final_price
amount=float(input("Enter the price:"))
total=calculate_discount(amount)
print(f"The price after discount is{total}")