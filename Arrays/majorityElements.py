"""
A majority element in an array A[] of size n is an element that appears more than n/2 times

This is Moore's Voting Algorithm. The findCandidate will give us the candidate for the majority element.

There are 2 cases when Moore's Voting Algorithm fails:
1) No majority Element (If the array does not have a majority element (no element appears more than half the times), the algorithm will still provide a candidate after the first phase.)
2) Incorrect Assumptions (The algorithm assumes that a majority element exists. If this assumption is incorrect, the result will not be valid.)
"""

def findCandidate(a):
    index = 0
    count = 1

    for i in range(1,len(a),1):
        if(a[i] == a[index]):
            count +=1
        else:
            count -= 1
            if(count == 0):
                index = i
                count = 1
    
    return a[index]

def isMajorityElement(candidate,a):
    count = 0
    for i in range(len(a)):
        if(a[i] == candidate):
            count += 1
    
    if(count >= len(a)/2):
        return 1
    
    return 0


if __name__ == "__main__":
    a = [3,4,2,4,2,4,4]
    candidate = findCandidate(a)

    if(isMajorityElement(candidate,a)):
        print("The majority element is: ", candidate)
    else:
        print("No majority Element")