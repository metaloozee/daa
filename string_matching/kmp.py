def kmp(text: str, pattern: str) -> list:
    m, n = len(pattern), len(text)
    i, j = 0, 0

    ans = []
    lps_array = lps(pattern)
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == m:
                ans.append(i - j)
                j = lps_array[j - 1]
        else:
            if j != 0:
                j = lps_array[j - 1]
            else:
                i += 1
    return ans

def lps(pattern: str) -> list:
    m = len(pattern)
    lps = [0] * m
    j = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps

if __name__ == "__main__":
    text = "ABACABABABAB"
    pattern = "ABAB"

    print(f"String occurs at {kmp(text, pattern)}")
