import random, time, hashlib
from kivy.app import App
from kivy.base import runTouchApp, stopTouchApp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.utils import platform
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle, Color
from kivy.uix.image import Image
				

class MyApp(App):
	def build(self):
		self.wind = Window
		self.wind_width = self.wind.width
		self.wind_height = self.wind.height
		self.wind_size = (self.wind_width, self.wind_height)
		self.createScreenManager()
		return self.scman

	def createScreenManager(self):
		self.scman = ScreenManager()

		self.menu = Screen(name="Menu")
		self.scman.add_widget(self.menu)
		with self.menu.canvas.before:
			Rectangle(source="./images/background.png", size=(self.wind_size[0], self.wind_size[1]))

		self.bxMain = BoxLayout(orientation="vertical")
		self.menu.add_widget(self.bxMain)

		self.head = BoxLayout(size_hint=(1, .1), orientation="vertical")
		self.body = BoxLayout(size_hint=(1, .75), orientation="vertical")
		self.down = BoxLayout(size_hint=(1, .15), orientation="vertical")

		self.bxMain.add_widget(self.head)
		self.bxMain.add_widget(self.body)
		self.bxMain.add_widget(self.down)

		with self.head.canvas.before:
			Color(22/255, 23/255, 16/255, .89)
			Rectangle(pos=(0,self.wind_size[1]-self.wind_size[1]*.1), size=(self.wind_size[0], self.wind_size[1]*.1))
		with self.down.canvas.before:
			Color(22/255, 23/255, 16/255, .89)
			Rectangle(pos=(0,0), size=(self.wind_size[0], self.wind_size[1]*.15))

		self.down_icons = BoxLayout(size_hint=(1, .8))
		self.down_icons_name = BoxLayout(size_hint=(1, .2))
		self.down.add_widget(self.down_icons)
		self.down.add_widget(self.down_icons_name)

		self.down_icons.add_widget(Image(source="./images/tort.png"))
		self.down_icons.add_widget(Image(source="./images/tort2.png"))
		self.down_icons.add_widget(Image(source="./images/bananIcon.png"))
		self.down_icons.add_widget(Image(source="./images/gear.png"))

		self.down_icons_name.add_widget(Label(text="Сегодня", color=(4/255, 4/255, 3/255), halign="center"))
		self.down_icons_name.add_widget(Label(text="Завтра", color=(4/255, 4/255, 3/255), halign="center"))
		self.down_icons_name.add_widget(Label(text="Кликер", color=(4/255, 4/255, 3/255), halign="center"))
		self.down_icons_name.add_widget(Label(text="Темы", color=(4/255, 4/255, 3/255), halign="center"))

		self.head.add_widget(Label(text="Календарь счастливых людей", color=(4/255, 4/255, 3/255), halign="center", font_size="20sp"))

if __name__ == "__main__":
	app = MyApp()
	app.run()
