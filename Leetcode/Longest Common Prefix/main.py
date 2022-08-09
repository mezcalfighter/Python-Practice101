def longestCommonPrefix(strs):
        longest = ''
        if len(strs) == 0:
            return ''
        for index in range(len(strs[0])):
            temp_longest = strs[0][index]
            for item in strs:
                if temp_longest != item[index]:
                    return longest
            longest += temp_longest

if __name__ == '__main__':
    print(longestCommonPrefix(strs = ["flower","flow","flight"]))
    print(longestCommonPrefix(strs = [""]))