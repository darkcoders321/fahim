import turtle

name=turtle.textinput("name","What is your name?")
name=name.lower()
if name.startswith("mr"):
         print("Hello sir, How are you?")
elif name.startswith("mrs") or startswith("ms"):
         print("Hello mem, How are you?")
else:
         name = name.capitalize()
         str ="Hi"+name+"..! How are you?"
         print(str)
