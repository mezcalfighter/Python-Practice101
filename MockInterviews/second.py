# Parentesis 
# valid "{{(())}([])}{}[](()())" 
# valid "()[]{}"
# valid "([((((([[[((()()))]]])))))])"
# invalid "(]"
# invalid ")("
# invalid "[{(})]"



# def is_valid(s):
#     d = {'(' : ')', '{': '}', '[' : ']'}
#     stack = []
#     for i in s:
#       if i in d:
#         stack.append(i)
#       elif len(stack) == 0 or d[stack.pop()] != i:
#         return false
#     return len(stack) == 0