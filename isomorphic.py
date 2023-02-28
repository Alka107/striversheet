def areIsomorphic(str1,str2):
    s=set(str1)
    p=set(str2)
    if len(s)!=len(p):
        return False
    d={}
    for i in range(len(str1)):
        if str1[i] in d:
            if d[str1[i]]!=str2[i]:
                return False
            
        else:
            d[str1[i]]=str2[i]
    
    return True
a=areIsomorphic("aab", "xxy")
print(a)