#Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando!')
            return
        print('Filmando...')
        self.filmando = True
    
    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando!')
            return
        print('Parando de filmar...')
        self.filmando = False

    
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar enquanto filma!')
            return
        print(f'Fotografando...')

camera1 = Camera('Kodak')
camera2 = Camera('Canon')

camera1.parar_filmar()
camera1.filmar()
camera1.fotografar()
camera1.parar_filmar()
camera1.fotografar()
print()
camera2.filmar()
camera2.parar_filmar()
camera2.fotografar()
camera2.parar_filmar()
camera2.fotografar()