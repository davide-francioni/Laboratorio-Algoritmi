import random

def selection_sort(A):
    #print("Lista iniziale Selection-sort", A)
    for i in range (0, len(A)):
        m=i
        for j in range(i, len(A)):
            if A[j] < A[m]:
                m = j
        if A[m] != A[i]:
            A[m], A[i] = A[i], A[m]

def quick_sort(A, p, r):
    if p < r:
        q=partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)

def partition(A,p,r):
    x= A[r]
    i=p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def genera_array_casuale(dimensione, minimo=0, massimo=100):
    return [random.randint(minimo, massimo) for _ in range(dimensione)]


if __name__ == '__main__':
    A=genera_array_casuale(10)
    B=[0,0,0,0,0,0,0,0,0,0]
    for i in range(0,10):
        B[i]=A[i]
    print("Lista iniziale Quick-sort", B)

    selection_sort(A)
    quick_sort(B, 0, len(B)-1)
    #print("Lista finale Selection-sort", A)
    print("Lista finale Quick-sort", B)
