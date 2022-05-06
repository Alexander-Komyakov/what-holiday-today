from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.colorpicker import ColorPicker

if __name__ == "__main__":
	exit()

class SettingsUI:
	def __init__(self):
		#self.color_background = (11/255,34/255,27/255)
		#self.color_font = (224/255, 213/255, 163/255)
		#self.color_font_label = (224/255, 213/255, 163/255)
		#self.color_button = (21/255, 62/255, 79/255)
		self.color_theme = [(0, 0, 0), (1, 1, 1), (21/255, 62/255, 79/255)]
		self.font_name = "./fontsTtf/Omni.ttf"
		self.font_size = 70
		self.path_img_button = "./images/button.png"
		self.wind = Window
#		self.wind.clearcolor = self.color_background
		self.wind_width = self.wind.width
		self.wind_height = self.wind.height

	def themeSwitch(self, theme):
		if (theme == "white"):
			self.color_background = (0, 0, 0)
			self.color_font = (0, 0, 0)
			self.color_font_label = (1, 1, 1)
			self.color_button = (1, 1, 1)
		elif (theme == "black"):
			self.color_background = (1, 1, 1)
			self.color_font = (1, 1, 1)
			self.color_font_label = (0, 0, 0)
			self.color_button = (0, 0, 0)
		elif (theme == "blue"):
			self.color_background = (11/255,34/255,27/255)
			self.color_font = (224/255, 213/255, 163/255)
			self.color_font_label = (224/255, 213/255, 163/255)
			self.color_button = (21/255, 62/255, 79/255)
		else:
			self.color_background = (11/255,34/255,27/255)
			self.color_font = (224/255, 213/255, 163/255)
			self.color_font_label = (224/255, 213/255, 163/255)
			self.color_button = (21/255, 62/255, 79/255)
		Window.clearcolor = self.color_background
	
class ScreenMenu(Screen, SettingsUI):
	def __init__(self, **kwargs):
		super(ScreenMenu, self).__init__(**kwargs)
		SettingsUI.__init__(self)
		self.SettingsUI = SettingsUI()

	def themeSwitchLayout(self, instance):
		self.SettingsUI.themeSwitch(instance.text)
		self.restart(instance.text)

	def build(self, holiday_press, 
				next_holiday_press, clicker_press, restart, goSetTheme, theme):
		self.restart = restart
		self.themeSwitch(theme)

		self.nameLabel = "Календарь счастливых\nлюдей"
		self.nameButtonHoliday = "Какой сегодня праздник?"
		self.nameButtonNextHoliday = "Какой завтра праздник?"
		self.nameSetTheme = "Настройка тем"
		self.nameClicker= "Бананы!"
		self.holiday_press = holiday_press
		self.next_holiday_press = next_holiday_press
		self.clicker_press = clicker_press

		self.bxMenu = BoxLayout(
							orientation="vertical",
							padding=[10, 10, 10, 10],
							spacing=10)
		self.add_widget(self.bxMenu)

		self.bxMenu.add_widget(Label(text=self.nameLabel,
								padding=[10, 10],
								size_hint=(1,1.1),
								font_name=self.font_name,
								color=self.color_font_label,
								halign="center",
								font_size=self.font_size))
		#theme button
		self.bxMenu.add_widget(Button(text="black",
			font_name=self.font_name,
			on_press=self.themeSwitchLayout,
			size_hint=(.1, .1),
			pos_hint={"right":1},
			color=self.color_font,
			background_normal=self.path_img_button,
			background_down=self.path_img_button,
			border=(30,30,30,30),
			background_color=self.color_theme[0]))
		self.bxMenu.add_widget(Button(text="white",
			font_name=self.font_name,
			on_press=self.themeSwitchLayout,
			size_hint=(.1, .1),
			pos_hint={"right":1},
			color=self.color_font,
			background_normal=self.path_img_button,
			background_down=self.path_img_button,
			border=(30,30,30,30),
			background_color=self.color_theme[1]))
		self.bxMenu.add_widget(Button(text="blue",
			font_name=self.font_name,
			on_press=self.themeSwitchLayout,
			size_hint=(.1, .1),
			pos_hint={"right":1},
			color=self.color_font,
			background_normal=self.path_img_button,
			background_down=self.path_img_button,
			border=(30,30,30,30),
			background_color=self.color_theme[2]))

		self.bxMenu.add_widget(Button(text=self.nameButtonHoliday,
			font_name=self.font_name,
			font_size=self.font_size,
			on_press=self.holiday_press,
			size_hint=(1, .25),
			color=self.color_font,
			background_normal=self.path_img_button,
			background_down=self.path_img_button,
			border=(55,55,55,55),
			background_color=self.color_button))
		self.bxMenu.add_widget(Button(text=self.nameButtonNextHoliday,
			font_name=self.font_name,
			font_size=self.font_size,
			on_press=next_holiday_press,
			size_hint=(1, .25),
			color=self.color_font,
			background_normal=self.path_img_button,
			background_down=self.path_img_button,
			border=(55,55,55,55),
			background_color=self.color_button))

		self.bxMenu.add_widget(Button(text=self.nameClicker,
			font_name=self.font_name,
			font_size=self.font_size,
			on_press=self.clicker_press,
			color=self.color_font,
			size_hint=(1, .25),
			background_normal=self.path_img_button,
			background_down=self.path_img_button,
			border=(55,55,55,55),
			background_color=self.color_button))

		self.bxMenu.add_widget(Button(text=self.nameSetTheme,
			font_name=self.font_name,
			font_size=self.font_size,
			on_press=goSetTheme,
			color=self.color_font,
			size_hint=(1, .25),
			background_normal=self.path_img_button,
			background_down=self.path_img_button,
			border=(55,55,55,55),
			background_color=self.color_button))


