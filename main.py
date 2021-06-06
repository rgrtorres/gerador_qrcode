from tkinter import *
from tkinter import ttk
import def_qrcode

app = Tk()
app.title("Gerador QRCode")
app.geometry("300x200")

label1 = Label(app, text="Ação do QRCode")
label1.pack(side=TOP)

txt_qrcode = Entry(app, bd=1, width=30)
txt_qrcode.pack(side=TOP)

label2 = Label(app, text="Nome do Cliente")
label2.pack(side=TOP)

txt_cliente = Entry(app, bd=1, width=30)
txt_cliente.pack(side=TOP)

label3 = Label(app, text="Estilo de QRCode")
label3.pack(side=TOP)

estilo = ttk.Combobox(app, values=['Light', 'Dark'], width=27)
estilo.pack(side=TOP)

botao_gerarQr = Button(app, text="Gerar e Salvar QRCode", command=lambda: def_qrcode.geraQRCode(txt_qrcode.get(), txt_cliente.get(), estilo.get()))
botao_gerarQr.pack(side=TOP)

app.mainloop()