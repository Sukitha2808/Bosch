def largest_smallest(l):
    maximum= float('-inf')
    minimum= float('inf')
    for i in l:
        if i > maximum:
            maximum=i
        if i < minimum:
            minimum=i
    return f"{maximum} is the Largest element in the list and {minimum} is the Smallest element in the list"

l1=input()
l1=list(map(int,l1.split()))
result=largest_smallest(l1)
print(result)