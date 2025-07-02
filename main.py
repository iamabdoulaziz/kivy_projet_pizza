from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.behaviors import CoverBehavior
from models import Pizza


class PizzaWidget(BoxLayout):
    name = StringProperty()
    ingredients = StringProperty()
    price = NumericProperty()
    vegetarian = BooleanProperty()

class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pizzas = [
            Pizza("4 fromages", "chèvre, emmental, brie, comté", 9.5, True),
            Pizza("Chorizo", "tomates, chorizo, parmesan", 11.2, False),
            Pizza("Calzone", "fromage, jambon, champignons, ", 10, False)

        ]

    def on_parent(self, widget, parent):
        pizza_list = [pizza.get_dictionary() for pizza in self.pizzas]
        self.recycleView.data = pizza_list


class PizzaApp(App):
    pass

PizzaApp().run()
