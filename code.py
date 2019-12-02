def insertionSort(A):
    if len(A)>0:
        comparison = 0
        for i in range(1,len(A)):
            comparison = insert(A[i],A,i,comparison)
        print(A)
        print("Number of comparisons: "+str(comparison))
    else:
        print("Array is already sorted ")

def insert(k, A, hi,c):
    for i in range (hi,0,-1):
        if k >= A[i-1]:
            c+=1
            A[i] = k
            
            return c
        A[i] = A[i-1]
        c+=1
    A[0] = k
    return c
    

insertionSort([2,4,6,8,10,1,3,5,7,9] )
insertionSort([1,2,3,4,5,6,7,8,9,10] )
insertionSort([10,9,8,7,6,5,4,3,2,1])
