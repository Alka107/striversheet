def shortestDistance( s, word1, word2):
    d1 = -1
    d2 = -1
    ans = len(s)
    
    for i in range(len(s)):
        if(s[i] == word1):
            d1 = i
        if(s[i] == word2):
            d2 = i
        if(d1 != -1 and d2 != -1):
            ans = min(ans, abs(d1-d2))
    
    return ans
a=shortestDistance(["the", "quick", "brown", "fox",  "quick"] ,"the",  "fox")
print(a)