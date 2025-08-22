import random

def print_skull_love_grid():
    # Ask user for grid size
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    skull = "💀"
    love = "❤️"

    # Random position for love emoji
    love_row = random.randint(0, rows - 1)
    love_col = random.randint(0, cols - 1)

    for r in range(rows):
        for c in range(cols):
            if r == love_row and c == love_col:
                print(love, end=" ")
            else:
                print(skull, end=" ")
        print()  # new line after each row

print_skull_love_grid()
