def binary_search(array,target,low,high):
    mid=(low+high)//2
    if(low>high):
        return -1
    if(array[mid]==target):
        return mid
    elif(array[mid]>mid):
        low=mid+1
        return binary_search(array,target,low,high)
    elif(array[mid]<mid):
        high=mid-1
        return binary_search(array,target,low,high)
    
  
array=[10,20,30,40,50]
target=50
low=0 
high=len(array)-1
result=binary_search(array,target,low,high)  
if(result !=-1):
    print(f"Target found at {result}")
else:
    print("Not found")
 