def Palindrome(string):
   ''' if string==string[::-1]:
        return True
    return False'''
   return string==string[::-1]
string=input("Enter the string :")
result=Palindrome(string)
if result:
    print(f"{string} is a Palindrome")
else:
    print(f"{string} is not a Palindrome")
