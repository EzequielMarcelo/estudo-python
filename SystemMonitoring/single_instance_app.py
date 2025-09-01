import os
import sys
import psutil
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
import logging

def IsAlreadyRunning():
    current_pid = os.getpid()
    proc_count = 0

    if getattr(sys, 'frozen', False):
        # Se for exe gerado pelo PyInstaller
        current_program = os.path.basename(sys.executable).lower()
    else:
        # Script Python
        current_program = os.path.basename(sys.argv[0]).lower()

    for proc in psutil.process_iter(['pid', 'exe', 'cmdline']):
        try:
            # ignora o processo atual
            if proc.info['pid'] == current_pid:
                continue

            cmdline = proc.info['cmdline']
            exe = proc.info['exe']
            
            if not cmdline or not exe:
                continue
            
            # ignora executavel do ambiente virtual para evitar falso positivo
            if "venv" in proc.info['exe']:
                continue

            # Verifica se algum argumento da linha de comando é o script/exe
            for arg in cmdline:
                if os.path.basename(arg).lower() == current_program:
                    # se estiver no modo one file o primeiro exe é para extrair os arquivos temporários
                    if getattr(sys, 'frozen', False):
                        proc_count += 1
                        if proc_count >= 2:
                            return True
                    else:
                        return True
                
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False



def loop():
    height, length = 480, 640
    void_gray = np.zeros((height, length), dtype=np.uint8)

    img = Image.fromarray(void_gray)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, loop)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),             
        logging.FileHandler("app.log")   
    ]
)

if IsAlreadyRunning():
    logging.warning("Já existe uma instância do programa rodando")
    sys.exit()

logging.info("Iniciando programa...")

root = tk.Tk()
root.title("Single Instance App")
root.resizable(False, False)

lmain = tk.Label(root)
lmain.pack()

loop()
root.mainloop()
