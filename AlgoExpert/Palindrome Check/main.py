def isPalindrome(string):
    # Write your code here.
    item1 = list(string)
    new_string = item1.copy()
    new_string.reverse()
    print(new_string)
    print(item1)
    if item1 == new_string:
        return True
    return False

if __name__ == '__main__':
    #string = "abcdcba"
    string = "ab"
    print(isPalindrome(string))