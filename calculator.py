# This is a calculator
name = input("Enter your name: ")
age = input('Enter your age: ')
favorite_number = int(input("Enter your favorite number: "))
mult = favorite_number * 10
print(f"Hello {name}! you are {age} years old.")
print(f"Your favorite number multiplied by 10 is {mult}.")
if favorite_number > 50:
    print("True, your favorite number is greater than 50.")
else:
    print("False, your favorite number is less than 50.")