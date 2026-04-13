"""Text validation helpers."""

import re


def has_min_words(text: str, min_words: int) -> bool:
    words = re.findall(r"[A-Za-z0-9']+", text)
    return len(words) >= min_words


def contains_keyword(text: str, keyword: str) -> bool:
    return keyword.lower() in text.lower()


def quality_score(text: str) -> int:
    score = 0
    if has_min_words(text, 8):
        score += 40
    if any(char.isdigit() for char in text):
        score += 20
    if text.endswith((".", "!", "?")):
        score += 20
    if len(text) >= 40:
        score += 20
    return score
