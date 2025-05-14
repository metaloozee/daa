def naive(text: str, pattern: str) -> list:
    ans = []
    
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if (text[i + j] != pattern[j]):
                match = False
                break
        if match:
            ans.append(i)

    return ans
    
if __name__ == "__main__":
    text = "ABACABABABAB"
    pattern = "ABAB"
    
    print(f"String occurs at {naive(text, pattern)}")

