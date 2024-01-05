changes = []

def apply_operation(user_input, operation):
    global changes
    if operation == 'U':
        result = user_input.upper()
        changes.append(operation)
    elif operation == 'L':
        result = user_input.lower()
        changes.append(operation)
    elif operation.startswith('C'):
        ch1, ch2 = operation[2], operation[4]
        result = user_input.replace(ch1, ch2)
        changes.append({'cmd': 'C', 'name': ch1, 'val': ch2})
    elif operation == 'R':
        result = user_input[::-1]
        changes.append(operation)
    else:
        result = user_input
        changes.append(operation)
    return result

def edit_string(user_input):
    global changes
    result = user_input
    operation = ""

    while operation != 'X':
        operation = input("Enter an operation (U, L, C, R, Z, or X to exit): ")

        if operation == 'Z':
            if len(changes) > 0:
                last_change = changes.pop()
                # print(last_change)
                if type(last_change) == dict:
                    result = apply_operation(user_input=result, operation=f"C {last_change['val']} {last_change['name']}")
                else:
                    result = apply_operation(user_input=result, operation=last_change)
            else:
                print("Cannot redo. No previous operation.")
        elif operation != 'X':
            result = apply_operation(user_input=result, operation=operation)

        print("Result:", result)
        # print("Changes:", changes)

    print("Final Resultant string:", result)

user_input = input("Enter a string: ")
edit_string(user_input=user_input)
