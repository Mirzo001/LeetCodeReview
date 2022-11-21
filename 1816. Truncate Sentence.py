s = "Hello how are you Contestant" 
k = 4

def truncateSentence(s: str, k: int) -> str:
    return ' '.join(s.split()[:4])
print(truncateSentence(s,k))


