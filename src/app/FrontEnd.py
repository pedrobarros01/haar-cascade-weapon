import tkinter as tk
from pathlib import Path
from src.app.ETLRetangle import RectangleYOLO
from src.app.HarCascade import cascade_video
from tkinter import ttk
import os
from tkinter import filedialog

class TelaConfig(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Haar Cascade")
        self.geometry("862x519")
        self.resizable(False, False)
        self.configure(bg="#3A7FF6")
        self.frames = {}
        for F in (TelaInicial, TelaVideo, TelaTreino, TelaDescricao):
            name_page = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[name_page] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.tela_atual = None
        self.trocar_tela('TelaInicial')
        
    def limpar_tela_anterior(self):
        if self.tela_atual:
            for widget in self.tela_atual.winfo_children():
                widget.destroy() 
    def trocar_tela(self, nome):
        self.limpar_tela_anterior()
        frame = self.frames[nome]
        frame.__init__(self, self)
        self.tela_atual = frame


class TelaInicial(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        canvas = tk.Canvas(
            self.controller,
            bg="#3A7FF6",
            height=519,
            width=862,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        canvas.create_text(
            69.0,
            91.0,
            anchor="nw",
            text="Bem vindo ao GUI do Haar Cascade de armas",
            fill="#FCFCFC",
            font=("Roboto Bold", 24 * -1)
        )

        canvas.create_text(
            69.0,
            155.0,
            anchor="nw",
            text="Aqui você poderá realizar 2 funções:\nPreparação do treino\nUpload de vídeo\n\nAperte o botão de descrição para mais detalhe",
            fill="#FCFCFC",
            font=("Inter", 16 * -1)
        )

        button_image_1 = tk.PhotoImage(file='src/images/frame0/button_1.png')
        button_1 = tk.Button(
            self.controller,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.trocar_tela('TelaTreino'),
            relief="flat"
        )
        button_1.image = button_image_1  # Manter a referência da imagem
        button_1.place(x=61.0, y=370.0, width=143.0, height=47.0)

        button_image_2 = tk.PhotoImage(file='src/images/frame0/button_2.png')
        button_2 = tk.Button(
            self.controller,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.trocar_tela('TelaDescricao'),
            relief="flat"
        )
        button_2.image = button_image_2  # Manter a referência da imagem
        button_2.place(x=231.0, y=370.0, width=143.0, height=47.0)

        button_image_3 = tk.PhotoImage(file='src/images/frame0/button_3.png')
        button_3 = tk.Button(
            self.controller,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.trocar_tela('TelaVideo'),
            relief="flat"
        )
        button_3.image = button_image_3  # Manter a referência da imagem
        button_3.place(x=401.0, y=370.0, width=143.0, height=47.0)

        image_image_1 = tk.PhotoImage(file='src/images/frame0/image_1.png')
        canvas.create_image(718.0, 219.0, image=image_image_1)

        # Manter a referência da imagem no widget para evitar que seja removida pelo garbage collector
        self.image_image_1 = image_image_1

    def comando_treino(self):
        self.controller.trocar_tela('TelaTreino')

    def comando_video(self):
        self.controller.trocar_tela('TelaVideo')


        


class TelaVideo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        self.classificador = ''
        self.arquivo = ''
        self.lista_arqs_classificadores = self.pegar_classificadores()
        canvas = tk.Canvas(
            self.controller,
            bg="#3A7FF6",
            height=519,
            width=862,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # Título da tela
        canvas.create_text(
            69.0,
            91.0,
            anchor="nw",
            text="Digite as informações a seguir:",
            fill="#FCFCFC",
            font=("Roboto Bold", 24 * -1)
        )
        
       

        # Segundo botão
        button_image_2 = tk.PhotoImage(
            file='src/images/frame3/button_2.png')
        button_2 = tk.Button(
            self.controller,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.upload_video(),
            relief="flat"
        )
        button_2.image = button_image_2  # Manter referência à imagem
        button_2.place(
            x=84.0,
            y=236.0,
            width=257.0,
            height=47.0
        )

        # Texto descritivo
        canvas.create_text(
            107.0,
            131.0,
            anchor="nw",
            text="Caminho do classificador",
            fill="#F6F7F9",
            font=("Inter Bold", 13 * -1)
        )

        
        entry_1 = ttk.Combobox(
            self.controller,
            values=self.lista_arqs_classificadores
        )
        entry_1.place(
            x=103.0,
            y=158.0,
            width=220.0,
            height=35.0
        )

        # Primeiro botão
        button_image_1 = tk.PhotoImage(
            file='src/images/frame3/button_1.png')
        button_1 = tk.Button(
            self.controller,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.iniciar_teste(entry_1),
            relief="flat"
        )
        button_1.image = button_image_1  # Manter referência à imagem
        button_1.place(
            x=84.0,
            y=309.0,
            width=257.0,
            height=47.0
        )
        # Imagem de fundo ou decorativa
        image_image_1 = tk.PhotoImage(file='src/images/frame3/image_1.png')
        canvas.create_image(718.0, 219.0, image=image_image_1)
    
    def pegar_classificadores(self):
        list_dir = os.listdir('src/haarcascades/')
        lista = [arq for arq in list_dir if arq.find('.xml')]
        return lista
    
    def upload_video(self):
        arquivo = filedialog.askopenfilename(title='Selecione o vídeo', filetypes=[("Arquivos MP4", "*.mp4")])
        if arquivo:
            self.arquivo = arquivo
        else:
            self.arquivo = ''
            print('Video nao carregado')
    
    def iniciar_teste(self, comboBox):
        valor = comboBox.get()
        if self.arquivo != '' and valor != '':
            print(valor)
            classificador = os.path.join('src/haarcascades', valor)
            cascade_video(classificador, self.arquivo)


class TelaDescricao(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        canvas = tk.Canvas(
            self.controller,
            bg="#3A7FF6",
            height=519,
            width=862,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # Título da descrição
        canvas.create_text(
            69.0,
            91.0,
            anchor="nw",
            text="Descrição",
            fill="#FCFCFC",
            font=("Roboto Bold", 24 * -1)
        )

        # Texto explicativo
        canvas.create_text(
            69.0,
            146.0,
            anchor="nw",
            text=(
                "Na preparação de treino você fornecerá a quantidade de imagens positivas e negativas "
                "para criar a amostra utilizada no treino.\n"
                "Lembrete: O código não realiza o treino, ele começa o início do treino e oferece o comando "
                "do treino para ser aplicado no terminal.\n\n"
                "Em UPLOAD você fornecerá o caminho do classificador e do vídeo e observará o teste da "
                "detecção de objetos."
            ),
            fill="#FCFCFC",
            font=("Inter", 12 * -1)
        )

        # Imagem ilustrativa
        image_image_1 = tk.PhotoImage(
            file='src/images/frame1/image_1.png')
        canvas.create_image(
            470.0,
            326.0,
            image=image_image_1
        )


class TelaTreino(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.quant_pos = -1
        self.quant_neg = -1
        self.quant_epoca = -1
        self.controller = controller
        canvas = tk.Canvas(
            self.controller,
            bg="#3A7FF6",
            height=519,
            width=862,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        
        canvas.create_text(
            69.0,
            91.0,
            anchor="nw",
            text="Digite as informações a seguir:",
            fill="#FCFCFC",
            font=("Roboto Bold", 24 * -1)
        )

        
        canvas.create_text(
            113.0,
            131.0,
            anchor="nw",
            text="Quantidade de imagens positivas",
            fill="#F6F7F9",
            font=("Inter Bold", 13 * -1)
        )

        entry_image_1 = tk.PhotoImage(file='src/images/frame2/entry_1.png')
        entry_bg_1 = canvas.create_image(219.0, 176.5, image=entry_image_1)
        entry_1 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(x=109.0, y=158.0, width=220.0, height=35.0)
        entry_1.image = entry_image_1  # Manter a referência da imagem

        canvas.create_text(
            113.0,
            220.0,
            anchor="nw",
            text="Quantidade de imagens negativas",
            fill="#F6F7F9",
            font=("Inter Bold", 13 * -1)
        )

        entry_image_2 = tk.PhotoImage(file='src/images/frame2/entry_2.png')
        entry_bg_2 = canvas.create_image(219.0, 265.5, image=entry_image_2)
        entry_2 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(x=109.0, y=247.0, width=220.0, height=35.0)
        entry_2.image = entry_image_2  # Manter a referência da imagem

        canvas.create_text(
            113.0,
            309.0,
            anchor="nw",
            text="Quantidade de epocas",
            fill="#F6F7F9",
            font=("Inter Bold", 13 * -1)
        )

        entry_image_3 = tk.PhotoImage(file='src/images/frame2/entry_3.png')
        entry_bg_3 = canvas.create_image(219.0, 365.5, image=entry_image_3)
        entry_3 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(x=109.0, y=347.0, width=220.0, height=35.0)
        entry_3.image = entry_image_3  # Manter a referência da imagem

        button_image_1 = tk.PhotoImage(file='src/images/frame2/button_1.png')
        button_1 = tk.Button(
            self.controller,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.pegar_texto_inputs(entry_1, entry_2, entry_3),
            relief="flat"
        )
        button_1.place(x=84.0, y=409.0, width=257.0, height=47.0)
        button_1.image = button_image_1  # Manter a referência da imagem


        image_image_1 = tk.PhotoImage(file='src/images/frame2/image_1.png')
        self.image_image_1 = canvas.create_image(716.0, 227.0, image=image_image_1)
        self.image_image_1_ref = image_image_1  # Referência da imagem
    

    def pegar_texto_inputs(self,input1, input2, input3):
        self.quant_pos = input1.get()
        self.quant_neg = input2.get()
        self.quant_epoca = input3.get()
        print(self.quant_epoca, self.quant_neg, self.quant_pos)
        if self.quant_epoca != '' and self.quant_neg != '' and self.quant_pos != '':
            os.remove('amostras.lst')
            os.remove('bg.txt')
            os.remove('positives.vec')
            comando = RectangleYOLO.prepare_train(int(self.quant_pos), int(self.quant_neg), int(self.quant_epoca))
            print('Comando: ' + comando)

        
        



