paragraph = input("insert a paragraph of your choice: ").lower().strip()
count = 0
if 'p' in paragraph:
    count += 1
    print(f"There are {count} p's in your sentence")
    
else:
    print('there is no p')