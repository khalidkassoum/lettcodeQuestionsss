def length_of_longest_substring(s):
    char_map = {}
    lastIndex = -1
    maxx = 0

    for i in range(len(s)):

        if s[i] in char_map and char_map[s[i]] > lastIndex:
            left = char_map[s[i]]
        char_map[s[i]] = i
        maxx = max(maxx, i - lastIndex)

    return maxx

if __name__ == "__main__":

 print(length_of_longest_substring("abcabcbb"))
 print(length_of_longest_substring("bbbbb"))
