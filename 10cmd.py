# command line arguments
# sum the values passed as command line argument
import sys


print("The content of sys.argv is : ",sys.argv)

print("No of parameter passed as command line(excluding the file name): ",len(sys.argv)-1)

sum=0
for i in range(1,len(sys.argv)):
    sum=sum+int(sys.argv[i])
print("Sum of the values passed:",sum)
               

#output1

#D:\Python Pgm\lab pgms>python 10.1cmd.py 20 50 70

#The content of sys.argv is : ['10.1cmd.py', '20', '50', '70']
#No of parameter passed as command line(excluding the file name):  3
#Sum of the values passed: 140

#output2

#D:\Python Pgm\lab pgms>python 10.1cmd.py 200 300

#The content of sys.argv is : ['10.1cmd.py', '200', '300']
#No of parameter passed as command line(excluding the file name):  2
#Sum of the values passed: 500
