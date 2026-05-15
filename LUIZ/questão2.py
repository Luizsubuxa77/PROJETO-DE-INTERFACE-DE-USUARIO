import tkinter as tk

janela = tk.Tk()
janela.title("Labels Coloridos")

tk.Label(janela, text="Vermelho", bg="red", fg="white").pack(pady=5)
tk.Label(janela, text="Verde", bg="green", fg="white").pack(pady=5)
tk.Label(janela, text="Azul", bg="blue", fg="white").pack(pady=5)

janela.mainloop()