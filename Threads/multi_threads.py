import threading
import queue
import time

def produtor(fila):
    for i in range(20):
        time.sleep(0.5)  
        mensagem = f"Mensagem {i}"
        fila.put(mensagem)
        print(f"Produzido: {mensagem}")

def consumidor(fila):
    while fila.not_empty:
        time.sleep(100) 
        mensagem = fila.get()        
        print(f"Consumido: {mensagem}")

fila = queue.Queue(10)

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