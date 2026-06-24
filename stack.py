# Backpack problem
def backpack():
    stack = []
    while True:
        inp = input("> ").strip()
        parts = inp.split()
        command = parts[0]

        if command == "ADD":
            keyword = parts[1]
            stack.append(keyword)    
            print(f"Added {keyword} to the backpack!")

        elif command == "DROP":
            if stack:
                print(f"Dropped {stack[-1]}")
                stack.pop()
            else:
                print("Empty Bag")

        elif command == "CHECK":
            if stack:
                print(stack[-1])
            else:
                print("Empty Bag")

print("Welcome to the Backpack!")
print ("You can\n1.ADD items to the bag.\n2.CHECK for items.\n3.DROP items.")
print("These commands help you to USE the bag.")
backpack()
