from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty


class CalculadoraLayout(MDBoxLayout):

    pantalla = StringProperty("0")
    historial = StringProperty("Historial de Operaciones")

    def on_button_press(self, comando):

        if comando in ("C", "CE"):
            self.pantalla = "0"
            self.historial = "Historial de Operaciones"

        elif comando == "=":
            expresion = self.pantalla
            try:
                resultado = eval(expresion, {"__builtins__": {}})
                self.historial = f"{expresion} ="
                self.pantalla = str(resultado)
            except Exception:
                self.historial = f"{expresion} ="
                self.pantalla = "Error"

        elif comando == "+/-":
            if self.pantalla not in ("0", "Error"):
                if self.pantalla.startswith("-"):
                    self.pantalla = self.pantalla[1:]
                else:
                    self.pantalla = "-" + self.pantalla

        else:

            if self.pantalla in ("0", "Error"):
                self.pantalla = comando
            else:
                self.pantalla += comando


class CalculadoraApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        self.title = "Calculadora - KV Language"
        return CalculadoraLayout()


if __name__ == "__main__":
    CalculadoraApp().run()
