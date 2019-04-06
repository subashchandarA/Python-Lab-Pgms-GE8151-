#Program to circulate n values

def find_max(lt):
    
    max=0
    for x in lt:
        if(x > max):
            max=x
    return max    




n=int(input("Enter the number of values:"))


lt = []   # creation of empty list

#getting n values and store in a list

i=0
while(i<n):
    number=int(input("Enter a value to store:"))
    lt.append(number)
    i=i+1

print("The values are :",lt)

maximum_value = find_max(lt)

print("The maxumum of the list of values is :",maximum_value)

#Output
#Enter the number of values:5
#Enter a value to store:34
#Enter a value to store:23
#Enter a value to store:67
#Enter a value to store:45
#Enter a value to store:23
#The values are : [34, 23, 67, 45, 23]
#The maxumum of the list of values is : 67

