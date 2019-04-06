def isprime(x):
    #print("function   ",x)
    i=2
    while( i < x):
        if(x % i == 0):
            return False
        i=i+1
    else:
        return True


n=int(input("Enter the number of prime numbers to print: "))
count=0
i=2 #considering 2 as the firts prime number 

print("The %d Prime number as follows:"%n)
while(count<n):
        if(isprime(i)):
               print(i,end="  ")
               count=count+1
        i=i+1
    
print("\n Thank You !!! ")

#Output
#Enter the number of prime numbers to print: 6
#The 6 Prime number as follows:
#2  3  5  7  11  13  
# Thank You !!! 


