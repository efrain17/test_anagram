""""fun_with_anagrams controller"""

def fun_with_anagrams(text):
    """Anagrams controll"""
    for word in text:
        for word2 in text[text.index(word) + 1:len(text)]:
            if sorted(list(word)) == sorted(list(word2)):
                text.remove(word2)
    return sorted(text)
