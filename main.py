from tkinter import *
from tkinter import ttk
from math import sqrt

#cores

corpreta = "#000000"
corLaranja ="#e36200"
corBranca = "#edeae8"
corCinza = "#999897"
corAzul ="#002fd9"

janela = Tk()
janela.title("calculadora")
janela.geometry("300x420")
janela.config(bg=corpreta)


Frame_espaco = Frame(janela,width=300,height=5, bg=corpreta)
Frame_espaco.grid(row=0,column=0)


Frame_tela = Frame(janela,width=300,height=50, bg=corAzul)
Frame_tela.grid(row=1,column=0)

Frame_espaco = Frame(janela,width=300,height=5, bg=corpreta)
Frame_espaco.grid(row=2,column=0)


Frame_corpo = Frame(janela,width=300,height=360)
Frame_corpo.grid(row=3,column=0)


todos_valores = ''

#criando função
def entrar_valor(event):
    global todos_valores
    todos_valores= todos_valores + str(event)

#colocando resultdo na tela
    valor_texto.set(todos_valores)



#calculando resultado
def calcular(event):
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
       

#função limpar tela
def limpar_tela(event):
    global todos_valores
    todos_valores=''
    valor_texto.set("")




#criando label

valor_texto = StringVar()
app_label = Label(Frame_tela,textvariable=valor_texto ,width=19,height=2,padx=7,relief=FLAT,anchor="e",justify=RIGHT,font="Ivy 18 bold",bg=corAzul,fg=corBranca)
app_label.place(x=0,y=0)

#botoes
b_1 = Button(Frame_corpo,command= lambda: limpar_tela("C") ,text="C",width=18,height=3,bg=corCinza,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_1.place(x=0,y=0)
b_2 = Button(Frame_corpo,command= lambda: entrar_valor("%"), text="%",width=10,height=3,bg=corCinza,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_2.place(x=150,y=0)
b_3 = Button(Frame_corpo, command= lambda: entrar_valor("/"), text="/",width=10,height=3,bg=corLaranja,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_3.place(x=225,y=0)

b_4 = Button(Frame_corpo, command= lambda: entrar_valor("7"), text="7",width=10,height=3,bg=corCinza,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_4.place(x=0,y=60)
b_4 = Button(Frame_corpo, command= lambda: entrar_valor("8"), text="8",width=10,height=3,bg=corCinza,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_4.place(x=75,y=60)
b_4 = Button(Frame_corpo, command= lambda: entrar_valor("9"), text="9",width=10,height=3,bg=corCinza,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_4.place(x=150,y=60)
b_4 = Button(Frame_corpo, command= lambda: entrar_valor("*"), text="x",width=10,height=3,bg=corLaranja,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_4.place(x=225,y=60)

b_5 = Button(Frame_corpo, command= lambda: entrar_valor("4"), text="4",width=10,height=3,bg=corCinza,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_5.place(x=0,y=120)
b_5 = Button(Frame_corpo, command= lambda: entrar_valor("5"),text="5",width=10,height=3,bg=corCinza,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_5.place(x=75,y=120)
b_5 = Button(Frame_corpo,command= lambda: entrar_valor("6"), text="6",width=10,height=3,bg=corCinza,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_5.place(x=150,y=120)
b_5 = Button(Frame_corpo,command= lambda: entrar_valor("-"), text="-",width=10,height=3,bg=corLaranja,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_5.place(x=225,y=120)

b_6 = Button(Frame_corpo, command= lambda: entrar_valor("1"),text="1",width=10,height=3,bg=corCinza,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_6.place(x=0,y=180)
b_6 = Button(Frame_corpo, command= lambda: entrar_valor("2"), text="2",width=10,height=3,bg=corCinza,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_6.place(x=75,y=180)
b_6 = Button(Frame_corpo, command= lambda: entrar_valor("3"), text="3",width=10,height=3,bg=corCinza,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_6.place(x=150,y=180)
b_6 = Button(Frame_corpo, command= lambda: entrar_valor("+"), text="+",width=10,height=3,bg=corLaranja,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_6.place(x=225,y=180)

b_7 = Button(Frame_corpo, command= lambda: entrar_valor("0"), text="0",width=18,height=3,bg=corCinza,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_7.place(x=0,y=240)
b_8 = Button(Frame_corpo, command= lambda: entrar_valor("."),text=".",width=10,height=3,bg=corCinza,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_8.place(x=150,y=240)
b_9 = Button(Frame_corpo,command= lambda: calcular("="), text="=",width=10,height=3,bg=corLaranja,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_9.place(x=225,y=240)


b_10 = Button(Frame_corpo, command= lambda: entrar_valor("**"), text="^",width=18,height=3,bg=corCinza,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_10.place(x=0,y=300)
b_10 = Button(Frame_corpo, command= lambda: entrar_valor("("),text="(",width=10,height=3,bg=corCinza,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_10.place(x=150,y=300)
b_10 = Button(Frame_corpo,command= lambda: entrar_valor(")"), text=")",width=10,height=3,bg=corLaranja,font="Ivy 13 bold",relief=RAISED,overrelief=RIDGE)
b_10.place(x=225,y=300)



janela.mainloop()


