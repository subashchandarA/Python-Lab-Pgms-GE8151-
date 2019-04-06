#Histogram
#Find and display histogram of frequency of numbers in a given list

lt = [35,5,10,5,20,10,5,20]

print("The given list is: ",lt)
d={}

#Storing Frequency : each number as key and frequency as its value 

for s in lt:
    if( s in d.keys()):
        d[s]=d[s]+1
    else:
        d[s]=1


print("Dictionary containing word and its frequency:",d)
print(" Histogram :")
print("Word".rjust(20)," : Frequency ")
for key in d:
    print(" %20d : "%key,end=" ")
    print("#"*d[key])

#The given list is:  [35, 5, 10, 5, 20, 10, 5, 20]
#Dictionary containing word and its frequency: {35: 1, 5: 3, 10: 2, 20: 2}
# Histogram :
#                Word  : Frequency 
#                   35 :  #
#                    5 :  ###
#                   10 :  ##
#                   20 :  ##
