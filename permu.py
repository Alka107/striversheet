def checkInclusion( s1, s2):
    s1 = list(s1)
    s1.sort()
    l = len(s1)
    for i in range(len(s2)-l+1):
        req = list(s2[i:i+l])
        req.sort()
        if req == s1:
            return (True)
    return False       
a=checkInclusion("ab", "eidbaooo")
print(a)