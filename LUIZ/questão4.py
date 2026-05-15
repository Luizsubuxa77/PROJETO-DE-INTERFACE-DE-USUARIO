import tkinter as tk

janela = tk.Tk()
janela.title("Botoes Lado a Lado")

botao_a = tk.Button(janela, text="Botao A", bg="lightblue")
botao_a.pack(side="left", padx=10, pady=10)

botao_b = tk.Button(janela, text="Botao B", bg="lightgreen")
botao_b.pack(side="left", padx=10, pady=10)

janela.mainloop()