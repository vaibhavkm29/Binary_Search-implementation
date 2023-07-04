def binary_search(lst,target):
    low=0
    high=len(lst)-1
    while low<=high:
        mid=(low+high)//2

        if lst[mid]==target:
            return mid
        elif lst[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

integers=list(map(int,input().split(" ")))
goal=int(input())
if binary_search(integers,goal)!=-1:
    print(True, binary_search(integers,goal))
else:
    print(False)
    