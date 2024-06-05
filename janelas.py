import customtkinter
from pegar_moedas import nome_moedas
from pegar_moedas import conver_disp
from pegar_cotacao import convert_moeda

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('dark-blue')

janela = customtkinter.CTk()
janela.geometry("500x500")

dic_conver_dips = conver_disp()

titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("Arial",20))
text_moedas_origem = customtkinter.CTkLabel(janela, text="Moeda Origem:")
text_moedas_destino = customtkinter.CTkLabel(janela, text="Moeda Destino:")
text_result = customtkinter.CTkLabel(janela, text="Resultado:")
text_cot = customtkinter.CTkLabel(janela, text="")
text_qtd = customtkinter.CTkLabel(janela, text="Digite o valor:")
campo_qtd = customtkinter.CTkTextbox(janela, width=200, height=10)

def carregar_moedas_dist(moeda_selecionada):
    lista_moedas_dist = dic_conver_dips[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_dist)
    campo_moeda_destino.set(lista_moedas_dist[0])

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, width=200, height=30 ,values=list(dic_conver_dips.keys()), command=carregar_moedas_dist)
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, width=200, height=30 ,values=["Selecione uma Moeda"])

def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_dist = campo_moeda_destino.get()
    qtd_moeda = campo_qtd.get("1.0", "end-1c")
    if moeda_origem and moeda_dist and qtd_moeda:
        cot = convert_moeda(moeda_origem, moeda_dist)
        text_cot.configure(text= f"{float(qtd_moeda)} {moeda_origem} = {float(cot)*float(qtd_moeda)} {moeda_dist}")

btc_conver = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)
lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disp = nome_moedas()
for codigo_moeda in moedas_disp:
    nome_moedas = moedas_disp[codigo_moeda]
    text_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moedas}")
    text_moeda.pack()

titulo.pack(padx=10, pady=20)
text_moedas_origem.place(x=50, y=79)
campo_moeda_origem.pack(padx=10, pady=10)
text_moedas_destino.place(x=50, y=129)
campo_moeda_destino.pack(padx=10, pady=10)
text_qtd.place(x=50, y=179)
campo_qtd.pack(padx=10, pady=10)
btc_conver.pack(padx=10, pady=10)
text_cot.pack(padx=10, pady=10)
text_result.place(x=50,y=278)
lista_moedas.pack(padx=10, pady=10)

janela.mainloop()