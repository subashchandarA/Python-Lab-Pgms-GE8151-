#Most Frequent word in a string

#str="is program is to find the of the word in the string"

filename=input("Enter the file name to find the most frequent word: ")
fo=open(filename,'r')
str=fo.read()

print("The given string is :",str)
wordlist = str.split(" ")
d={}

for s in wordlist:
    if( s in d.keys()):
        d[s]=d[s]+1
    else:
        d[s]=1

#Frequency: each word as key and frequency is its value 
print("Dictionary containing word and its frequency:",d)
m = max(d.values())
print(m)

for key in d:
    if(d[key]==m):
        result=key
print(" The most frequent word : ",result)
print(" It is present ",m," times")
