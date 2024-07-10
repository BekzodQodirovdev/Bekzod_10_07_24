# -----------------------------------1 - misol ----------------------------------------
# def tek(s):
#     stack = []
#     remove_indexes = set()

#     for i, char in enumerate(s):
#         if char in '([{':
#             stack.append((char, i))
#         elif char in ')]}':
#             if stack and ((char == ')' and stack[-1][0] == '(') or 
#                         (char == ']' and stack[-1][0] == '[') or 
#                         (char == '}' and stack[-1][0] == '{')):
#                 stack.pop()
#             else:
#                 remove_indexes.add(i)

#     remove_indexes.update(i for _, i in stack)
#     return ''.join(char for i, char in enumerate(s) if i not in remove_indexes)

# user_input = input("Enter : ")
# result = tek(user_input)
# print(f"Natija: {result}")

# -----------------------------------2 - misol ----------------------------------------

# def eng_katta_faq(n):
#     if len(n) < 2:
#         return None, None, None
    
#     max = 0
#     index = 0

#     for i in range(len(n) - 1):
#         diff = abs(n[i] - n[i + 1])
#         if diff > max:
#             max = diff
#             index = i

#     return index, n[index], n[index + 1]

# n = list(map(int, input().split()))

# index, val1, val2 = eng_katta_faq(n)

# if index is not None:
#     print(f"{val2-val1}({val1} va {val2})")
# else:
#     print("Listda kamida 2 ta element bo'lishi kerak.")

# -----------------------------------3 - misol ----------------------------------------


def fun(file_name, symbol):
    if symbol in "*":
        return True

    parts = symbol.split('*')
    start_index = 0

    for part in parts:
        i = 0
        while i < len(part) and start_index < len(file_name):
            if part[i] == '?':
                start_index += 1
            elif part[i] != file_name[start_index]:
                return False
            else:
                start_index += 1
            i += 1
        
        if i < len(part):
            return False

        while start_index < len(file_name) and file_name[start_index] != part[0]:
            start_index += 1

    return True


file_name = input("File name: ")
syml = input("Enter Symbol(* or ? or txt): ")

resualt = fun(file_name,syml)
print(resualt)
