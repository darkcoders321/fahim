li=[1,3,4,5]
new_li=[]
for i in li:
         new_li.append(2*i)
print(new_li)

#list comprehensions

list=[1,2,3,4,5]
new_list=[2*i for i in list]
print(new_list)

#even number
even_list=[1,2,3,4,5,6]
even_num=[]
for x in even_list:
         if x%2 == 0:
                  even_num.append(x)
print(even_num)

#comprehensions even_number
even_num2=[x for x in range(1,21) if x%2==0]
print(even_num2)



