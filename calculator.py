# This is a calculator
name = input("Enter your name: ")
age = input('Enter your age: ')

print(f"Hello {name}! you are {age} years old.")
rule = True
while True:
    favorite_number = int(input("Enter your favorite number: "))
    mult = favorite_number * 10
    print(f"Your favorite number times 10 is {mult}")
    response = input("Do you want to try another favorite number? (yes/no)").lower().strip()
    if response == "yes" or response == "y":
        continue
    elif response == "no" or response == "n":
        break
    else:
        continue
if favorite_number > 50:
    print("True, your favorite number is greater than 50.")
else:
    print("False, your favorite number is less than 50.")