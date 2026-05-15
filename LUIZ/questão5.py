import tkinter as tk

janela = tk.Tk()
janela.title("Formulario")

tk.Label(janela, text="Nome").grid(row=0, column=0, sticky="e", padx=5, pady=5)
tk.Label(janela, text="Cidade").grid(row=1, column=0, sticky="e", padx=5, pady=5)

entry_nome = tk.Entry(janela)
entry_cidade = tk.Entry(janela)

entry_nome.grid(row=0, column=1, padx=5, pady=5)
entry_cidade.grid(row=1, column=1, padx=5, pady=5)

janela.mainloop()