
def callback(stack,key):
    for i in range(len(stack)):
        if stack[i]==key:
            print("at indx",i)
        else:
            print("not found")    
    

key=11
stack=[15,18,9,5,11]
callback(stack,key)


