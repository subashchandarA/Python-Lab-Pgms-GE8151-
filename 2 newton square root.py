def newton_method(number, number_iters = 100):
    a = float(number) # number to get square root of
    for i in range(number_iters):
        number = 0.5 * (number + a / number) # update
	  # x_(n+1) = 0.5 * (x_n +a / x_n)
    return number



# first argument - number to find the root
# second argument is the number of times the newton's approximation performed
print (newton_method(9,2))
print (newton_method(9,3))
print (newton_method(9,10))



# square root accuracy increases when number of iteration increased
#  OUTPUT 
#  3.4
#  3.023529411764706
#  3.0

