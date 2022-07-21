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

class MainGui():
	def __init__(self):
		#текст праздника
		self.textHoliday = ""

		#создаем окно
		self.wind = Window
		#self.wind.size = (480, 854)
		#сохраняем его размер
		self.wind_width = self.wind.width
		self.wind_height = self.wind.height
		self.wind_size = (self.wind_width, self.wind_height)

		#устанавливаем размер интерфейса
		#верх, тело, низ
		self.size_head = (1, 0.06)
		self.size_body = (1, 0.75)
		self.size_footer = (1, 0.1)
		#размер нижних иконок
		self.size_footer_icons = (.8, 1.1 - self.size_footer[1])
		self.size_icons_name = (self.size_footer_icons[0], 1 - self.size_footer_icons[1])
		#размер кнопок
		self.size_button = (1, .01)
		#создать весь интерфейс
		self.__createMainGui()
		#self.setCurrentSlide(1)
	def getMainApp(self):
		return self.scman

	def getTextHoliday(self):
		return self.textHoliday
	
	def setTextHoliday(self, textHoliday):
		self.textHoliday = textHoliday
		self.lblTextHoliday.text = self.textHoliday
	
	def getTextNextHoliday(self):
		return self.textNextHoliday

	def setTextNextHoliday(self, textNextHoliday):
		self.textNextHoliday = textNextHoliday
		self.lblTextNextHoliday.text = self.textNextHoliday

	def getImageHoliday(self):
		return self.img.texture

	def getImageNextHoliday(self):
		return self.imgNextHoliday.texture

	def setImageHoliday(self, texture):
		self.img.texture = texture

	def setImageNextHoliday(self, texture):
		self.imgNextHoliday.texture = texture
	
	def getCurrentSlide(self):
		return self.bodyCarousel.index
	
	def setCurrentSlide(self, slideNumber):
		self.bodyCarousel.index = slideNumber
	
	def bindButtonTort(self, func):
		self.tortButton.bind(on_press=func)

	def bindButtonTort2(self, func):
		self.tort2Button.bind(on_press=func)

	def bindButtonBanan(self, func):
		self.bananButton.bind(on_press=func)

	def bindButtonGear(self, func):
		self.gearButton.bind(on_press=func)

	def __createMainGui(self):
		self.scman = ScreenManager()

		#создаем экран меню
		self.screenBody = Screen(name="Menu")

		#фоновое изображение меню
		with self.screenBody.canvas.before:
			Rectangle(source="./images/background.png", 
						size=(self.wind_size[0], self.wind_size[1]))

		#добавляем меню в контроллер экранов
		self.scman.add_widget(self.screenBody)


		#тело экрана body
		#carousel - изменяемая часть экрана
		#внутри себя имеет виджеты и может их переключать
		self.bodyCarousel = Carousel(size_hint=self.size_body)

		self.bodyHoliday = BoxLayout(size_hint=self.size_body, orientation="vertical")
		self.bodyNextHoliday = BoxLayout(size_hint=self.size_body, orientation="vertical")
		#тело gui - центр
		#self.themeSwitch = BoxLayout(size_hint=(1,1), orientation="vertical")
		self.bodyCarousel.add_widget(self.bodyHoliday)
		self.bodyCarousel.add_widget(self.bodyNextHoliday)

		#добавляем виджеты в карусель
		#self.bodyCarousel.add_widget(self.themeSwitch)

		
		self.bxBody = BoxLayout(orientation="vertical")
		self.__createHead()
		self.__createFooter()
		self.__createHoliday()
		self.__createNextHoliday()
		#self.createThemeSwitch()

	def __createHead(self):
		#виджеты верха gui
		#неизменяемая часть
		self.head = BoxLayout(size_hint=self.size_head, orientation="vertical")
		#доавляем прозрачные прямоугольники в которых будет содержимое блоков
		with self.head.canvas.before:
			Color(22/255, 23/255, 16/255, .59)
			Rectangle(pos=(0,self.wind_size[1]-self.wind_size[1]*self.size_head[1]), 
					size=(self.wind_size[0], self.wind_size[1]*self.size_head[1]))
		#добавляем название в head
		self.head.add_widget(Label(text="Календарь счастливых людей", 
									color=(4/255, 4/255, 3/255), 
									halign="center", 
									font_size="18sp"))

		self.bxBody.add_widget(self.head)
		#добавляем на основной экран карусель
		self.bxBody.add_widget(self.bodyCarousel)
		#экран основного меню
		self.screenBody.add_widget(self.bxBody)

	def __createFooter(self):
		#виджеты верха и низа gui
		#неизменяемая часть
		self.footer = BoxLayout(size_hint=self.size_footer, orientation="vertical")
		#доавляем прозрачные прямоугольники в которых будет содержимое блоков
		with self.footer.canvas.before:
			Color(22/255, 23/255, 16/255, .59)
			Rectangle(pos=(0,0), 
					size=(self.wind_size[0], 
					self.wind_size[1]*self.size_footer[1]))
		#иконки footer-а
		self.footer_icons = BoxLayout(size_hint=(1, .4), padding=[0,10,0,-10])
		#место для названий иконок
		self.footer_icons_name = BoxLayout(size_hint=(1, .2))
		self.footer.add_widget(self.footer_icons)
		self.footer.add_widget(self.footer_icons_name)

		#добавляем кнопки внизу
		#cap - заглушка, для невидимости оригинального изображения кнопки
		self.tortButton = Button(size_hint=self.size_footer_icons,
								background_normal="./images/cap.png",
								background_down="./images/cap.png")
		#добавляем изображение внутри кнопки
		size_button = (self.wind_width/4, self.wind_height/13)
		self.tortButton.add_widget(Image(source="./images/tort.png",
										size = size_button,
										x = 0,
										y = size_button[1] * 0.3,
										allow_stretch=True))
		self.footer_icons.add_widget(self.tortButton)

		self.tort2Button = Button(size_hint=self.size_footer_icons,
								background_normal="./images/cap.png",
								background_down="./images/cap.png")
		self.tort2Button.add_widget(Image(source="./images/tort2.png",
										size=size_button,
										x = size_button[0],
										y = size_button[1] * 0.3,
										allow_stretch=True))
		self.footer_icons.add_widget(self.tort2Button)

		self.bananButton = Button(size_hint=self.size_footer_icons,
								background_normal="./images/cap.png",
								background_down="./images/cap.png")
		self.bananButton.add_widget(Image(source="./images/bananIcon.png",
										size=size_button,
										x = size_button[0]*2,
										y = size_button[1] * 0.3,
										allow_stretch=True))
		self.footer_icons.add_widget(self.bananButton)

		self.gearButton = Button(size_hint=self.size_footer_icons,
								background_normal="./images/cap.png",
								background_down="./images/cap.png")
		self.gearButton.add_widget(Image(source="./images/gear.png",
										size=size_button,
										x = size_button[0]*3,
										y = size_button[1] * 0.3,
										allow_stretch=True))
		self.footer_icons.add_widget(self.gearButton)
		self.tortButton.index = 0
		self.tort2Button.index = 1
		self.bananButton.index = 2
		self.gearButton.index = 3

		#добавляем подписи иконок
		self.footer_icons_name.add_widget(Label(text="Сегодня", 
											color=(4/255, 4/255, 3/255), 
											halign="center"))
		self.footer_icons_name.add_widget(Label(text="Завтра", 
											color=(4/255, 4/255, 3/255), 
											halign="center"))
		self.footer_icons_name.add_widget(Label(text="Кликер", 
											color=(4/255, 4/255, 3/255), 
											halign="center"))
		self.footer_icons_name.add_widget(Label(text="Темы", 
											color=(4/255, 4/255, 3/255), 
											halign="center"))

		self.bxBody.add_widget(self.footer)
		
	def __createHoliday(self):
		#доавляем прозрачный прямоугольник в котором будет содержимое блока
		with self.bodyHoliday.canvas.before:
			Color(22/255, 23/255, 16/255, .49)
			RoundedRectangle(pos=(self.wind_size[0]*.04,self.wind_size[1]*.01), 
					size=(self.wind_size[0]-self.wind_size[0]*.08, self.wind_size[1]-self.wind_size[1]*.20))
		#заглушки для разметки интерфейса
		self.body_cap = BoxLayout(size_hint=(1,.3), orientation="vertical")
		#создаем места для текста и изображения
		self.body_text = BoxLayout(size_hint=(1,.3), orientation="vertical")
		self.body_image = BoxLayout(size_hint=(1,.6), 
									orientation="vertical",
									pos_hint={"top:":0.5, "center_x":0.5},
									padding=(self.wind_size[0]*.06,0,self.wind_size[0]*.06,0))
		#заглушки для разметки интерфейса
		self.body_cap2 = BoxLayout(size_hint=(1,.15), orientation="vertical")

		#добавляем все что создали в тело
		self.bodyHoliday.add_widget(self.body_text)
		self.bodyHoliday.add_widget(self.body_cap)
		self.bodyHoliday.add_widget(self.body_image)
		self.bodyHoliday.add_widget(self.body_cap2)
		#добавляем виджет с текстом
		self.lblTextHoliday = Label(text=self.textHoliday,
									color=(4/255, 4/255, 3/255), 
									halign="center", 
									valign="top", 
									font_size="18sp",
									text_size=(self.wind_size[0]*.9, self.wind_size[1]*.3),)
		self.body_text.add_widget(self.lblTextHoliday)
		#загружаем изображение
		self.img = Image()
		#добавляем изображение
		self.body_image.add_widget(self.img)

	def __createNextHoliday(self):
		#доавляем прозрачный прямоугольник в котором будет содержимое блока
		with self.bodyNextHoliday.canvas.before:
			Color(22/255, 23/255, 16/255, .49)
			RoundedRectangle(pos=(self.wind_size[0]*.04,self.wind_size[1]*.01), 
					size=(self.wind_size[0]-self.wind_size[0]*.08, self.wind_size[1]-self.wind_size[1]*.20))
		#заглушки для разметки интерфейса
		self.bodyNextHoliday_cap = BoxLayout(size_hint=(1,.3), orientation="vertical")
		#создаем места для текста и изображения
		self.bodyNextHoliday_text = BoxLayout(size_hint=(1,.3), pos_hint={"top":"0"}, orientation="vertical")
		self.bodyNextHoliday_image = BoxLayout(size_hint=(1,.6), 
									orientation="vertical",
									pos_hint={"top:":0.5, "center_x":0.5},
									padding=(self.wind_size[0]*.06,0,self.wind_size[0]*.06,0))
		#заглушки для разметки интерфейса
		self.bodyNextHoliday_cap2 = BoxLayout(size_hint=(1,.15), orientation="vertical")

		#добавляем все что создали в тело
		self.bodyNextHoliday.add_widget(self.bodyNextHoliday_text)
		self.bodyNextHoliday.add_widget(self.bodyNextHoliday_cap)
		self.bodyNextHoliday.add_widget(self.bodyNextHoliday_image)
		self.bodyNextHoliday.add_widget(self.bodyNextHoliday_cap2)
		#добавляем виджет с текстом
		self.lblTextNextHoliday = Label(text=self.textHoliday,
									color=(4/255, 4/255, 3/255), 
									halign="center", 
									valign="top", 
									font_size="18sp",
									text_size=(self.wind_size[0]*.9, self.wind_size[1]*.3),)
		self.bodyNextHoliday_text.add_widget(self.lblTextNextHoliday)
		#загружаем изображение
		self.imgNextHoliday = Image()
		#добавляем изображение
		self.bodyNextHoliday_image.add_widget(self.imgNextHoliday)


	"""
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
	"""
