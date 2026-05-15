import tkinter as tk

def cliqueAqui():
    texto['text'] = novoTexto.get(), 

janela = tk.Tk()
# 2. Alterando o título da janela
janela.title("Troca o texto")
# 3. Definindo o tamanho da janela
janela.geometry("300x200")

texto = tk.Label(janela, text='Meu texto')
texto.pack()
novoTexto = tk.Entry(janela)
novoTexto.pack()
botao = tk.Button(janela, text='CLique aqui', command=cliqueAqui)
botao.pack()
tk.mainloop()