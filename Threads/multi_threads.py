import threading
from collections import deque 
import time

def produtor(fila):
    for i in range(20):
        time.sleep(0.1)  
        mensagem = f"Mensagem {i}"
        fila.append(mensagem)
        print(f"Produzido: {mensagem}")

def consumidor(fila):
    time.sleep(1.5) 
    while fila:
        time.sleep(1) 
        mensagem = fila.popleft()        
        print(f"Consumido: {mensagem}")

fila = deque(maxlen=10)

produtor_thread = threading.Thread(target=produtor, args=(fila,))
consumidor_thread = threading.Thread(target=consumidor, args=(fila,))

print("Thread produtor iniciada")
produtor_thread.start()
print("Thread consumidor iniciada")
consumidor_thread.start()

produtor_thread.join()
print("Thread produtor encerrada")

consumidor_thread.join()
print("Thread consumidora encerrada")

print("Threads finalizadas")