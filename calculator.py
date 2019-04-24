
print("Please Make a Selection ")
#time.sleep(5)
menu = True 
while(menu):
   print("1.addition")
   print("2.subtration")
   print("3.Multiplication")
   print("4.Division")
   print("5.Exit")
   
   choice = input() 
   

   if choice ==  '1': 
      num1 = int   (input("plese enter the first number"))
      num2 = int  ( input("plese enter the second number"))
      total = num1 + num2 
      print ("" , str(total))
   elif choice ==  '2' : 
       num1 = int   (input("plese enter the first number"))
       num2 = int  ( input("plese enter the second number"))
       total = num1-num2 
       print ("" , str(total))
   elif choice ==  '3' : 
       num1 = int   (input("plese enter the first number"))
       num2 = int  ( input("plese enter the second number"))
       total = num1*num2 
       print ("" , str(total))
   elif choice ==  '4' : 
       num1 = int   (input("plese enter the first number"))
       num2 = int  ( input("plese enter the second number"))
       total = num1/num2 
       print ("" , str(total))
   else:
       choice == '5'
       print ("good Bye")
       break 
    
  
