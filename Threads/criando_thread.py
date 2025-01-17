import threading

def funcao_thread():
    for i in range(10):
        print("Executando thread")

thread = threading.Thread(target=funcao_thread)
thread.start()
print("Thread principal finalizada")
thread.join()