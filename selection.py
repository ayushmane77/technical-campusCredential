stack=[11,14,16,2,4,15]
for i in range(len(stack)):
    min_index=i
    for j in range(i+1,len(stack)):
        if stack[j]<stack[min_index]:
            
           
            min_index=j
    stack[i], stack[min_index] = stack[min_index], stack[i]    
print(stack)    

# L=[15,13,3,11,0,14]
# print("unsorted list",L)
