def selectionsort(lt):
    "select the min value and insert into its position"
    for i in range(len(lt)-1):
        min_pos=i 
        for x in range(i+1,len(lt)):
            if(lt[min_pos]>lt[x]):
                min_pos=x
        lt[min_pos],lt[i]=lt[i],lt[min_pos]
        print(lt)    #Print the list to see the each step of selection sort
            


n=int(input("Enter the number of values:"))

lt = []   # creation of empty list
#getting n values and store in a list
i=0
while(i<n):
    number=int(input("Enter a value to store:"))
    lt.append(number)
    i=i+1


print("Before Selcection Sort : ",lt)

selectionsort(lt)

print("After Selcection Sort : ",lt)


#OUTPUT 1
#Enter the number of values:6
#Enter a value to store:23
#Enter a value to store:80
#Enter a value to store:250
#Enter a value to store:10
#Enter a value to store:500
#Enter a value to store:50
#Before Selcection Sort :  [23, 80, 250, 10, 500, 50]
#[10, 80, 250, 23, 500, 50]
#[10, 23, 250, 80, 500, 50]
#[10, 23, 50, 80, 500, 250]
#[10, 23, 50, 80, 500, 250]
#[10, 23, 50, 80, 250, 500]
#After Selcection Sort :  [10, 23, 50, 80, 250, 500]
