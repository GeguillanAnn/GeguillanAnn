print ("                                           S U C K M A I C E")
print ("                           HELLO AND WELCOME 'ICE CREAMPIES' TO SUCKMAICE!!")
print ("                                       'L I C K  I T  G O O D ! !'")

print ("")
print ("")
print ("")

order = input ("Type 'YES' if you would you like to order: ")
if (order=="YES"):


  print ("")
  print ("")
  
  print ("                                                'M E N U'")
  
  print ("")
  print ("")
  
  print ("   I c e C r e a m ( M A I N )""          D r i n k s""                 S i d e D i s h e s")
  
  print ("")
  print ("")
  
  print ("F L A V O R S        CONE     CUP")
  
  print ("")
  
  print ("> CHOCOLATE           P50     P90      > MANGO SHAKE      P65    > JELLO SALAD          P40")
  print ("> ROCKY ROAD          P50     P90      > ORANGE SHAKE     P65    > CANDIES/SWEETS       P40")
  print ("> AVOCADO             P50     P90      > AVOCADO SHAKE    P65    > BAKED/COOKED APPLE   P40")
  print ("> VANILLA             P50     P90      > MILKSHAKE        P65    > BROWNIES             P40")
  print ("> STRAWBERRY          P50     P90      > VEGAN SHAKE      P65")
  print ("> HAZELNUT            P50     P90      > BANANA SHAKE     P65")
  print ("> LEMON               P50     P90      > COCONUT SHAKE    P65")
  print ("> MASCARPONE          P50     P90      > TROPICAL SHAKE   P65")
  print ("> COOKIES 'N CREAM'   P50     P90")
  print ("> MANGO CHEESECAKE    P50     P90")
  print ("> MATCHA              P50     P90")
  
  print ("")
  
  print ("")
  
  print ("Use UPPERCASE LETTER and STRICTLY ONE ORDER PER PERSON. THANK YOU!!")
  
  name = input('Enter Your Name: ')
  
  print ("")
  
  print ("Please Enter Your Order!!")
  
  icecream = input("Enter your Ice Cream Flavor: ")
  
  cone = "CONE"
  cup = "CUP"
  
  size= input("Ice Cream Size: ")
  
  print ("")
  
  if(size==cone):
    print("Your", icecream, "flavor icecream is 50 php." )
  else:
    print("Your", icecream, "flavor icecream is 90 php." )
  
  print ("")
  
  drinks = input("Enter your prefered Drink: ")
  
  print ("")
  
  print ("Your", drinks, "is 65 php.")
  
  print ("")
  
  side = input("Enter your Side Dish: ")
  
  print ("")
  
  print ("Your", side, "is 40 php.")
  
  print ("")
  
  print ("--------------------------ORDER CONFIRMATION-------------------------")
  print ("Hi Mr./ Ms.", name,)
  
  print ("")

  confirm = input ("We would like to confirm your order:")
  if (confirm == "YES"):
         print("")
    
         print ("You ordered, a", size,"of", icecream, "flavored Ice Cream, with", drinks, "and", side,)

  print ("")
  
  
  if (confirm == "NO"):
      print ("")
      
      
      print ("                                                'M E N U'")
      
      print ("")
      print ("")
      
      print ("   I c e C r e a m ( M A I N )""          D r i n k s""                 S i d e D i s h e s")
      
      print ("")
      print ("")
      
      print ("F L A V O R S        CONE     CUP")
      
      print ("")
      
      print ("> CHOCOLATE           P50     P90      > MANGO SHAKE      P65    > JELLO SALAD          P40")
      print ("> ROCKY ROAD          P50     P90      > ORANGE SHAKE     P65    > CANDIES/SWEETS       P40")
      print ("> AVOCADO             P50     P90      > AVOCADO SHAKE    P65    > BAKED/COOKED APPLE   P40")
      print ("> VANILLA             P50     P90      > MILKSHAKE        P65    > BROWNIES             P40")
      print ("> STRAWBERRY          P50     P90      > VEGAN SHAKE      P65")
      print ("> HAZELNUT            P50     P90      > BANANA SHAKE     P65")
      print ("> LEMON               P50     P90      > COCONUT SHAKE    P65")
      print ("> MASCARPONE          P50     P90      > TROPICAL SHAKE   P65")
      print ("> COOKIES 'N CREAM'   P50     P90")
      print ("> MANGO CHEESECAKE    P50     P90")
      print ("> MATCHA              P50     P90")
      
      print ("")
      
      print ("")
      
      print ("Use UPPERCASE LETTER and STRICTLY ONE ORDER PER PERSON. THANK YOU!!")
      
      name = input('Enter Your Name: ')
      
      print ("")
      
      print ("Please Enter Your Order!!")
      
      icecream = input("Enter your Ice Cream Flavor: ")
      
      cone = "CONE"
      cup = "CUP"
      
      size= input("Ice Cream Size: ")
      
      print ("")
      
      if(size==cone):
        print("Your", icecream, "flavor icecream is 50 php." )
      else:
        print("Your", icecream, "flavor icecream is 90 php." )
      
      print ("")
      
      drinks = input("Enter your prefered Drink: ")
      
      print ("")
      
      print ("Your", drinks, "is 65 php.")
      
      print ("")
      
      side = input("Enter your Side Dish: ")
      
      print ("")
      
      print ("Your", side, "is 40 php.")
      
      print ("")
      
      print ("--------------------------ORDER CONFIRMATION-------------------------")
      print ("Hi Mr./ Ms.", name,)
      
      print ("")


         
      print ("You ordered, a", size,"of", icecream, "flavored Ice Cream, with", drinks, "and", side,)
      
      print ("")
      
      
      shake = 65
      sidedish = 40
      
      
      
      print     ("===========================================================================")
      print ("                                 BILL")
      print ("")
      print ("                          S U C K M A I C E")
      print ("               HELLO AND WELCOME 'ICE CREAMPIES' TO SUCKMAICE!!")
      print ("                       'L I C K  I T  G O O D ! !'")
      print ("")
      print ("===========================================================================")
      print ("                            Receipt # 0403")
      print ("===========================================================================")
      print ("      05-02-22                                  Monday")
      print ("===========================================================================")
      print ("QTY                   ITEM                        PRICE")
      print ("")
      if(size==cone):
        print("1                  ", icecream, "                      50 Php" )
      else:
        print("1                  ", icecream, "                      90 Php" )
      print ("1                  ", drinks, "                          65 Php" )
      print ("1                  ", side, "                           40 Php" )
      print ("")
      
      if (size==cone):
        total=50+shake+sidedish
        print ("Total amount: P", total)
        print ("(Bill)")
        bayad1=int(input("How much money are you willing to pay?:  "))
        if bayad1>=1 :
          bill1=(bayad1 - total) 
        print("Change for your payment :")
        print(  "P", bill1, ".00")
        
        print ("THANK YOU!")
        print("")
        
        print (" Please proceed to another transaction for other orders.")
        print     ("===========================================================================")
      elif (size==cup):
        etotal=90+shake+sidedish
        print ("Total amount: P", etotal)
        print ("(Bill)")
        bayad1=int(input("How much money are you willing to pay?  "))
        if bayad1>=1 :
          bill1=(bayad1 - etotal) 
        print("Change for your payment :")
        print(   "P", bill1, ".00")
        
        print ("THANK YOU!")
        print("")
        
        print (" Please proceed to another transaction for other orders.")
        print   ("===========================================================================")
        print ("")
      
      else:
        print("Invalid")ye
    
  else: 
    
    
    print ("===========================================================================")
    print ("                                 BILL")
    print ("")
    print ("                          S U C K M A I C E")
    print ("               HELLO AND WELCOME 'ICE CREAMPIES' TO SUCKMAICE!!")
    print ("                       'L I C K  I T  G O O D ! !'")
    print ("")
    print ("===========================================================================")
    print ("                            Receipt # 0403")
    print ("===========================================================================")
    print ("      05-02-22                                  Monday")
    print ("===========================================================================")
    print ("QTY                   ITEM                        PRICE")
    print ("")
    if(size==cone):
      print("1                  ", icecream, "                      50 Php" )
    else:
     print("1                  ", icecream, "                      90 Php" )
    print ("1                  ", drinks, "                   65 Php")
    print ("1                  ", side, "                     40 Php")
    print ("")
    
    if (size==cone):
      shake=65
      sidedish=40
      total=50+shake+sidedish
      print ("Total amount: P", total)
      print ("(Bill)")
      bayad1=int(input("How much money are you willing to pay?  "))
      if bayad1>=1 :
        bill1=(bayad1 - total) 
      print("Change for your payment :")
      print(  "P", bill1, ".00")
      
      print ("THANK YOU!")
      print("")
      
      print (" Please proceed to another transaction for other orders.")
      print     ("===========================================================================")
    elif (size==cup):
      shake=65
      sidedish=40
      etotal=90+shake+sidedish
      print ("Total amount: P", etotal)
      print ("(Bill)")
      bayad1=int(input("How much money are you willing to pay?  "))
      if bayad1>=1 :
        bill1=(bayad1 - etotal) 
      print("Change for your payment :")
      print(   "P", bill1, ".00")
      
      print ("THANK YOU!")
      print("")
      
      print (" Please proceed to another transaction for other orders.")
      print   ("===========================================================================")
      print ("")
    
    else:
      print("Invalid")
    
else:
  print("Wag kang pumindot pag di ka bibili")