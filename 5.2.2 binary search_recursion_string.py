def binary_search(search,lt):
    print(lt)
    if(len(lt)==0):
        return False
    
    mid=len(lt) // 2
   
    if(search==lt[mid]):
        return True
    elif(search<lt[mid]):
        lt=lt[ :mid]
        return binary_search(search,lt)
    elif(search>lt[mid]):
        lt=lt[mid+1:]
        return binary_search(search,lt)
  
      



a=["anand","bagya","banu","chitra","dinesh"]
search="dinesh" #int(input("Enter the search element"))

res=binary_search(search,a)

if(res):
    print("The element is available")
else:
    print("The element is NOT available")
