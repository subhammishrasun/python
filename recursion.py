'''def factorial(n):
    if n==0:
        return 1
    ans=n*factorial(n-1)
    return ans
n=int(input("Enter n:"))
print("The factorial is:",factorial(n))'''

'''def print_one(n):
    #base case
    if n==0:
        return
    #print(n)
    #recursive case
    print_one(n-1)
    print(n)
print_one(5)'''

'''def sum(n):
    if n==1:
        return 1
    ans=n+sum(n-1)
    return ans
n=int(input("Enter n:"))
print(sum(n))'''

'''def power(a,b):
    #base case
    if b==0:
        return 1
    #recursive case
    ans=a*power(a,b-1)
    return ans
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print(power(a,b)) '''

#fibonacci series
'''def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
n=int(input("Enter n:"))
for i in range(1,n+1):
    print(fibonacci(i))'''

#string
from multiprocessing.reduction import recv_handle


str1="   hello world  "
#print(str1)

#list comphrensive
#list=[char for char in str1]
#for i in list:
 #   print(i)
#print(str1.find('d'))
#print(str1[6:])
#print(str1[-8:])
'''print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.strip())'''

#print(str1.replace("world","beautiful"))
str2="ria,mia, pia siya tiya"
#print(str2.split(",",2))
#print(str1+str2)
'''print("this girl name is {r}".format(r=str2))

text="The unexpected always happens"
print(text)
print(len(text))
print(text.find("pp"))
print(text[:11])
print(text.replace("always","never"))
str3=" no matter what"
str4=text+ str3
print(str4)'''

#palindrome or not
'''def palindrome(str):
    clean_str=(str.replace(" ","")).lower()
    reverse_str=clean_str[::-1]
    return clean_str==reverse_str
str=input("Enter a string:")
if palindrome(str):
    print("it is palindrome string")
else:
    print("it is not palindrome string")'''

str1="6/4"
print(type(str1))

     


