import requests
from tkinter import *
from PIL import Image, ImageTk
import formas

def mostrarImagem():
    formas.plotarImagem()
    widget1 = Frame()
    widget1.pack()
    
    # imagem = ImageTk.PhotoImage(Image.open("bola.jpg"))
    image = Image.open("image.jpg")
    photo = ImageTk.PhotoImage(image)
    imagem = Label(text = "adicionando", image = photo)
    imagem.image = photo
    imagem.pack()

    teste = Label(widget1, text="testando")
    teste.pack()

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto_resposta['text'] = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

janela = Tk()
janela.title("Trabalho Comkputacao Grafica")
texto = Label(janela, text="Clique no botão para ver as cotações de moedas")
texto.grid(column=0, row=0, padx=10, pady=10)

#botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
botao = Button(janela, text="Buscar cotações", command=mostrarImagem)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)




janela.mainloop()