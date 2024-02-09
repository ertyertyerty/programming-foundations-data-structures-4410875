from collections import deque

def check_matching_parentheses(sample):
    dubdeque = deque(sample)
    count = 0
    while len(dubdeque) > 0:
        leftchar = dubdeque.popleft()
        # print(leftchar)
        if leftchar == '(':
            count = count + 1
        if leftchar == ')':
            count = count - 1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False

print(f"Answer: {check_matching_parentheses('((sdlf))ksdf')}")
print(check_matching_parentheses("()"))
print(check_matching_parentheses("(hi there)"))
print(check_matching_parentheses("(hell)o"))
print(check_matching_parentheses("((linkedin)) learning"))

print(check_matching_parentheses("(hi(there"))
print(check_matching_parentheses("()ok)"))
print(check_matching_parentheses("((increment)"))
print(check_matching_parentheses(")linkedin()"))
