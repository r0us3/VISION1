from kivy.app import App
from kivy.lang import Builder
from kivy.uix.camera import Camera

KV = """
Button:
    text: "Load"
    size_hint: None, None
    size: 100, 50
    pos_hint: {"center_y": .1, "center_x": .5}
"""


class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

        return Camera(play=True, index=1, resolution=(640, 480))


MyApp().run()