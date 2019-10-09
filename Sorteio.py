import random
from tkinter import *
import turtle as tt

continuar = True
lista_item = []

contador_item = 0
while continuar:
    item = []
    #item_nome = input("Informe o nome do item ou digite X para sair: ")
    item_nome = tt.textinput("Itens de sorteio","Informe o nome do item ou digite X para sair: ")

    if item_nome == "" or item_nome is None:
        continuar = False
    elif item_nome.upper() == "X":
        continuar = False
    else:
        contador_item += 1
        item_qtd = 0
        item.append(contador_item)
        item.append(item_nome)
        item.append(item_qtd)
        lista_item.append(item)
"""   
item = []
item.append(1)
item.append("REST")
item.append(0)
lista_item.append(item)

item = []
item.append(2)
item.append("SOA")
item.append(0)
lista_item.append(item)

item = []
item.append(3)
item.append("WEBSERVICE")
item.append(0)
lista_item.append(item)
"""
num_item_final = len(lista_item)
#print("Tamanho da lista: ",num_item_final)

#colocar a tartaruga (caneta)
caneta = tt.Pen()
tt.bgcolor("black")
tt.resetscreen()
#tt.screensize(100,100,"gray")
tentativas = int(tt.numinput("Qual a sua escolha?","3 tentativas\n5 tentativas\nOutra? Informe",3))
caneta.speed(10)
#print(tt.screensize())

# Lista de cores
cores = ["red","yellow","blue","green","orange","purple","white","gray"]

for x in range(1,tentativas+1):
    
    # Obtem o número sorteado do primeiro ao último número da lista
    numero_sorteado = random.randint(1,num_item_final)
    #print("Número sorteado: ",numero_sorteado)

    #print("Tentativa: ",x)
    for x in range(0,len(lista_item)):
        indice_cor = random.randrange(0,len(cores)-1)   # sorteio um número entre 0 e o último índice da lista de cores
        caneta.pencolor(cores[indice_cor])  # atribui o índice definindo qual cor será utilizada no desenho do círculo
        caneta.circle(50)   # desenha círculo definindo o raio
        caneta.left(360/tentativas)     # define o grau de virada como padrão para que cada círculo seja uniformemente espaçado
        if lista_item[x][0] == numero_sorteado:
            #print(lista_item[x][1])
            #texto = lista_item[x][1]
            #print(texto)
            lista_item[x][2] = lista_item[x][2] + 1
            break
    caneta.left(7)
tt.bye()

# iterar na lista de valores e gerar string para impressão
texto=""
for item in lista_item:
    texto = texto + "{0:<30}".format(item[1]) + "{:4d}".format(item[2]) +"\n"

# Usando Tkinter
class Aplicacao (Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.msg = Label(self, text=texto, justify="left", pady=30)
        self.msg.pack()
        #self.bye = Button (self, text="Ok", command=self.quit)
        #self.bye.pack()
        self.pack()

    def limpar(self):
        self.destroy()

app = Aplicacao()
app.master.title("Sorteio")
app.master.geometry("250x200+100+100")
mainloop()
