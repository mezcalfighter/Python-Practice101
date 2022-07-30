def fibonacci(prev_number,add_number):
    new_number = prev_number + add_number
    prev_number = add_number
    return prev_number, new_number

def getNthFib(n):
    # Write your code here.
    first = 0
    second = 1
    count = 0
    if n == 1:
        return first
    for index in range(n-2):
        print(second)
        first,second=fibonacci(first,second)
    return second

if __name__ == '__main__':
    n = 0
    print(getNthFib(n))