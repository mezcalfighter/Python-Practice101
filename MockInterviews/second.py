# Parentesis 
# valid "{{(())}([])}{}[](()())" 
# valid "()[]{}"
# valid "([((((([[[((()()))]]])))))])"
# invalid "(]"
# invalid ")("
# invalid "[{(})]"
def is_valid(string_input):
    hash = {
        '{':'}',
        '[':']',
        '(':')',
    }
    stack = []
    for item in string_input:
        if item in hash:
            stack.append(item)
        elif len(stack) == 0 or hash[stack.pop()] != i:
            return False
    return len(stack) == 0


if __name__ == '__main__':
    print(is_valid('{{(())}([])}{}[](()())'))
    print(is_valid('[{(})]'))
# def is_valid(s):
#     d = {'(' : ')', '{': '}', '[' : ']'}
#     stack = []
#     for i in s:
#       if i in d:
#         stack.append(i)
#       elif len(stack) == 0 or d[stack.pop()] != i:
#         return false
#     return len(stack) == 0