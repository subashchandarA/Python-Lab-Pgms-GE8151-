#Histogram
#Find and display histogram of frequency of each word in a String

str="is program is to find the of the word in the string"


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

print("Word".rjust(20)," Frequency ")
for key in d:
    print( key.rjust(20),end=" ")
    print("#"*d[key])
    #print(" %4d : "%key,end=" ")
    #print("#"*d[key])
