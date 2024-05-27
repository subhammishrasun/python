#n=int(input("Enter n:"))
#for _ in range (n):
   # print("*" * 5)

'''n=int(input("Enter n:"))
for i in range(n):
    for j in range(1,n+1):
        print(j ,end="")
    print()  ''' 
'''n=int(input("Enter n:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print() '''

'''ascii=int(input("Enter number:"))
for i in range(65,ascii+1):
    for j in range(65,i+1):
        print(j,end="")
    print()'''

'''d={"key1":"apple","key2":"orange"}
print(d)'''

n=int(input("Enter n:"))

for i in range(1,n+1):
    print(" "*(n-i),end="" )
    for j in range(1,2*i):
        print(j,end="")
    print()