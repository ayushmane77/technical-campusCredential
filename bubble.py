stack=[12,45,16,45,11,6]
for i in range(len(stack)):
  
    for j in range(i+1,len(stack)-i-1):
        if stack[j]<stack[j]:
            print()