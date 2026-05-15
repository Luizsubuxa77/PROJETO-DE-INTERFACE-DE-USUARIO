import tkinter as tk

janela = tk.Tk()
janela.title("Meu Primeiro App")
janela.geometry("300x200")
janela.configure(bg="#0D1B2A")

label = tk.Label(
    janela,
    text="Ola, Comando!",
    bg="#0D1B2A",
    fg="white",
    font=("Arial", 18, "bold")
)
label.pack(expand=True)

janela.mainloop()