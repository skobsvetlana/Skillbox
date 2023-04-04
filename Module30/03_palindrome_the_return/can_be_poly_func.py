from collections import Counter
def can_be_poly(word: str) -> bool:
    return len(word) % 2 == sum(x % 2 for x in Counter(word).values())