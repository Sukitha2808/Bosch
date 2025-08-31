'''''def fibonacci(n):
    if n==0:
        return []
    elif n==1:
        return [1]
    l1=[0,1]
    for i in range(2,n):
        x=l1[i-1]+l1[i-2]
        l1.append(x)
    return l1
n=int(input())
result=fibonacci(n)
print(result)'''''


'''''def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
n=int(input())
fibonacci(n)'''''


'''''def fibonacci(n):
    a,b=0,1
    count=0
    while(count<n):
        print(a,end=" ")
        a,b=b,a+b
        count+=1
n=int(input())
fibonacci(n)'''''


def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
n=int(input())
for i in range(n):
    print(fibonacci(i), end=" ")

