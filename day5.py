

#each cuntomer comes take order on
#tea(10),coffee(20),water(15),bun maska(20)
#once done give bill(generated) with itemzied bill
# 1.tea 3
# 2.coffee 1
# 3.water 0
# 4.bun maska 2

# Bill Number: 121
# Tea unit:3 cost:30.00
# Coffee unit:1 cost:20.00
# Bun Maska unit:2 cost:40.00
# .........................
# Total:90.00
# after this ask for next order and stop system when -1 is entered
# update total busineess done:(total)
# '''

# Global_total=0
# billno=20240116
# while True:
#     yes_no=int(input("Do you want to order:1/yes 0/no:"))
#     if yes_no==1:
#         billno+=1#generate bill no
#         ct=cc=cw=cb=0
#         ct=int(input("Tea:"))
#         cc=int(input("Coffee:"))
#         cw=int(input("Water:"))
#         cb=int(input("Bun Maska:"))
#         #bill generation
#         print("Bill no:",billno)
#         print("------------------------------------------------")
#         if ct>0:
#             print("Tea\t",ct,"\t",ct*10)
#         if cc>0:
#             print("Coffee\t",cc,"\t",cc*20)
#         if cw>0:
#             print("Water\t",cw,"\t",cw*15)
#         if cb>0:
#             print("Bun Maska\t",cb,"\t",cb*20)
#         print("------------------------------------------------")
#         total=ct*10+cc*20+cw*15+cb*20
#         Global_total+=total#ADD TO BUSINESS TOTAL
#         print("Total\t\t",total)
#     elif yes_no==0:
#         print("Total business done:",Global_total)#show total business done
#         break
#     else:
#         print("please select 1 or 0")

# set1={"ayu","ubai","sac"}
# print(set1)
# print(type(set1))
# set2={11,12,34,43}
# print(set2)
# print(type(set2))
# set3={True,False,True}
# print(set3)
# print(type(set3))

# set4={11,56,23,1,56}
# print(set4)
# abc=[11,12,13,14,15,12]
# x=set(abc)
# print(x)
# y=set([12,56,72,14,16])
# list=[16,17,18]
# # print(y)
# y.add(13)
# y.update(list)
# print(y)

set1={11,12}
# set2={16,12}
# set1.add(13)
# set1.update(set2)
# print(set1)

# t=set1.copy()
# # print(t)

# t.discard(11)
# print(t)

# set1={12,11,56,34}
# set2={67,11,21,87}
# t=set1.union(set2)
# print(t)
# i=set1.difference(set2)
# print(i)
# t=set1.intersection(set2)
# print(t)

# M_dict={
#     "name": "sachin",
#     "age": "21",
#     "hobby":"havas"
    
# }
# print(M_dict['name'])
# M_dict['movie']='animal'
# print(M_dict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])
# print(len(thisdict))


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(type(thisdict))


# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# thi = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thi["year"] = 2018
# print(thi)

# thi.update({"year":2021})
# thi["color"]="red"
# print(thi)
# thi.pop("model")
# print(thi)
# thi.popitem()
# print(thi)

# def checkmax(a,b,c):
#     return max(a,b,c)
# a=int(input("enter 1st number"))
# b=int(input("enter 2nd number"))
# c=int(input("enter 3rd number"))

# print("The maximum number between", a, ",", b, ", and", c, "is", checkmax(a, b, c))

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# number = int(input("Enter a number: "))
# if is_prime(number):
#     print(number, "is a prime number")
# else:
#     print(number, "is not a prime number")

# def check_prime(num):
#     if num==1:
#         print("not a prime number")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 print("not a prime nunber")
#                 break;
#             else:
#                 print("prime number")
#                 break;
# var=int(input("enter number"))
# check_prime(var)    

# def calculator(a,b,op):
#     if op=="+":
#         print(a+b)
#     elif op=="-":
#         print(a-b)
#     elif op=="*":
#         print(a*b)   
#     elif op=="/":
#         print(a/b)
#     else:
#         print("Invalid") 

# calculator(2,4,"+")


def addition(a,b):
        return a+b;
def subtract(a,b):
        return a-b;
def multiply(a,b):
        return a*b;
def duvide(a,b):
        return a/b;
a=int(input("enter a number"))
b=int(input("enter a number"))
while True:
    option=int(input("enter"))
    if option==1:
           x=addition(a,b)
           print(x)
    elif option==2:
           y=subtract(a,b)
           print(y)
    elif option==3:
           z=multiply(a,b)
           print(z)
    elif option==4:
           m=duvide(a,b)  
           print(m)
    elif option==0:
           break;        
    else:
           print("invalid")           
    