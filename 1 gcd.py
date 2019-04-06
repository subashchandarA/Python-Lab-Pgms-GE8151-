def gcd(m,n):
    "recursive function to find GCD of two numbers"
    if(m % n ==0 ):
        return n
    else:
        return(gcd(n,m%n))

a=int(input("Enter the first number to find GCD "))
b=int(input("Enter the second number to find GCD "))
result=gcd(a,b)
print("GCD of ",a," and ",b," is :",result)


#output1

#Enter the first number to find GCD 56
#Enter the second number to find GCD 781
#GCD of  56  and  781  is : 1

#output2
#Enter the first number to find GCD 45
#Enter the second number to find GCD 9
#GCD of  45  and  9  is : 9
