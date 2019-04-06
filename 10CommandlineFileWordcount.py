import sys


#filename="file1.txt"
#filename=input("enter the filename")

if(len(sys.argv)==2):
    filename=sys.argv[1]

fo=open(filename,mode='r+')

str=fo.read()

print(str)

lt=str.split(" ")
count=len(lt)
print("Number of words present :",count)

fo.close()
 
