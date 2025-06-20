import random
import time

def selection_sort(A):
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

def funzione_da_misurare():
    total = 0
    for i in range(1000000):
        total += i
    return total

def confrontig(n):
    A = genera_array_casuale(n)
    B = [0] * n
    for i in range(0, n):
        B[i] = A[i]

    print("Lista iniziale Selection-sort", A)
    print("Avvio Selection-sort...")
    s_start_time = time.time()
    selection_sort(A)
    s_end_time = time.time()
    s_tempo_impiegato = s_end_time - s_start_time
    print("Lista finale Selection-sort", A)
    print(f"Tempo impiegato: {s_tempo_impiegato:.6f} secondi")

    print(" ")

    print("Lista iniziale Quick-sort", B)
    print("Avvio Quick-sort...")
    q_start_time = time.time()
    quick_sort(B, 0, len(B) - 1)
    q_end_time = time.time()
    q_tempo_impiegato = q_end_time - q_start_time
    print("Lista finale Quick-sort", B)
    print(f"Tempo impiegato: {q_tempo_impiegato:.6f} secondi")

    print(" ")

    if s_tempo_impiegato < q_tempo_impiegato:
        print("Selection-sort più veloce di Quick-sort")
    if s_tempo_impiegato > q_tempo_impiegato:
        print("Quick-sort più veloce di Selection-sort")
    if s_tempo_impiegato == q_tempo_impiegato:
        print("Selection-sort veloce come Quick-sort")

if __name__ == '__main__':
    print("Confrontiamo per 3 elementi:")
    print(" ")
    confrontig(3)
    print(" ")
    print("Confrontiamo per 5 elementi:")
    print(" ")
    confrontig(5)
    print(" ")
    print("Confrontiamo per 10 elementi:")
    print(" ")
    confrontig(10)
    print(" ")
    print("Confrontiamo per 20 elementi:")
    print(" ")
    confrontig(20)
    print(" ")
    print("Confrontiamo per 30 elementi:")
    print(" ")
    confrontig(30)
    print(" ")
    print("Confrontiamo per 100 elementi:")
    print(" ")
    confrontig(100)
    print(" ")
