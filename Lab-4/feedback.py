from collections import Counter


def evaluate(target, guess):
    if len(target) != len(guess):
        raise ValueError("target and guess must be the same length")

    result = ["gray"] * len(guess)
    unmatched = Counter()

    # Pass 1: exact matches are green; count target letters not matched exactly
    for i, (t_ch, g_ch) in enumerate(zip(target, guess)):
        if g_ch == t_ch:
            result[i] = "green"
        else:
            unmatched[t_ch] += 1

    # Pass 2: yellow only if an unmatched copy is still available
    for i, g_ch in enumerate(guess):
        if result[i] == "green":
            continue
        if unmatched[g_ch] > 0:
            result[i] = "yellow"
            unmatched[g_ch] -= 1

    return result