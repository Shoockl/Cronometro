import tkinter as tk
import time

def contador_infinito():
    segundos = 0
    while True:
        horas, restante = divmod(segundos, 3600)
        min, seg = divmod(restante, 60)
        text = f'{horas:02d}:{min:02d}:{seg:02d}'
        label.config(text=text)
        time.sleep(1)
        segundos += 1
        root.update()

# Criar a janela principal
root = tk.Tk()
root.title("Cronometro")
root.geometry("400x200") 

# Criar um rótulo para exibir o contador
label = tk.Label(root, font=('Helvetica', 24))
label.pack(pady=20)

# Iniciar o contador em uma thread separada
root.after(0, contador_infinito)

# Iniciar o loop principal da interface gráfica
root.mainloop()
