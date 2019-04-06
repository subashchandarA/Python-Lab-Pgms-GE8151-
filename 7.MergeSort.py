
# Program for implementation of MergeSort 

# function to print the list 
def printList(arr): 
    for i in range(len(arr)):        
        print(arr[i],end=" ") 
    print()
    
# function to do merge sort the array    
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  

        i = j = k = 0

          
        # Merging the sorted first half and second half 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
      
        while i < len(L):          
            arr[k] = L[i]          
            i+=1
            k+=1                
         
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  


arr = [12, 331, 810, 28, 26, 2]  
print ("Given array is : ")  
printList(arr)

mergeSort(arr) 

print("Sorted array is: ", end="\n") 
printList(arr) 
  
