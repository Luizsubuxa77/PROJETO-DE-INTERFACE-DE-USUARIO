import tkinter as tk

def limpar():
    entry.delete(0, tk.END)

janela = tk.Tk()
janela.title("Limpar Campo")

entry = tk.Entry(janela)
entry.pack(pady=10)

botao = tk.Button(janela, text="Limpar", command=limpar)
botao.pack()

janela.mainloop()