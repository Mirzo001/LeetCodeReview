# def common(words):
#     if len(words) == 0:
#         return ''
#     if len(words) == 1:
#         return ''
#     prefix = words[0]
#     for l in prefix:
#         for x in l:
#             print(x)
#     for word in words:
#         print(letter)


# words = ['cooperative', 'coworking', 'cooking', 'cooling']
# minimumLength = len(words[0])
# # common(words)
# print(minimumLength)
strs=['cooperative', 'coworking', 'cooking', 'cooling']
def longestCommonPrefix(strs):
    # Longest common prefix string
    lcp = ""
    # Base condition
    if strs is None or len(strs) == 0:
        return lcp
    # Find the minimum length string from the array
    minimumLength = len(strs[0])
    for i in range(1, len(strs)):
        minimumLength = min(minimumLength, len(strs[i]))
    # Loop until the minimum length
    for i in range(0, minimumLength):
        # Get the current character from the first string
        current = strs[0][i]
        # Check if this character is found in all other strings or not
        for j in range(0, len(strs)):
            if strs[j][i] != current:
                return lcp
        lcp += current
    return lcp
print(longestCommonPrefix(strs))