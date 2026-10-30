
# LIST DATA STRUCTURE
# A list stores multiple items in one variable.
# Lists are ordered, allow duplicates, and can be changed.

products = ["milk", "sugar", "Bread", "blueband"]
print(f"My products: {products}")

products[0] = "cake"
print(f"My updated products: {products}")

products.pop()
print(products)

for p in products:
    print(p)


# TUPLE DATA STRUCTURE
# Immutable means unchangeable.
# Tuples are useful for items that do not change.

locations = ("Nairobi", "Mombasa", "Kisumu", "Arusha")
print(locations)


# SET DATA STRUCTURE
# A set stores unique items, meaning duplicates are removed.

my_stock = {"Hp", "Dell", "lenovo", "Hp"}
print(my_stock)


# DICTIONARY DATA STRUCTURE
# A dictionary stores information as key-value pairs.

customer = {
    "Id": "42862227",
    "Name": "Mary",
    "profession": "Software Eng",
    "age": "21"
}

print(f"Name: {customer['Name']}")


# STORE PRODUCTS AND THEIR PRICES

shop = {
    "Bread": 130,
    "Milk": 100,
    "sugar": 140
}

for product, price in shop.items():
    # .items() accesses each key and its value.
    print(product, "cost Ksh", price)

print("Milk cost Ksh", shop["Milk"])
fee_balances={
    "Leah":4500,
    "Rachael":6790,
    "Martin":8900
}
for student,fee in fee_balances.items():
    print(student,"fee remaning  is Ksh",fee )


# CALCULATE AVERAGE MARKS
# A loop adds all the marks, then we calculate the average.

marks = [76, 83, 67, 90, 79]
total = 0

for mark in marks:
    total = total + mark

average = total / len(marks)

print(f"Total marks: {total}")
print(f"Average mark is: {average}")


# CALCULATOR USING INPUTOUTPUT AND LOOPS
