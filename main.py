from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

from models import Pizza


class PizzaWidget(BoxLayout):
    name = StringProperty()

class MainWidget(BoxLayout):
    recycleView = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pizzas = [
            Pizza("4 fromages", "chèvre, emmental, brie, comté", 9.5, True),
            Pizza("Chorizo", "tomates, chorizo, parmesan", 11.2, False),
            Pizza("Calzone", "fromage, jambon, champignons, ", 10, False)

        ]

    def on_parent(self, widget, parent):
        self.recycleView.data = [
            {"name": "4 fromages"},
            {"name": "Chorizo"}
        ]


class PizzaApp(App):
    pass

PizzaApp().run()
