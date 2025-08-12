paragraph = input("insert a paragraph of your choice: ").lower().strip()
count = 0
if 'p' in paragraph:
    count = paragraph.count('p')
    print(f"There are {count} p's in your sentence")
    position = [] 

    for i, char in enumerate(paragraph):
        if char == 'p':
            position.append(i + 1)
    print(f"The postions of 'p' is {position}")
    
else:
    print('there is no p')