import customtkinter as ctk

ctk.set_appearance_mode("dark")     # dark, system, light
ctk.set_default_color_theme("blue") # blue, green, dark-blue

class Aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()
        # executa meus codigos personalizados
        self.title("Sistema de Cadastros de Clientes")
        self.geometry("900x600")

        # criar divisao da tela  weight = 1 -> expande junto com a tela
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # parte lateral
        self.barra_lateral = ctk.CTkFrame(self, width=200)
        self.barra_lateral.grid(row=0, column=0, sticky="nsew")

        # parte principal
        self.janela_abas = ctk.CTkTabview(self, width=400)
        self.janela_abas.grid(row=0, column=1, sticky="nsew", padx=10)

        self.janela_abas.add("Perfil")
        self.janela_abas.add("Preferencias")
        self.janela_abas.add("Dashboard")

        # preencher as partes/abas
        
        # preencher aba lateral
        self.construir_aba_lateral()
        # preencher aba perfil
        self.construir_aba_perfil()
        # preencher aba preferencias
        self.construir_aba_preferencias()
        # preencher aba sistema
        self.construir_aba_sistema()


    def construir_aba_lateral(self):
        # titulo
        self.titulo = ctk.CTkLabel(self.barra_lateral, 
                                   text="Meu app",
                                   font=ctk.CTkFont(size=24, weight="bold"))
        self.titulo.pack(pady=(30, 10), padx=(20,20))

        #botao
        self.botao_principal = ctk.CTkButton(self.barra_lateral,
                                             text="Dashboard Principal")

        self.botao_principal.pack(pady=(30.30), padx=(20,20))

        # switch
        self.switch_mododark = ctk.CTkSwitch(self.barra_lateral,
                                             text="Modo Escuro")
        self.switch_mododark.pack(pady=(10,10), side="bottom")

    def construir_aba_perfil(self):
        self.aba_perfil = self.janela_abas.tab("Perfil")
        # campo nome
        self.campo_nome = ctk.CTkEntry(self.aba_perfil,
                                  placeholder_text="Digite seu nome",
                                  width=300)

        self.campo_nome.pack(pady=(20,20))

        # nivel usuario -> radio button

        self.nivel_usuario = ctk.IntVar(value=0)

        # titulo 
        self.radio_label = ctk.CTkLabel(self.aba_perfil, text="Nivel Usuario")
        self.radio_label.pack()

        # radio basico
        self.radio_basico = ctk.CTkRadioButton(self.aba_perfil,
                                               text="Basico",
                                               variable=self.nivel_usuario,
                                               value=1)
        self.radio_basico.pack()


        # radio admin
        self.radio_admin = ctk.CTkRadioButton(self.aba_perfil,
                                              text="Admin",
                                              variable=self.nivel_usuario,
                                              value=2)
        self.radio_admin.pack()


        # notificacoes -> checkbox
        self.checkbox_notificacoes = ctk.CTkCheckBox(self.aba_perfil,
                                                    text="Receber notificacpes por email")
        self.checkbox_notificacoes.pack(pady=(20,20))

        # salvar perfil -> botao
        self.botao_salvarPerfil = ctk.CTkButton(self.aba_perfil,
                                                text="Salvar perfil",
                                                fg_color="green",
                                                hover_color="darkgreen")
        self.botao_salvarPerfil.pack(pady=(20,20))
        

    def construir_aba_preferencias(self):
        self.aba_preferencas = self.janela_abas.tab("Preferencias")

        # idioma -> label

        self.idioma_label = ctk.CTkLabel(self.aba_preferencas,
                                         text="Selecione o idioma:")
        self.idioma_label.pack(pady=(20,5))

        # idioma -> menu dropdown
        self.menu_idiomas = ctk.CTkOptionMenu(self.aba_preferencas,
                                              values=["Portgues", "Ingles", "Espanhol"])
        self.menu_idiomas.pack()

        #volume -> label
        self.label_volume = ctk.CTkLabel(self.aba_preferencas,
                                         text="Volume do sistema")
        self.label_volume.pack(pady=(10))

        #volume -> slider
        self.slider_volume = ctk.CTkSlider(self.aba_preferencas,
                                           from_=0, to=100)
        self.slider_volume.pack()
        self.slider_volume.set(50)

        #volume % -> label~
        self.label_valorVolume = ctk.CTkLabel(self.aba_preferencas,
                                              text="50%")
        self.label_valorVolume.pack()

    def construir_aba_sistema(self):
        pass
        




janela = Aplicativo()

janela.mainloop()