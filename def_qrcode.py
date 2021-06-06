import qrcode
import os
from datetime import datetime
from tkinter import messagebox, filedialog

# def validandoPasta(nomePasta):
#     nome_pasta = nomePasta
#     caminho = './' + nome_pasta

#     if not os.path.exists(caminho):
#         os.makedirs(caminho)

#     return caminho

def geraQRCode(url, cliente, estilo):
    if (url == "") or (cliente == "") or (estilo == ""):
        messagebox.showerror('ATENÇÃO', 'Por favor preenche todos os campos!')
    else:
        if (estilo == "Dark") or (estilo == "Light"):
            # validandoPasta('QRCode_gerados')

            diretorio = filedialog.askdirectory(initialdir="./", title="Selecione a pasta")

            #Configuração de salvamento, baseados na data e hora atual
            data_hora_atual = datetime.now()
            formato_dh = data_hora_atual.strftime('%d%m%Y%H%M%S')
            formato_salvar = cliente + formato_dh

            #Gera o QR Code
            geraQR = qrcode.QRCode(version=1,
                                    error_correction=qrcode.constants.ERROR_CORRECT_M,
                                    box_size=10,
                                    border=2)

            geraQR.add_data(url)
            geraQR.make(fit=True)

            if estilo == 'Dark':
                img = geraQR.make_image(fill_color="orange", back_color="black")
            elif estilo == 'Light':
                img = geraQR.make_image(fill_color="black", back_color="white")
            img.save(diretorio+'/'+ formato_salvar + '.png')

            messagebox.showinfo('Atenção', 'QRCode Gerado com sucesso')
        else:
            messagebox.showerror('ATENÇÃO', 'Escolha um estilo válido!')