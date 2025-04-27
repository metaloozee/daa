def naive(text: str, pattern: str):
    n = len(text)
    m = len(pattern)

    occurrences = []

    if m > n:
        return occurrences

    for s in range(n - m + 1):
        match = True
        for j in range(m):
            if text[s + j] != pattern[j]:
                match = False
                break
        
        if (match):
            occurrences.append(s)

    return occurrences