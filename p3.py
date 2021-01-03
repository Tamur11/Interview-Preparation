def is_string_balanced(string):
    stack = []
    for char in string:
        if char == "(":
            stack.append("(")
        elif char == ")":
            try:
                stack.pop()
            except:
                return False
    return True if not stack else False

string = "(())"

print(is_string_balanced(string))