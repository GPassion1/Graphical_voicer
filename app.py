import tkinter as tk
import ttkbootstrap as ttk
from gtts import gTTS
from pygame import mixer
import time

def falar():
    mytext = entrada.get()
    selected_lang_name = lang_var.get()
    selected_lang_value = language_options[selected_lang_name]

    obj = gTTS(text=mytext, lang=selected_lang_value)
    obj.save("texto.mp3")
    mixer.init()
    mixer.music.load("texto.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
    mixer.quit()
    atualizar_textbox()

def update_language(*args):
    selected_lang_name = lang_combobox.get()
    lang_var.set(selected_lang_name)


def click(*args):
    entrada.delete(0, 'end')

def enter(e):
    falar()

def atualizar_textbox():
    texto_entrada = entrada.get()
    texto.insert(tk.END, texto_entrada + "\n")


# Criando a Janela
janela = ttk.Window(themename='solar')
janela.title('Voicer')
janela.geometry('400x350')

# Criando o título
titulo_label = ttk.Label(master=janela, text='Voicer', font='Calibri 24 bold')
titulo_label.pack()

# Criando o campo de Input
input_frame = ttk.Frame(master=janela)
entrada = ttk.Entry(master=input_frame, cursor='hand2')
botao = ttk.Button(master=input_frame, text='Falar', command=falar)

# Packs
entrada.pack(side='left', padx=10, ipadx=25)
botao.pack(side='left', ipadx=20)
input_frame.pack(pady=10)

# text Frame
text_frame = ttk.Frame(master=janela)
# Título do txtbox
txtbox_label = ttk.Label(master=text_frame, text='Últimos textos', font='Calibri 12 bold')
txtbox_label.pack(anchor=tk.N)
texto = ttk.Text(master=text_frame, width=20, height=5)
texto.pack(pady=10, padx=10, ipadx=20)
text_frame.pack(pady=5, anchor=tk.S)

# lista de idiomas dicionário
language_options = {
    "Português": "pt",
    "English": "en",
    "Español": "es",
    "Français": "fr",
    "Deutsch": "de"
}

# Combobox de seleção de idioma
combo_frame = ttk.Frame(master=janela)
# Label
combo_label = ttk.Label(master=combo_frame, text='Selecione o idioma', font='Calibri 12 bold')
combo_label.pack(anchor=tk.N)
# Combobox com as opções de idioma
lang_var = tk.StringVar()
lang_combobox = ttk.Combobox(combo_frame, textvariable=lang_var)
lang_combobox['values'] = list(language_options.keys())
lang_var.set("Português")
lang_combobox.pack(expand=True, anchor=tk.S, pady=4)
combo_frame.pack(expand=True, anchor=tk.N, pady=1)
lang_combobox.bind("<<ComboboxSelected>>", update_language) # Bind para atualizar idioma
lang_var.trace_add("write", update_language)


# Adicionando um placeholder
entrada.insert(0, "Insira aqui o texto: ")
entrada.bind("<Button-1>" or "<Backspace>", click)
janela.bind("<Return>", enter)


#Iniciar o app
janela.mainloop()


