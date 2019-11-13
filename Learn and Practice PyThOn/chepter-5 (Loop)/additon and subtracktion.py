terminated_program= False
while not terminated_program:
         number1=int(input("Enter a number:"))
         number2=int(input("Enter a number:"))

         while True:
                  operation=input("please enter add/sub or quit to exit:")
                  if operation == "quit":
                           terminated_program= True
                           break
                  if operation not in["add","sub"]:
                           print("unknown Operation")
                           continue
                  if operation =="add":
                           print("result is",number1+number2)
                           break
                  if operation == "sub":
                           print("result is",number1+number2)
                           break
