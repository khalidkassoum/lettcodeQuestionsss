def isAnagram(s, t):
    if len(s) != len(t):
        return False
    Map1, Map2 = {}, {}
    for i in range(len(s)):
        Map1[s[i]] = 1 + Map1.get(s[i], 0)
        Map2[t[i]] = 1 + Map2.get(t[i], 0)
    for j in Map1:
        if Map1[j] != Map2.get(j, 0):
            return False
    return True
