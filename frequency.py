'''''def count_frequency(l1):
    freq = {}
    for item in l1:
        freq[item] = freq.get(item, 0) + 1
    return freq

l1=input()
l1=list(map(int,l1.split()))
print(count_frequency(l1))'''''

from collections import Counter
l1=input()
l1=list(map(int,l1.split()))
print(Counter(l1))
