from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText

class CalculadoraApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        # 1. LAYOUT PRINCIPAL: MDBoxLayout Vertical
        layout_principal = MDBoxLayout(
            orientation='vertical',
            padding=15,
            spacing=10
        )

        # --- Panel Superior (Vista Secundaria y Pantalla Principal) ---
        panel_pantallas = MDBoxLayout(
            orientation='vertical',
            size_hint_y=0.3,
            spacing=5
        )

        # Vista secundaria (Historial / Operaciones previas)
        self.vista_secundaria = MDLabel(
            text="Historial de Operaciones",
            halign="right"
        )

        # Pantalla principal de resultados
        self.pantalla = MDLabel(
            text="0",
            halign="right",
            bold=True
        )

        panel_pantallas.add_widget(self.vista_secundaria)
        panel_pantallas.add_widget(self.pantalla)

        # 2. LAYOUT DE BOTONES: MDGridLayout 4 columnas x 5 filas
        panel_botones = MDGridLayout(
            cols=4,
            rows=5,
            spacing=8,
            size_hint_y=0.7
        )

        # Distribución del teclado (20 botones en total)
        botones = [
            "C", "CE", "%", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "+/-", "0", ".", "="
        ]

        for texto in botones:
            btn = MDButton(
                MDButtonText(text=texto),
                size_hint=(1, 1),
                on_release=self.on_button_press
            )
            panel_botones.add_widget(btn)

        # Agregar contenedores al layout principal
        layout_principal.add_widget(panel_pantallas)
        layout_principal.add_widget(panel_botones)

        return layout_principal

    def on_button_press(self, instance):
        # En KivyMD 2.0 el texto está dentro del primer hijo (MDButtonText)
        comando = instance.children[0].text

        if comando in ["C", "CE"]:
            self.pantalla.text = "0"
            self.vista_secundaria.text = "Historial de Operaciones"
        elif comando == "=":
            self.vista_secundaria.text = f"{self.pantalla.text} ="
        else:
            if self.pantalla.text == "0":
                self.pantalla.text = comando
            else:
                self.pantalla.text += comando

if __name__ == "__main__":
    CalculadoraApp().run()