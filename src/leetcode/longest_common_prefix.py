# %% 14. Longest Common Prefix

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"

"""


strs = ["flower", "flow", "flight"]
strs = ["dog", "racecar", "car"]
common_prefix = []
idx = 1
for i in range(len(max(strs))):
    for word in strs:
        if i < len(word):
            if all(word[:idx] in string for string in strs):
                common_prefix.append(word[:idx])
    idx += 1
if common_prefix:
    print(max(common_prefix))
else:
    print("")
