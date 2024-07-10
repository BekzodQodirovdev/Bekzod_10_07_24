def tek(s):
    stack = []
    remove_indexes = set()

    for i, char in enumerate(s):
        if char in '([{':
            stack.append((char, i))
        elif char in ')]}':
            if stack and ((char == ')' and stack[-1][0] == '(') or 
                        (char == ']' and stack[-1][0] == '[') or 
                        (char == '}' and stack[-1][0] == '{')):
                stack.pop()
            else:
                remove_indexes.add(i)

    remove_indexes.update(i for _, i in stack)
    return ''.join(char for i, char in enumerate(s) if i not in remove_indexes)

user_input = input("Enter : ")
result = tek(user_input)
print(f"Natija: {result}")
