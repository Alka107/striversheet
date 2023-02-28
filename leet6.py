def reverseWords(s):
    #s = s.split()
    x=s[::-1]
    l = []
    for i in x:
        
        l.append(i)
    
    return(" ".join(l))
a=reverseWords("the sky is blue")
print(a)