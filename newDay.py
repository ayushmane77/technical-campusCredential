
# def Movehyphen(string):
#     str2=""
#     str3=""
#     for i in string:
#         if i=="-":
#             str2+=i
#         else:
#             str3+=i
#     return str3

# print(Movehyphen("----he-ll-o"))  

# str1="apple"

# def replace(str1):
#     ch1="a"
#     ch2="p"
#     ch3=""
#     for i in str1:
#         if i==ch1:
#             ch3+=ch2
#         elif i==ch2:
#             ch3+=ch1
#         else:
#             ch3+=i  
    
#     return ch3 

# print(replace("apple"))

# flag=False
# li=[1,3,4,5,6]
# if li.sort==True:
#     print("it is already sorted")
#     print(li)

# else:
#     for j in range(len(li)-1):
#         for i in range(len(li)-1):
#             if li[i]>li[i+1]:
#                 temp=li[i]
#                 li[i]=li[i+1]
#                 li[i+1]=temp

# print(li)  

# def selectionSort(arr,size):
#     for i in range(size-1):
#         min=i
#         for j in range(i+1,size):
#             if arr[j]<arr[min]:
#                 min=j
#         arr[i],arr[min]=arr[min],arr[i]
#     return arr            
    

# print(selectionSort([23,32,45,62,24],5))

# i=1
# while i<=10:
    
#     print(i)
#     i=i+1

## factorial of a number using recursion
def recursiveNumber(n):
    if n==1:
        return n
    else:
        return n*recursiveNumber(n-1)  




num=5
print(recursiveNumber(num))  

def bs(arr,n):
    left=0
    right=0
    mid=0
    