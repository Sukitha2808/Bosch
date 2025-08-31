def function(**kwargs):
    count=0
    for v in kwargs.values():
        count += v
    return count
   ## count=sum(kwargs.values())
    

result=function(a=1,b=1,c=5,d=2,e=5)
print(result)