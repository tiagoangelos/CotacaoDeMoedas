import requests
import datetime
import os
from tkinter import*
from tkinter import Entry

#FUNÇÃO
def programa():
    #DATA COMPLETA:
    dat = (datetime.datetime.now()) #OBJETO DATA
    dataHora = (dat.strftime("%H:%M:%S")) #FORMATEI A HORA PARA = HORA/MINUTO/SEGUNDOS
    dataDia = (dat.strftime("%d/%m/%y")) #FORMATEI A DATA PARA = DIA/MÊS/ANO

    #PASSEI ESSE VALORES DE = DATA + HORA PARA A VARIAVEL "dataFormatada"
    dataFormatada =  str("Data De Consulta:" + "\n" + str(dataDia) + " \n " + "[" + str(dataHora) + "]")

    #API
    api = requests.get("https://economia.awesomeapi.com.br/json/all")

    #PEGAR CONTEUDO NA API
    dolar = api.json()['USD']['bid']
    dolarCanadense = api.json()['CAD']['bid']
    euro = api.json()['EUR']['bid']
    bitCoin = api.json()['BTC']['bid']
    iene = api.json()['JPY']['bid']
    libra = api.json()['GBP']['bid']

    #PEGAR CONTEUDO SOLICITADO E IMPRIMIR CONTEUDO NA TELA
    resProgram = (f""
        f"Dólar Americano: {float(dolar):.2f} Reais\n"
        f"Dólar Canadense: {float(dolarCanadense):.2f} Reais\n"      
        f"Euro: {float(euro):.2f} Reais\n"
        f"Libra: {float(libra):.2f} Reais\n"
        f"Iene: {float(iene):.2f} Reais\n"
        f"Bitcoin: {float(bitCoin):.2f} Reais\n" 
    "")

    #IMPRIMIR CONTEUDO NA TELA
    conteudo['text'] = resProgram
    data['text'] = dataFormatada



#FIM - PROGRAMA ------------------------------------------------------------------------------------------------


#INTERFACE------------------------------------------------------------------------------------------------------
tela = Tk()
tela.resizable(0, 0)
tela.title("VALORES DAS MOEDAS")

texto_principal = Label(tela, text="Valor Das 6 Moedas\n Mais Importantes\n_______________________", foreground = "blue")
texto_principal.grid(column=0, row=0, padx=10, pady=10)
texto_principal.config(font = ("Helvitica, 20"))

botao = Button(tela, text="CONSULTAR", command = programa, foreground="red")
botao.grid(column=0, row = 1, padx=10, pady=10)
botao.config(font = ("Italic, 14"))

conteudo = Label(tela, text="", foreground = "black")
conteudo.grid(column=0, row=2, padx = 7, pady=7)
conteudo.config(font = ("Helvitica, 19"))

data = Label(tela, text="", foreground = "blue")
data.grid(column=0, row=4, padx = 8, pady=8)
data.config(font = ("Helvitica, 14"))

tela.mainloop()

