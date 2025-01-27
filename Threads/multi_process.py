from multiprocessing import Process, Queue
import time
import keyboard

class Produto:
    def __init__(self, id, delay):
        self.id = id
        self.data = 1
        self.delay = delay


def pessoa_process(pessoa, response_queue, delay):
    i = 0
    while True:
        i += 1
        pessoa.data = i
        time.sleep(delay)
        response_queue.put(f"{pessoa.data} atualizou: {pessoa.id}")

def main():
    response_queue = Queue(maxsize=10)
    produtos = [
        Produto(0, 0.1),
        Produto(1, 0.3),
        Produto(2, 0.5),
        Produto(3, 1),
    ]

    processos = []

    for produto in produtos:
        processos.append(Process(target=pessoa_process, args=(produto, response_queue, produto.delay)))

    for processo in processos:
        processo.start()

    print("Pressione 'q' para encerrar.")

    while True:
        while not response_queue.empty():
            message = response_queue.get()
            print(f"Mensagem recebida: {message}")

        if keyboard.is_pressed('q'):
            print("Encerrando...")
            for processo in processos:
                processo.terminate()
                processo.join()
            break

    print("Programa finalizado.")


if __name__ == "__main__":
    main()