class ScreenHoliday(Screen, SettingsUI):
	def __init__(self, **kwargs):
		super(ScreenHoliday, self).__init__(**kwargs)
		SettingsUI.__init__(self)
		self.SettingsUI = SettingsUI()

	def build(self, menu_press, 
				path_img, text_holiday, theme):
		self.themeSwitch(theme)
		self.text_holiday = text_holiday
		self.menu_press = menu_press 
		self.path_img = path_img
		self.nameBack = "Назад"

		self.bxHoliday = BoxLayout(orientation="vertical",
							pos=(0,0),
							size_hint=(1, 1),
							padding=[5, 5, 5, 5],
							spacing=5)

		self.add_widget(self.bxHoliday)
		self.holidayLabel = Label(text=self.text_holiday,
								font_name=self.font_name,
								valign="center",
								font_size=self.font_size,
								color=self.color_font_label,
								text_size=(self.wind_width,None))
		self.bxHoliday.add_widget(self.holidayLabel)

		self.holidayImage = Image(source=self.path_img,
							pos_hint={"center_x":.5, "center_y":.5},
							size_hint=(.8, .6))

		self.bxHoliday.add_widget(self.holidayImage)
		self.bxHoliday.add_widget(Button(text=self.nameBack,
									font_name=self.font_name,
									font_size=self.font_size,
									on_press=self.menu_press,
									size_hint=(1, .20),
									color=self.color_font,
									background_normal=self.path_img_button,
									background_down=self.path_img_button,
									border=(55,55,55,55),
									background_color=self.color_button))
	def setText(self, text):
		self.text_holiday = text
		self.holidayLabel.text = self.text_holiday

	def setImage(self, path_image):
		self.path_image = path_image
		self.holidayImage.source = self.path_image
		self.holidayImage.reload()

