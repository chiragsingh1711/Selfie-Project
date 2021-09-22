from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        self.camera_object = Camera()

        #Button
        self.button_object = Button(text="Take Selfie")
        self.button_object.size_hint = (0.2, 0.2 )
        self.button_object.pos_hint = {'x': 0.25, 'y': 0}
        self.button_object.bind(on_press = self.take_selfie)

        #Layout
        self.layout_object = BoxLayout()
        self.layout_object.add_widget(self.camera_object)
        self.layout_object.add_widget(self.button_object)
        return self.layout_object

    def take_selfie(self, *args):
        print("Selfie Done")
        name = "Database/Selfie.png"
        self.camera_object.export_to_png(name)

if __name__ == '__main__':
    app = MainApp()
    app.run()