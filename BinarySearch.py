def binarySearch(ArrA, targetVal):
    left = 0;
    right= len(ArrA)-1;
    while left<=right:
        mid = (left+right)//2
        if ArrA[mid]==targetVal:
            return mid
        if ArrA[mid]<targetVal:
            left=mid+1
        else:
            right=mid-1
    return -1
mylist = [2,3,7,7,11,15,25]
x=11
result = binarySearch(mylist,x)
if result!=-1:
    print("Found at index", result)
else:
    print("Not found")

