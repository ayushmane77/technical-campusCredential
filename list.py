import math

import random
# d1=[12,45,23,87,45]
# d1[0]=120*100
# d2=[56,34,12,89]
# for i in range(len(d1)):
#     print("the value of ",i  ,"is" ,d1[i])

# dlt=d1.copy()    
# print(dlt)
# con=d1+d2

# print(con)
# d1.extend(
# d2)
# print(d1)

# num=input("enter numbers").split()

# print(list(map(float,num)))

# print(list(map(float,num)))

# d1=[]
# n=4
# for i in range(1,n):
    
#     # print(d1[i])
#     # sum=sum+d1[i]
#     item=int(input("enter numbers"))
#     d1.append(item)
#     # print(d1)
    
# # print(sum)

# print(d1)

# d2=[]

# while True:
#     inp=(input("enter numbers"))
#     if inp==" ":
#         print("invalid")
#         break;
#     else:
         
#         d2.append(int(inp))
#         great=max(d2)
#         small=min(d2)
        

# print(d2)    
# print(great)
# print(small)    
# print(sum(d2))

# d3=[]
# while True:
#     data=input("enter data")
#     if data=="":
#         break
    
#     d3.append(int(data))
   
# avg=sum(d3)/len(d3)
# for i in range(len(d3)):
#     if d3[i]<avg:
#         d3[i]+=10
#     else:
#         d3[i]-=5
# print(d3)
# ayush=['mobile','laptop','TV']
# # ayush.pop(1)
# # ayush.remove('mobile')
# ayush.insert(3,"sachin")
# print(ayush)

# l=[5,3,2,4,1]
# for i in range(5):
#     out=l.pop(0)
#     l.append(out)
#     print(l)  


# l1=[5,4,3,2,1]
# l2=[1,2,4,3,5]
# l1.sort()

# l2.sort()

# for i in range(len(l1)):
#     if l1[i]==l2[i]:
#         print("it is same")
#     else:
#         print("it is not same")    

# l1=[5,4,3,2,1]
# l2=[1,2,4,3,5]
# l1.sort()
# l2.sort()
# flag=True
# for i in range(len(l1)):
#     if l1[i]!=l2[i]:
#         flag=False
#         break;
# if flag==True:
#     print("it is anagram")
# else:
#     print("not a anagram")    

# num=int(input("enter a number"))
# flag=False
# if num%2==0:
#     flag=True
# else:
#     flag=False
# if flag==True:
#     print("it is even")
# else:
#     print("it is odd")     

# l1=[12,45,11,89,34]
# # even=[]
# # odd=[]
# for i in l1:
#     if i%2==0:
#         l1.remove(i)
#         # even+=l1[i]
       
#     else:
#         continue

# print(l1)
        
# num=[10,20,[30,40]]
# for i in num:
#     print(num[2][0])

# num1=[12,12,[10,20],[13,14]]
# num1[2].append(10)
# print(num1)

# store=['tea','coffee','water','bread']
# tea=int(input("enter tea quantity"))
# coffee=int(input("enter coffee quantity"))
# water=int(input("enter water quantity"))
# bread=int(input("enter no.of bread"))

# T=tea*10 +  coffee*15 + water*20 + bread*35
# print(T)

# tea=10
# coffee=15
# water=20
# bread=35
# count_t=0;count_c=0;count_w=0;count_w=0;count_b=0;
count_t=count_c=count_w=count_b=0

while True:
    ch=int(input("please select some items"))

    if ch==1:
        print("tea selected")
        count_t+=1
    elif ch==2:
        print("coffee selected")   
        count_c+=1 
    elif ch==3:
        print("water selected")
        count_w+=1
    elif ch==4:
        print("bread selected")   
        count_b+=1 
    elif ch==0:
        print("thank you for ordering")
        break
    else:#default
        print("thank you")
print("count of tea is ",count_t) 
print("count of tea is ",count_c) 
print("count of tea is ",count_w) 
print("count of tea is ",count_b) 
print("total units sold is ",(count_t+count_c+count_w+count_b))
total=(count_t*10)+(count_c*15)+(count_w*20)+(count_b*35)
print("the total price is",total)

bill=random(1,10)
print("the bill number is ",bill)