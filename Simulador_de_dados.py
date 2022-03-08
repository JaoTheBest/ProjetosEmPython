import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        #layout
        self.layout = [
            [sg.Text('Jogar o Dado?')],
            [sg.Button('sim'),sg.Button('nao')]
        ]
    def Iniciar(self):
        self.janela = sg.Window('Simulador de dado', layout=self.layout)
        #ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        #fazer alguma coisa com esses valores

        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'nao' or self.eventos == 'n':
                print('agradecemos sua participaçao')
            else:
                print('Favor digitar sim ou nao')
        except:
            print('ocorreu um erro ao receber sua resposta')
    
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()
