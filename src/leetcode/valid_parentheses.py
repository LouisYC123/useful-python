# %%
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""

# %%
bracket_dict = {
    "(":")",
    "[":"]",
    "{":"}",
    ")":"(",
    "}":"{",
    "]":"[",
}

# %%
s = "()[]{}"
# s = "()"
# s = "(]"


pairs = [(s[i], s[i+1]) for i in range(0, len(s)-1, 2)]

[True for pair in pairs if ]


# %%
tracker = []
set_skip = False
for char in s:
    idx = s.index(char)
    if idx != len(s) -1:
        if set_skip:
            idx += 1
            set_skip = False
        if bracket_dict[char] == s[idx + 1]:
            tracker.append(True)
            set_skip = True
        else:
            tracker.append(False)
if all(tracker):
    print('success')
else:
    print('fail')
# %%
len(s)
# %%
