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
        assert all([paren_test_wc(s) for s in GOOD_STRS])
        logging.debug("GOOD passes!")
    except AssertionError:
        for t in [s for s in GOOD_STRS if not paren_test_wc(s)]:
            logging.warning(f"Error: {t} = {paren_test_wc(t)}")

    try:
        assert not any([paren_test_wc(s) for s in BAD_STRS])
        logging.debug("BAD passes!")
    except AssertionError:
        for t in [s for s in BAD_STRS if paren_test_wc(s)]:
            logging.warning(f"Error: {t} = {paren_test_wc(t)}")
