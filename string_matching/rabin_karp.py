def rabin_karp(text: str, pattern: str) -> list:
    n, m = len(text), len(pattern)
    if m > n or m == 0:
        return []
    
    p = 101 
    b = 256
    result = []
    pattern_hash = hash_function(pattern)
    window_hash = hash_function(text[:m])
    
    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                result.append(i)
        if i < n - m:
            left = ord(text[i]) * pow(b, m - 1, p)
            window_hash = (b * (window_hash - left) + ord(text[i + m])) % p
            window_hash = (window_hash + p) % p  
    return result

def hash_function(string: str) -> int:
    n = len(string)
    p = 101
    b = 256
    
    H = sum(ord(c) * pow(b, n - i - 1) for i, c in enumerate(string)) % p
    
    return H
    
if __name__ == "__main__":
    text = "ABACABABABAB"
    pattern = "ABAB"

    print(f"String occurs at {rabin_karp(text, pattern)}")
