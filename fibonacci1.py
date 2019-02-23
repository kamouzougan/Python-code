Solution Project Euler problem 2 
This code will generate the Fibonaccis' numbers 
We will start with  2 numbers 0 and 1 
the next number is found by adding the 2 numbers (0+1 )
the third number is found by adding the next 2 number which is 1 + 1
and so on 
the third number is found by adding the
 
''' 
total = 0 
a = 0 
b = 1 
for i in range(0,10): 
    print (i)
    print('')
    total = a + b 
    a=b 
    b=total 
print("This is the sum of all the numbers :",total)
