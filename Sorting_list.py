def Sorting_list(l1):
    for i in range(len(l1)):
        maximum=i
        for j in range(i+1,len(l1)):
            if l1[j] >l1[maximum]:
                maximum = j

        l1[i], l1[maximum]=l1[maximum],l1[i]
    return l1

l1=input()
l1=list(map(int,l1.split()))
result=Sorting_list(l1)
print(result)