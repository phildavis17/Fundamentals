"""
is the string valid?
normal rules for parens, but * can be a wildcard.
"""

import logging

logging.basicConfig(level=logging.DEBUG)


def paren_test_wc(s: str) -> bool:
    ops = []
    cps = []
    ast = []

    stacks = {
        "(": ops,
        ")": cps,
        "*": ast,
    }

    for i, c in enumerate(s):
        assert c in stacks
        if c == "(":
            ops.append(i)
        if c == ")":
            if ops:
                ops.pop()
            else:
                cps.append(i)
        if c == "*":
            ast.append(i)

    for i in ops:
        for a in ast:
            if i < a:
                pass


def paren_test(s: str) -> bool:
    stack = []
    for c in s:
        if c == "(":
            stack.append(")")
        elif stack and c == ")":
            stack.pop()
        elif c == ")":
            return False
    return not stack


def checkValidString(s):
    lo = hi = 0
    for c in s:
        lo += 1 if c == "(" else -1
        hi += 1 if c != ")" else -1
        if hi < 0:
            break
        lo = max(lo, 0)
    return lo == 0


def check_lc_pd(s):
    low, high = 0, 0
    for c in s:
        if c == "(":
            low += 1
            high += 1
        if c == ")":
            low += -1
            high += -1
        if c == "*":
            high += 1
            low += -1
        if not high >= 0:
            break
        low = max(low, 0)
    return low == 0


GOOD_STRS = [
    "",
    "()",
    "(())",
    "()()",
    "*",
    "****",
    "()*",
    "*()",
    "(*)",
    "(*",
    "((*)",
    "*)",
    "*)(*",
    "*)*(*",
    "(*)*(*)",
    "***())))",
]

BAD_STRS = [
    "(",
    "()(",
    "((",
    ")",
    ")(",
    "*(",
    "*(*(",
    ")*****(",
]


if __name__ == "__main__":
    try:
        assert all([check_lc_pd(s) for s in GOOD_STRS])
        logging.debug("GOOD passes!")
    except AssertionError:
        for t in [s for s in GOOD_STRS if not check_lc_pd(s)]:
            logging.warning(f"Error: {t} = {check_lc_pd(t)}")

    try:
        assert not any([check_lc_pd(s) for s in BAD_STRS])
        logging.debug("BAD passes!")
    except AssertionError:
        for t in [s for s in BAD_STRS if check_lc_pd(s)]:
            logging.warning(f"Error: {t} = {check_lc_pd(t)}")


"""

What are the rules?
 - go through and try to balance it the normal way
 - if there is a residual stack, try to apply asterisks to it

"""
