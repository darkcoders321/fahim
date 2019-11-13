year=int(input("Enter the Year:"))
if year%4 !=0:
         print("no")
else:
         if year%100 ==0:
                  if year%400==0:
                           print("Yes")
                  else:
                           print("No")
         else:
                  print("Yes")
