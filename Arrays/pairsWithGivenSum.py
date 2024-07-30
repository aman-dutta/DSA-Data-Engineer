"""
# This is the brute force technique, O(n^2)
def checkPair(a, size, x):
    for i in range(0,size-1):
        for j in range(i+1,size):
            print(i,j)
            if(a[i] + a[j] == x):
                return 1
    
    return 0
"""

def checkPair(a, size, sum):
    a.sort()
    leftPointer = 0
    rightPointer = size-1

    while(leftPointer < rightPointer):
        if(a[leftPointer] + a[rightPointer] == sum):
            return 1
        elif(a[leftPointer] + a[rightPointer] > sum):
            rightPointer -= 1
        else:
            leftPointer += 1

    return 0


if __name__ == "__main__":
    a = [0,-1,2,-3,1]
    x = -2
    size = len(a)

    if(checkPair(a,size,x)):
        print("Pair exists")
    else:
        print("Pair does not exists")

  