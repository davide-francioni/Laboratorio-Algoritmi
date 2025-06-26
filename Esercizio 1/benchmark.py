import time
import random
from heap import MaxHeap
from lista_concatenata import Lista_Concatenata as ListaNonOrdinata
from lista_concatenata_ordinata import Lista_Concatenata as ListaOrdinata
import csv

def genera_array_casuale(dimensione, minimo=0, massimo=100):
    return [random.randint(minimo, massimo) for _ in range(dimensione)], [random.randint(minimo, massimo) for _ in range(dimensione)]

def misura_tempi_struttura(nome, struttura, arr, pri):
    tempi = {}

    start = time.time()
    for p, v in zip(pri, arr):
        struttura.insert(p, v)
    tempi["insert"] = time.time() - start

    start = time.time()
    struttura.list_max()
    tempi["max"] = time.time() - start

    nodo = struttura.get_random_node()
    start = time.time()
    try:
        struttura.increase_priority(nodo, nodo.priority + 1)
    except:
        pass
    tempi["increase"] = time.time() - start

    start = time.time()
    struttura.extract_max()
    tempi["extract"] = time.time() - start

    return [nome, tempi["insert"], tempi["max"], tempi["increase"], tempi["extract"]]

def benchmark(dimensione):
    arr, pri = genera_array_casuale(dimensione)
    risultati = []

    risultati.append(misura_tempi_struttura("Heap", MaxHeap(), arr, pri))
    risultati.append(misura_tempi_struttura("Lista Non Ordinata", ListaNonOrdinata(), arr, pri))
    risultati.append(misura_tempi_struttura("Lista Ordinata", ListaOrdinata(), arr, pri))

    with open(f"risultati_{dimensione}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Struttura", "Insert (s)", "Max (s)", "Increase (s)", "Extract (s)"])
        writer.writerows(risultati)

if __name__ == "__main__":
    for n in [10, 100, 1000]:
        benchmark(n)
