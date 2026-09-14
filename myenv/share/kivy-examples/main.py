from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import time

class ClickTestApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Etiqueta para tiempo restante
        self.time_label = Label(text="Presiona 'Empezar' para iniciar el test", font_size="20sp")
        self.layout.add_widget(self.time_label)

        # Etiqueta para clicks
        self.click_label = Label(text="Clicks: 0", font_size="18sp")
        self.layout.add_widget(self.click_label)

        # Botón para iniciar
        self.start_button = Button(text="Empezar", font_size="22sp", background_color=(0.2, 0.8, 0.2, 1))
        self.start_button.bind(on_press=self.start_test)
        self.layout.add_widget(self.start_button)

        # Botón de clicks (inicialmente deshabilitado)
        self.click_button = Button(text="¡Clic aquí!", font_size="24sp", background_color=(0.2, 0.6, 1, 1), disabled=True)
        self.click_button.bind(on_press=self.on_click)
        self.layout.add_widget(self.click_button)

        # Variables de control
        self.clicks = 0
        self.start_time = None
        self.test_duration = 5  # segundos
        self.test_running = False

        return self.layout

    def start_test(self, instance):
        # Reiniciar variables
        self.clicks = 0
        self.start_time = time.time()
        self.test_running = True

        # Actualizar UI
        self.time_label.text = f"Tiempo restante: {self.test_duration}s"
        self.click_label.text = "Clicks: 0"
        self.click_button.disabled = False
        self.start_button.disabled = True

        # Actualizar tiempo cada segundo
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)
        Clock.schedule_once(self.end_test, self.test_duration)

    def update_timer(self, dt):
        elapsed = int(time.time() - self.start_time)
        remaining = self.test_duration - elapsed
        if remaining > 0:
            self.time_label.text = f"Tiempo restante: {remaining}s"

    def on_click(self, instance):
        if self.test_running:
            self.clicks += 1
            self.click_label.text = f"Clicks: {self.clicks}"

    def end_test(self, dt):
        self.test_running = False
        Clock.unschedule(self.timer_event)
        elapsed = time.time() - self.start_time
        cps = self.clicks / elapsed if elapsed > 0 else 0

        # Mostrar resultados
        self.time_label.text = f"Test terminado 🎉"
        self.click_label.text = f"Clicks totales: {self.clicks}\nCPS: {cps:.2f}"

        # Desactivar botón de clicks y habilitar reinicio
        self.click_button.disabled = True
        self.start_button.disabled = False
        self.start_button.text = "Empezar de nuevo"

if __name__ == "__main__":
    ClickTestApp().run()
