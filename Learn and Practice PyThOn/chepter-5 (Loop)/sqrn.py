while True:
         n=int(input("plese enter a positive number(0 to exit):"))
         if n <0:
                  print("Only positive number allowed.Please try again")
                  continue
         if n==0:
                  break
         print("Square of",n,"is",n*n)
