print('Welcome to the Mini Bio Generator!')
name = input("Enter your name: ").lower().strip()
age = input('Enter your age: ')
favourite_number = input('Enter your favourite number: ')
hobby = input('Write a short sentence about your hobby: ')
print(f"Lower case name: {name}")
print(f"Upper case name: {name.upper()}")
print(f"First three letters of your name: {name[:3]}")
space_cup =[]
non_space_cup = []
new_hobby = ''
for i, space in enumerate(hobby):
    if space == " ":
        space_cup.append(space)
        new_hobby += "❤"
    else:
        non_space_cup.append(space)
        new_hobby += space
print(f"Modified hobby with emoji: {new_hobby}")