import tkinter as tk
import ttkbootstrap as ttk
from gtts import gTTS
from pygame import mixer
import time

def falar():
    mytext = entrada.get()
    obj = gTTS(text=mytext, lang="pt", tld="com.br")
    obj.save("texto.mp3")
    mixer.init()
    mixer.music.load("texto.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
    mixer.quit()

def reset_window():
    entrada.delete(0, tk.END)

def click(*args):
    entrada.delete(0, 'end')

# Criando a Janela
janela = ttk.Window(themename='darkly')
janela.title('Voicer')
janela.geometry('350x150')

#Criando o título
titulo_label = ttk.Label(master=janela, text='Voicer', font='Calibri 24 bold')
titulo_label.pack()

# Criando o campo de Input
input_frame = ttk.Frame(master=janela)
entrada = ttk.Entry(master=input_frame, cursor='hand2')
botao = ttk.Button(master=input_frame, text='Falar', command=falar)
botao_reset = ttk.Button(master=input_frame, text='Novo Texto', command=reset_window)
entrada.pack(side='left', padx=10)
botao.pack(side='left')
botao_reset.pack(padx=10)
input_frame.pack(pady=10)

# Adicionando um placeholder
entrada.insert(0, "Insira aqui o texto: ")
entrada.bind("<Button-1>", click)


#Iniciar o app
janela.mainloop()
