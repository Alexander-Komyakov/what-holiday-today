from gui import MainGui
from clicker import cnvClicker
from kivy.uix.image import Image

class ControllerGui():
	def __init__(self):
		self.mgui = MainGui()
		self.mgui.bindButtonTort(self.clickButtonFlutter)
		self.mgui.bindButtonTort2(self.clickButtonFlutter)
		self.mgui.bindButtonBanan(self.clickButtonFlutter)
		self.mgui.bindButtonGear(self.clickButtonFlutter)
		self.createClicker()

		self.mgui.bindButtonTheme(self.clickButtonTheme)
		self.mgui.setCurrentSlide(3)

	def getMainApp(self):
		return self.mgui.getMainApp()
	
	#установить текст
	def setTextHoliday(self, text):
		#проверки на валидность
		if (isinstance(text[0], str)):
			#установить текст view
			self.mgui.setTextHoliday(text)

	def setTextNextHoliday(self, text):
		#проверки на валидность
		if (isinstance(text[0], str)):
			#установить текст view
			self.mgui.setTextNextHoliday(text)

	def setImageHoliday(self, image):
		#проверки на валидность
		#установить изображение
		try:
			#проверяем работоспособность изображения
			textImage = Image(texture=image)
		except:
			return 0
		self.mgui.setImageHoliday(image)

	def setImageNextHoliday(self, image):
		#проверки на валидность
		try:
			textImage = Image(texture=image)
		except:
			return 0
		self.mgui.setImageNextHoliday(image)
	
	def clickButtonTheme(self, instance):
		#цвет кнопки задаем цвету темы
		self.mgui.setThemeColor(instance.background_color)

	#если нажата клавиша расположенная внизу
	def clickButtonFlutter(self, instance):
		#первая кнопка, переход на первый слайд
		self.mgui.setCurrentSlide(instance.index)

	def createClicker(self):
		self.clicker = cnvClicker()
		self.mgui.setLayoutClicker(self.clicker.getLayout())
