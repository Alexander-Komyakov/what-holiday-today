import random, time, hashlib
from kivy.app import App
from kivy.base import runTouchApp, stopTouchApp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.utils import platform
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
				

class MyApp(App):
	def build(self):
		self.wind = Window
		self.wind_width = self.wind.width
		self.wind_height = self.wind.height
		self.createScreenManager()
		return self.scman

	def createScreenManager(self):
		self.scman = ScreenManager()

		self.menu = Screen(name="Menu")
		self.scman.add_widget(self.menu)

if __name__ == "__main__":
	app = MyApp()
	app.run()
