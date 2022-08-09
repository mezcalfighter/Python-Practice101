def strStr(haystack,needle):
    haystack = list(haystack)
    first_item = needle[0]
    for index in range(len(haystack)):
        if first_item == haystack[index]:
            final = index+len(needle)-1
            str_temp = "".join(haystack[index-1:final])
            print("NEEDLE:{} STRING:{}".format(needle,str_temp))
            if needle == "".join(haystack[index-1:final]):
                return index - 1
    return -1

if __name__ == '__main__':
    print(strStr(haystack = "hello", needle = "ll"))