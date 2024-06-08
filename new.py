import math
# i=1
# sum=0
# mul=1

# while i<=20:
#     if i%2==0:
#         sum=sum+i
        
#     else:
#         mul=mul*i  
#     i+=1
# print(mul+sum)

# p=int(input("enter a number"))
# q=int(input("enter second number"))
# if p<q:
#     for i in range(p,q):
#         print(i)
# else:
#     for i in range(q,p,-1):
#         print(i)        

# num=int(input("enter number"))
# sum=0
# temp=num
# while temp >0:
#     digit=temp%10
#     sum+=digit**9
#     temp//=10
# if num==sum:
#     print(num,"is an armstrongnuber")
# else:
#     print(num,"is not an armstrongnumber ")       


# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)
# s=str(input())   ////////////////////////////
# e=str(input())
# for i in range(ord(s),ord(e)+1):
    
#     for j in range(ord(s),i+1):
#         print(chr(j),end=" ")
#     print()    

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i%2,end="")
#     print()   

# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()     
# a=int(input("enter a number"))
# b=int(input("enter second number"))
# c=int(input("enter third number"))
# y=min(a,b,c)
# print("the smallest number is ",y)


# num=int(input("enter a number"))
# print(abs(num))
# print(math.sqrt(num))
# print(math.floor(num))

# print(math.floor(1.4))
# print(math.pi)
# print(math.factorial(7))

# n=int(input("enter a number"))
# factorial=1
# if n<0:
#     print("invalid")
# elif n==0:
#     print("the factorial is 1")
# else:
#     for i in range(1,n+1):
#         factorial*=i
#     print("the factorial is ",factorial)    

# s="abcdefgh"
# for i in range(len(s)):
#     print(s[i])

# s="abcdefghijklmnopqrstuvwxyz"
# for i in range(ord("a"),ord("z"),+1):
#     print("the asci value of",chr(i), "is", i)


# print(s[-2])

# print(ord("a"));
# print(chr(97))

# for i in range(ord("a"),ord("e")):
#     for j in range()
    
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("P",end="") 
#     print()   

# c=str("enter string")   
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("god",end=" ")
#     print()

# p='god '
# for i in range(1):
#     print(p*5)

# for i in range(1,6):
#     print("god "*i)  

# for i in range(5,0,-1):
#     print("@ "*i)

# for i in range(1,5):
#     print(" "*(6-i)," X "*i)

# for i in range(5,0,-1):
#     print(" "*(6-i)," X "*i)    
    
# print("*"*6)
# for i in range(1,5):
#     print("*"," "*2,"*")

# print("*"*6)    

# d="anish"
# a=''
# for i in range(4,-1,-1):
#     a+=d[i]
# print(a)
        
s="python"
# print(s[::-1])   

# print(s[0].capitalize())
# print(s.upper())
# print(s.title())
# A="PYTHON"
# print(A.lower())

# print(A.casefold())
# for i in range(1,len(s)+1):
#     print(s[:i])

txt="I love apples, apples are my favourite fruit."
print(txt.count("apples"))
print(txt.index("apples"))
print(txt.endswith("."))
print(txt.startswith("I"))
print(txt.find("es"))

# s="elvish"
# print(s.center(16,"*"))
# print(s.ljust(10,"$"))
# txt="pratik is here"
# print(txt.replace("pratik","Ayush"))

# print(txt.split())

# sac=str(input("enter a string\n").split())
# print(sac)
# print(sac.__len__())

# list=[12,245,2324,5645,23]
# print(list[::-1])
# list.sort()
# print(list)

# s=str(input("enter a string"))
# reverseStr=s[::-1]
# if reverseStr==s:
#     print("it is a palindrome")
# else:
#     print("it is not")    

s=['N','I','T','I','N']
vowel="aeiouAEIOU"
for i in s:
    if s==vowel:
        print("it is vowewl")
    else:
        print("not a vowel")    

