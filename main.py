from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout

class CameraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.camera = Camera(play=True)
        button = Button(text='Capture', on_press=self.capture)
        layout.add_widget(self.camera)
        layout.add_widget(button)
        return layout

    def capture(self, event):
        # Aquí debes implementar la lógica para procesar la imagen de la cámara y extraer el número de la barra.
        pass

if __name__ == '__main__':
    CameraApp().run()
