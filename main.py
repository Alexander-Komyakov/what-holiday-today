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
from kivy.graphics.vertex_instructions import RoundedRectangle
from kivy.graphics import BorderImage


class MyApp(App):
	def build(self):
		self.wind = Window
		self.wind.size = (480, 854)
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
			Color(22/255, 23/255, 16/255, .59)
			Rectangle(pos=(0,self.wind_size[1]-self.wind_size[1]*.1), 
					size=(self.wind_size[0], self.wind_size[1]*.1))
		with self.down.canvas.before:
			Color(22/255, 23/255, 16/255, .59)
			Rectangle(pos=(0,0), 
					size=(self.wind_size[0], 
					self.wind_size[1]*.15))
		with self.body.canvas.before:
			Color(22/255, 23/255, 16/255, .69)
			RoundedRectangle(pos=(self.wind_size[0]*.1,self.wind_size[1]*.2), 
					size=(self.wind_size[0]-self.wind_size[0]*.2, self.wind_size[1]-self.wind_size[1]*.35))
		self.down_icons = BoxLayout(size_hint=(1, .8), padding=[0,8,0,0])
		self.down_icons_name = BoxLayout(size_hint=(1, .2))
		self.down.add_widget(self.down_icons)
		self.down.add_widget(self.down_icons_name)

		self.down_icons.add_widget(Image(source="./images/tort.png"))
		self.down_icons.add_widget(Image(source="./images/tort2.png"))
		self.down_icons.add_widget(Image(source="./images/bananIcon.png"))
		self.down_icons.add_widget(Image(source="./images/gear.png"))

		self.down_icons_name.add_widget(Label(text="Сегодня", 
											color=(4/255, 4/255, 3/255), 
											halign="center"))
		self.down_icons_name.add_widget(Label(text="Завтра", 
											color=(4/255, 4/255, 3/255), 
											halign="center"))
		self.down_icons_name.add_widget(Label(text="Кликер", 
											color=(4/255, 4/255, 3/255), 
											halign="center"))
		self.down_icons_name.add_widget(Label(text="Темы", 
											color=(4/255, 4/255, 3/255), 
											halign="center"))

		self.head.add_widget(Label(text="Календарь счастливых людей", 
									color=(4/255, 4/255, 3/255), 
									halign="center", 
									font_size="20sp"))
		self.body_cap = BoxLayout(size_hint=(1,.15), orientation="vertical")
		self.body_text = BoxLayout(size_hint=(1,.3), orientation="vertical")
		self.body_image = BoxLayout(size_hint=(1,.4), 
									orientation="vertical",
									pos_hint={"top:":0.5},
									padding=(self.wind_size[0]*.15,0,self.wind_size[0]*.15,0))
		self.body_cap2 = BoxLayout(size_hint=(1,.15), orientation="vertical")

		self.body.add_widget(self.body_cap)
		self.body.add_widget(self.body_text)
		self.body.add_widget(self.body_image)
		self.body.add_widget(self.body_cap2)
		self.body_text.add_widget(Label(text="""15  мая 2022 года, \
воскресенье: День семей, День климата, 155 лет 'Российскому \
обществу Креста', день рождения черного тюльпана""",
									color=(4/255, 4/255, 3/255), 
									halign="center", 
									valign="center", 
									font_size="18sp",
									text_size=(self.wind_size[0]*.7, self.wind_size[1]*.3),))
		self.img = Image(source="./images/imageTmp.png")
		self.img = MyImage(source="./images/imageTmp.png")
		self.body_image.add_widget(self.img)

class MyImage(Image):
	def __init__(self, **kwargs):
		super(MyImage, self).__init__(**kwargs)
		with self.canvas.before:
			RoundedRectangle(pos=self.pos, 
					pos_hint={"top":0})
#			print(dir(RoundedRectangle))
#					size=self.texture.size)
		print("TEXTURE DIR: ", dir(self.texture))
		print(self.texture.uvsize)
		print(self.texture.width)
		print(self.texture.height)
		print(self.width)
		print(self.height)
		print(str(self.texture_size))


if __name__ == "__main__":
	app = MyApp()
	app.run()
