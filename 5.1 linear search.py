#Program for linear search

def linear_search(lt,search):
    
    max=0
    for x in lt:
        if(x == search):
            return True
    return False   


n=int(input("Enter the number of values:"))


lt = []   # creation of empty list

#getting n values and store in a list

i=0
while(i<n):
    number=int(input("Enter a value to store:"))
    lt.append(number)
    i=i+1


search_element=int(input("\n\nEnter the search value :"))


if(linear_search(lt,search_element)):
   print("The search element ",search_element," is available in the list ",lt)
else:
   print("The search element ",search_element," is NOT available in the list ",lt)



#Output1
#Enter the number of values:5
#Enter a value to store:34
#Enter a value to store:23
#Enter a value to store:98
#Enter a value to store:100
#Enter a value to store:50


#Enter the search value :23
#The search element  23  is available in the list  [34, 23, 98, 100, 50]

#Output2
#Enter the number of values:4
#Enter a value to store:30
#Enter a value to store:40
#Enter a value to store:10
#Enter a value to store:25


#Enter the search value :50
#The search element  50  is NOT available in the list  [30, 40, 10, 25]
