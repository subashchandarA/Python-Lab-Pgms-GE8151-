def insertion_sort(arr):
    " select ith element and insert into the sorted sequence of 0 to i "
    
    for i in range(1, len(arr)):  # starting from i=1
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key  
        print(arr)    

    

n=int(input("Enter the number of values:"))

lt = []   # creation of empty list
#getting n values and store in a list
i=0
while(i<n):
    number=int(input("Enter a value to store:"))
    lt.append(number)
    i=i+1


print("Before Sorting : ",lt)

insertion_sort(lt)

print("After Sorting : ",lt)


#OUTPUT 1
#Enter the number of values:6
#Enter a value to store:25
#Enter a value to store:150
#Enter a value to store:75
#Enter a value to store:25
#Enter a value to store:200
#Enter a value to store:10
#Before Sorting :  [25, 150, 75, 25, 200, 10]
#[25, 150, 75, 25, 200, 10]
#[25, 75, 150, 25, 200, 10]
#[25, 25, 75, 150, 200, 10]
#[25, 25, 75, 150, 200, 10]
#[10, 25, 25, 75, 150, 200]
#After Sorting :  [10, 25, 25, 75, 150, 200]
