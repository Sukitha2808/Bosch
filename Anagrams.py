def anagrams(s1,s2):
    return sorted(s1)==sorted(s2)
print(anagrams("listen","silent"))
print(anagrams("hello","world"))

'''''from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

print(is_anagram("listen", "silent"))'''''
