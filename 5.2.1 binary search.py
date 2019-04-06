def binary_search(search,lt):

    while(len(lt)>=1):  
      print(lt)
      mid=len(lt) // 2
      print("mid is ",mid)
      if(search==lt[mid]):
          return True
      elif(search<lt[mid]):
          lt=lt[ :mid]
      elif(search>lt[mid]):
          lt=lt[mid+1:]
    else:
        return False


a=[10,20,30,40,50,60]
search=50
res=binary_search(search,a)
if(res):
    print("The element is available")
else:
    print("The element is NOT available")
