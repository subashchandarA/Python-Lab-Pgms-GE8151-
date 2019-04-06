def find_power(a,b):
    " function to find a raise to the power b "
    i=1
    result=1
    while(i<=b):
        result=result * a
        i=i+1
    return result


a=int(input("Enter the base value : "))
b=int(input("Enter the power : "))
power = find_power(a,b)
print(a," raise to the power ",b," is : ",power)


#Output
#Enter the base value : 5
#Enter the power : 4
#5  raise to the power  4  is :  625