class ScreenClicker(Screen, SettingsUI):
	def __init__(self, **kwargs):
		super(ScreenClicker, self).__init__(**kwargs)
		SettingsUI.__init__(self)
		self.SettingsUI = SettingsUI()

	def build(self, menu_press, clicker_image_layout, theme):
		self.themeSwitch(theme)
		self.menu_press = menu_press 
		self.clicker_image_layout = clicker_image_layout
		self.name_score = "Бананов: "
		self.name_go_menu = "Сохранить и выйти"

		self.bxClicker = FloatLayout(pos=(0,0))
		self.add_widget(self.bxClicker)

		self.bxClicker.add_widget(self.clicker_image_layout)
		self.btnScore =	Button(text=self.name_score, 
								font_name=self.font_name,
								font_size=self.font_size,
								size_hint=(1, .10),
								pos_hint={'x':0, 'y':0},
								color=self.color_font,
								background_normal=self.path_img_button,
								background_down=self.path_img_button,
								border=(55,55,55,55),
								background_color=self.color_button)
		self.bxClicker.add_widget(self.btnScore) 
		self.bxClicker.add_widget(Button(text=self.name_go_menu, 
										font_name=self.font_name,
										font_size=self.font_size,
										size_hint=(1, .10),
										pos_hint={'x':0, 'y':.11},
										on_press=self.menu_press,
										color=self.color_font,
										background_normal=self.path_img_button,
										background_down=self.path_img_button,
										border=(55,55,55,55),
										background_color=self.color_button))
	def setScore(self, score):
		self.btnScore.text = self.name_score+str(score)

class ScreenSettingsTheme(Screen, SettingsUI):
	def __init__(self, **kwargs):
		super(ScreenSettingsTheme, self).__init__(**kwargs)
		SettingsUI.__init__(self)
		self.SettingsUI = SettingsUI()

	def build(self, menu_press, 
				theme):
		self.themeSwitch(theme)
		self.menu_press = menu_press 
		self.nameBack = "Назад"
		self.nameSizeFont = "Цвет шрифта"
		self.nameColorButton = "Цвет кнопок"
		self.nameColorBackground = "Цвет фона"
		self.nameColorFont2 = "Цвет заголовка"
		self.nameLabel = "Настройка тем"
		self.font_size = self.font_size - 20

		self.bxMain = BoxLayout(orientation="vertical",
							pos=(0,0),
							size_hint=(1, 1),
							padding=[5, 5, 5, 5],
							spacing=5)

		self.add_widget(self.bxMain)

		self.bxMain.add_widget(Label(text=self.nameLabel,
								padding=[10, 10],
								size_hint=(1,.15),
								font_name=self.font_name,
								color=self.color_font_label,
								halign="center",
								font_size=self.font_size))

		self.cl_pick = ColorPicker()
		self.bxMain.add_widget(self.cl_pick)
		self.bxSetSwitch = BoxLayout(orientation="horizontal",
							size_hint=(1, .2),
							padding=[5, 5, 5, 5],
							spacing=5) 
		self.bxMain.add_widget(self.bxSetSwitch)


		self.bxMain.add_widget(Button(text=self.nameBack,
									font_name=self.font_name,
									font_size=self.font_size,
									on_press=self.menu_press,
									size_hint=(1, .20),
									color=self.color_font,
									background_normal=self.path_img_button,
									background_down=self.path_img_button,
									border=(55,55,55,55),
									background_color=self.color_button))
		self.bxSetSwitch.add_widget(Button(text=self.nameSizeFont,
									font_name=self.font_name,
									font_size=self.font_size,
									size_hint=(1, 1),
									color=self.color_font,
									background_normal=self.path_img_button,
									background_down=self.path_img_button,
									border=(55,55,55,55),
									background_color=self.color_button))
		self.bxSetSwitch.add_widget(Button(text=self.nameColorButton,
									font_name=self.font_name,
									font_size=self.font_size,
									size_hint=(1, 1),
									color=self.color_font,
									background_normal=self.path_img_button,
									background_down=self.path_img_button,
									border=(55,55,55,55),
									background_color=self.color_button))
		self.bxSetSwitch.add_widget(Button(text=self.nameColorFont2,
									font_name=self.font_name,
									font_size=self.font_size,
									size_hint=(1, 1),
									color=self.color_font,
									background_normal=self.path_img_button,
									background_down=self.path_img_button,
									border=(55,55,55,55),
									background_color=self.color_button))
		self.bxSetSwitch.add_widget(Button(text=self.nameColorBackground,
									font_name=self.font_name,
									font_size=self.font_size,
									size_hint=(1, 1),
									color=self.color_font,
									background_normal=self.path_img_button,
									background_down=self.path_img_button,
									border=(55,55,55,55),
									background_color=self.color_button))
