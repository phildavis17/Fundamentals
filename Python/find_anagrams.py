from collections import Counter


def findAnagrams(s: str, p: str) -> list:
    target_counter = Counter(p)
    found_indecies = []
    for i in range(len(s)):
        search_counter = Counter(s[i : i + len(p)])
        if search_counter == target_counter:
            found_indecies.append(i)
    return found_indecies

    123
    string

    Counter("str")
