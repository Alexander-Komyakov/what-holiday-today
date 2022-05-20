from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle, Color
from kivy.uix.image import Image
from kivy.graphics.vertex_instructions import RoundedRectangle
from kivy.uix.carousel import Carousel
from kivy.uix.scrollview import ScrollView


if __name__ == "__main__":
	exit()

class MyUI():
	def build(self):
		self.wind = Window
		self.wind.size = (480, 854)
		self.wind_width = self.wind.width
		self.wind_height = self.wind.height
		self.wind_size = (self.wind_width, self.wind_height)
		self.size_head = (1, 0.06)
		self.size_body = (1, 0.75)
		self.size_down = (1, 0.1)
		self.size_down_icons = (.8, 1.1 - self.size_down[1])
		self.size_icons_name = (self.size_down_icons[0], 1 - self.size_down_icons[1])
		self.size_button = (1, .01)
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

		self.bodyCarousel = Carousel(size_hint=self.size_body)

		self.head = BoxLayout(size_hint=self.size_head, orientation="vertical")
		self.down = BoxLayout(size_hint=self.size_down, orientation="vertical")

		self.body = BoxLayout(size_hint=self.size_body, orientation="vertical")
		self.themeSwitch = BoxLayout(size_hint=(1,1), orientation="vertical")

		self.bodyCarousel.add_widget(self.body)
		self.bodyCarousel.add_widget(self.themeSwitch)

		self.bxMain.add_widget(self.head)
		self.bxMain.add_widget(self.bodyCarousel)
		self.bxMain.add_widget(self.down)


		with self.head.canvas.before:
			Color(22/255, 23/255, 16/255, .59)
			Rectangle(pos=(0,self.wind_size[1]-self.wind_size[1]*self.size_head[1]), 
					size=(self.wind_size[0], self.wind_size[1]*self.size_head[1]))
		with self.down.canvas.before:
			Color(22/255, 23/255, 16/255, .59)
			Rectangle(pos=(0,0), 
					size=(self.wind_size[0], 
					self.wind_size[1]*self.size_down[1]))
		self.down_icons = BoxLayout(size_hint=(1, .4), padding=[0,10,0,-10])
		self.down_icons_name = BoxLayout(size_hint=(1, .2))
		self.down.add_widget(self.down_icons)
		self.down.add_widget(self.down_icons_name)

		self.down_icons.add_widget(Image(source="./images/tort.png", 
										size_hint=self.size_down_icons))
		self.down_icons.add_widget(Image(source="./images/tort2.png",
										size_hint=self.size_down_icons))
		self.down_icons.add_widget(Image(source="./images/bananIcon.png",
										size_hint=self.size_down_icons))
		self.down_icons.add_widget(Image(source="./images/gear.png",
										size_hint=self.size_down_icons))

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
									font_size="18sp"))
		self.createHoliday()
		self.createThemeSwitch()
		
	def createHoliday(self):
		with self.body.canvas.before:
			Color(22/255, 23/255, 16/255, .49)
			RoundedRectangle(pos=(self.wind_size[0]*.04,self.wind_size[1]*.01), 
					size=(self.wind_size[0]-self.wind_size[0]*.08, self.wind_size[1]-self.wind_size[1]*.20))
		self.body_cap = BoxLayout(size_hint=(1,.15), orientation="vertical")
		self.body_text = BoxLayout(size_hint=(1,.3), orientation="vertical")
		self.body_image = BoxLayout(size_hint=(1,.6), 
									orientation="vertical",
									pos_hint={"top:":0.5, "center_x":0.5},
									padding=(self.wind_size[0]*.06,0,self.wind_size[0]*.06,0))
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
									valign="top", 
									font_size="18sp",
									text_size=(self.wind_size[0]*.9, self.wind_size[1]*.3),))
		self.img = Image(source="./images/imageTmp.png")
		self.body_image.add_widget(self.img)

	def createNextHoliday(self):
		pass

	def createThemeSwitch(self):
		with self.themeSwitch.canvas.before:
			Color(22/255, 23/255, 16/255, .49)
			RoundedRectangle(pos=(self.wind_size[0]*.04,self.wind_size[1]*.01), 
					size=(self.wind_size[0]-self.wind_size[0]*.08, self.wind_size[1]-self.wind_size[1]*.20))
		self.body_cap = BoxLayout(size_hint=(1,.04), orientation="vertical")
		self.body_cap2 = BoxLayout(size_hint=(1,.04), orientation="vertical")
		self.scrollTheme = ScrollView()
		self.bxScrollTheme = BoxLayout(orientation="vertical", 
										pos_hint={"center_x":0.5},
										size_hint=(1, 1.8),
										padding=(30, 6, 30, 6))
		self.butTheme = Button(size_hint=self.size_button,
								text="green",
								padding=(10,10),
								background_color=(0,2,0,.08),
								background_down="",
								background_normal="")
		self.butTheme2 = Button(size_hint=self.size_button)
		self.butTheme3 = Button(size_hint=self.size_button)
		self.butTheme4 = Button(size_hint=self.size_button)
		self.butTheme5 = Button(size_hint=self.size_button)
		self.butTheme6 = Button(size_hint=self.size_button)
		self.butTheme7 = Button(size_hint=self.size_button)
		self.butTheme8 = Button(size_hint=self.size_button)

		self.bxScrollTheme.add_widget(self.butTheme)
		self.bxScrollTheme.add_widget(BoxLayout(size_hint=(1, 0.001), orientation="vertical"))
		self.bxScrollTheme.add_widget(self.butTheme2)
		self.bxScrollTheme.add_widget(BoxLayout(size_hint=(1, 0.001), orientation="vertical"))
		self.bxScrollTheme.add_widget(self.butTheme3)
		self.bxScrollTheme.add_widget(BoxLayout(size_hint=(1, 0.001), orientation="vertical"))
		self.bxScrollTheme.add_widget(self.butTheme4)
		self.bxScrollTheme.add_widget(BoxLayout(size_hint=(1, 0.001), orientation="vertical"))
		self.bxScrollTheme.add_widget(self.butTheme5)
		self.bxScrollTheme.add_widget(BoxLayout(size_hint=(1, 0.001), orientation="vertical"))
		self.bxScrollTheme.add_widget(self.butTheme6)
		self.bxScrollTheme.add_widget(BoxLayout(size_hint=(1, 0.001), orientation="vertical"))
		self.bxScrollTheme.add_widget(self.butTheme7)
		self.bxScrollTheme.add_widget(BoxLayout(size_hint=(1, 0.001), orientation="vertical"))
		self.bxScrollTheme.add_widget(self.butTheme8)

		self.scrollTheme.add_widget(self.bxScrollTheme)

		self.themeSwitch.add_widget(self.body_cap)
		self.themeSwitch.add_widget(self.scrollTheme)
		self.themeSwitch.add_widget(self.body_cap2)
