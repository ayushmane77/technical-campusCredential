def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


arr = [2, 4, 7, 10, 14, 18, 23]
target = 18
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} is present at index {result}.")
else:
    print(f"Element {target} is not present in the array.")


# def binary(stack,target):
#     left=0
#     right=len(stack)-1
#     while left<=right:
#         mid=(left+right)//2
#         if stack[mid]==target:
#             return mid
#         elif stack[mid]<target:
#             left=mid+1
#         else :
#             
            #   right=mid-1
#             return mid   

# stack=[11,12,13,14,15]
# target=1
# result=binary(stack,target)
# if result!=-1:
#     print("the element is found at index",result)
# else:
#     print("not found")    


li=[11,34,42,21,62,14]



