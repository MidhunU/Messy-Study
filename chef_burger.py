def manage_burger_stack(operations):
    stack = []
    output = []
    for op in operations:
        parts = op.split()
        command = parts[0]
        if command == "add":
            keyword = parts[1]
            stack.append(keyword)

        elif command == "remove":
            if not stack:
                output.append("Empty")
            else:
                stack.pop()

        elif command == "top":
            if not stack:
                output.append("Empty")
            else:
                output.append(stack[-1])

    return output



print("Chef's Burger")
n = int(input())
operation = [input().strip() for _ in range (n)]
result = manage_burger_stack(operation)

for res in result:
    print(res)
