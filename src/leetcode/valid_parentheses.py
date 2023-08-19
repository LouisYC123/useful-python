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

def validate_string(s: str):
    stack = []
    pairs = {
        '(':')',
        '{':'}',
        '[':']',
    }
    for bracket in s:
        if bracket in pairs.keys():
            stack.append(bracket)
        else:
            if len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False
    return len(stack) == 0

validate_string("()[{}]")

# %%
