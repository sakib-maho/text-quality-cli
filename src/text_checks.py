"""Text quality scoring helpers."""

from __future__ import annotations

from collections import Counter
import math
import re


WORD_RE = re.compile(r"[A-Za-z0-9']+")
SENTENCE_RE = re.compile(r"[^.!?]+[.!?]?")


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def has_min_words(text: str, min_words: int) -> bool:
    return len(words(text)) >= min_words


def contains_keyword(text: str, keyword: str) -> bool:
    return keyword.lower() in text.lower()


def avg_sentence_length(text: str) -> float:
    sentences = [s.strip() for s in SENTENCE_RE.findall(text) if s.strip()]
    if not sentences:
        return 0.0
    return sum(len(words(s)) for s in sentences) / len(sentences)


def flesch_approx(text: str) -> float:
    """Rough readability proxy (not full syllable Flesch)."""
    w = words(text)
    sentences = max(1, len([s for s in SENTENCE_RE.findall(text) if s.strip()]))
    if not w:
        return 0.0
    # Approximate syllables by vowel groups.
    syllables = 0
    for word in w:
        syllables += max(1, len(re.findall(r"[aeiouy]+", word.lower())))
    return 206.835 - 1.015 * (len(w) / sentences) - 84.6 * (syllables / len(w))


def duplicate_word_ratio(text: str) -> float:
    w = [token.lower() for token in words(text)]
    if not w:
        return 0.0
    counts = Counter(w)
    dupes = sum(count - 1 for count in counts.values() if count > 1)
    return dupes / len(w)


def passive_voice_hits(text: str) -> int:
    return len(re.findall(r"\b(?:was|were|be|been|being)\s+\w+ed\b", text.lower()))


def quality_report(text: str, keyword: str | None = None) -> dict:
    w = words(text)
    report = {
        "word_count": len(w),
        "char_count": len(text),
        "avg_sentence_length": round(avg_sentence_length(text), 2),
        "readability_approx": round(flesch_approx(text), 2),
        "duplicate_word_ratio": round(duplicate_word_ratio(text), 3),
        "passive_voice_hits": passive_voice_hits(text),
        "ends_with_punctuation": text.strip().endswith((".", "!", "?")),
        "has_digits": any(ch.isdigit() for ch in text),
        "keyword_found": contains_keyword(text, keyword) if keyword else None,
        "score": 0,
        "flags": [],
    }

    score = 0
    if report["word_count"] >= 8:
        score += 25
    else:
        report["flags"].append("too_short")
    if report["ends_with_punctuation"]:
        score += 15
    else:
        report["flags"].append("missing_terminal_punctuation")
    if report["avg_sentence_length"] <= 25:
        score += 15
    else:
        report["flags"].append("long_sentences")
    if report["duplicate_word_ratio"] <= 0.2:
        score += 15
    else:
        report["flags"].append("repeated_words")
    if report["passive_voice_hits"] <= 1:
        score += 10
    else:
        report["flags"].append("passive_voice")
    if report["readability_approx"] >= 40:
        score += 10
    if report["has_digits"]:
        score += 5
    if keyword:
        if report["keyword_found"]:
            score += 5
        else:
            report["flags"].append("missing_keyword")

    report["score"] = min(100, score)
    return report


def quality_score(text: str) -> int:
    return int(quality_report(text)["score"])
