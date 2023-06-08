
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.set('kivy','window_icon','icon.ico')
import kivy
import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder





from kivy.uix.image import Image

from kivy.uix.floatlayout import FloatLayout


# Set the app size


#Window.size = (400, 600)

Builder.load_file('layout.kv')


class MyLayout(Widget):

    def on_state1(self):
        global combustivel
        combustivel = self.ids.toggle1.text
        #self.ids.resultado.text = combustivel

    def on_state2(self):
        global combustivel
        combustivel = self.ids.toggle2.text
       # self.ids.resultado.text = combustivel

    def botao_ok(self):

        #combustivel = self.ids.resultado.text
        valor = self.ids.preco.text
        valor = valor.replace(',' , '.')
        try:
             if combustivel == "Gasolina":
                total = float(valor) * 0.7
                if total >= 0:
                    final = round(total, 2)

                    self.ids.resultado.text = f'O álcool tem que estar ' \
                                         f' acima de\n R$ {str(final).replace(".", ",")}  para a gasolina valer a pena! '
                else:
                    self.ids.resultado.text = f'Digite um valor acima de zero! '

             elif combustivel == "Álcool":
                total = float(valor) / 0.7
                if total >= 0:
                    final = round(total, 2)

                    self.ids.resultado.text =f'A gasolina tem que estar ' \
                                       f' acima de\n R$ {str(final).replace(".","," )}  para o álcool valer a pena! '
                else:
                    self.ids.resultado.text = f'Digite um valor acima de zero! '
             else:
                self.ids.resultado.text = f'Escolha um combustível!'
        except:

                self.ids.resultado.text = (f'ERRO! Escolha um combustível\n e digite um' \
                                          f' preço válido!')



# Esta parte do código abaixo é para o app ir à tela.
class Gasolina_ou_ÁlcoolApp(App):
    def build(self):
        self.icon = r'C:\Users\Renato\Documents\Py_charm\Gasolina_ou_Alcool_py\icon.png'
        # cor do main layout
        #Window.clearcolor = (193/255,193/255,193/255,1)
       # Window.clearcolor = (0,128/255,1,1)
       # Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()


if __name__ == '__main__':
    Gasolina_ou_ÁlcoolApp().run()