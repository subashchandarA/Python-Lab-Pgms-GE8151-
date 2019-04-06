# Program to copy a file into another new file


sourcename=input("enter the source filename")
destname=input("Enter the new file name to create")


srcfo=open(sourcename,mode='r')
destfo=open(destname,'w')

str=srcfo.read()
s=destfo.write(str)

print(s)

#print(str)


srcfo.close()
destfo.close() 
