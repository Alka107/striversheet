def longestCommonPrefix(strs):
    x=""
    if len(strs) ==0:
        return x
    for i in range(len(strs[0])):
        t=strs[0][i]
    for j in range(1,len(strs)):
        if t != strs[j][i]:
            return x
    x+=t
    return x
a=longestCommonPrefix(["flower","flow","flight"])
print(a)

    