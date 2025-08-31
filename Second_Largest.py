def second_largest(l1):
    ##return sorted(set(l1))[-2]
    maximum = float('-inf')
    second_maximum = float('-inf')
    for i in l1:
        if i > maximum:
            second_maximum, maximum = maximum, i
        elif maximum > i > second_maximum:
            second_maximum = i
    return second_maximum

l1=input()
l1=list(map(int,l1.split()))
print(second_largest(l1))
