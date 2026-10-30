for i in range(1, 11):
    print(f"Welcome to my shop customer {i}")

mycustomers = ("Mary", "Esther", "Betty", "Sarah", "Lee")

for n in mycustomers:
    print(f"Welcome to my school {n}")

# suppose you buy
# milk ksh100
# sugar ksh 200
# bread ksh 130
# blueband
# calculate total expense

my_shopping = [130, 100, 200, 120]
total = 0
for s in my_shopping:
    total = total + s
    
print(f"Total Shopping Expense: Ksh {total}")


# while loop
num = 0
while num <= 8:
    num += 1
    print(f"loop:{num}")

# imagine you start with 0 and save 100 everyday until you save 500
savings = 0
while savings < 500:
    savings = savings + 100
    print(f"Your saving goal of {savings} achieved")

battery = 0
print("Charger connected")
while battery < 100:
    battery += 25
    print(f"The current charging is {battery}")

print("the battery is full")