def rotateString(s, goal):
    for i in range(len(s)):
        if s[i] == goal[0]:
            if s[i:] + s[:i] == goal:
                return True
    return False
a=rotateString("abcde" , "cdeab")
print(a)