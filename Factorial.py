def factorial(number):
    if  number ==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)
    
number=int(input("Ente number : "))
result=factorial(number)
print("THe factotial of the given Number : ",result)