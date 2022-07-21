from gui import MainGui

class ControllerGui():
	def __init__(self):
		self.mgui = MainGui()
		self.mgui.bindButtonTort(self.clickButtonFlutter)
		self.mgui.bindButtonTort2(self.clickButtonFlutter)
		self.mgui.bindButtonBanan(self.clickButtonFlutter)
		self.mgui.bindButtonGear(self.clickButtonFlutter)

	def getMainApp(self):
		return self.mgui.getMainApp()
	
	#установить текст и изображение
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
		if (True):
			#установить текст view
			self.mgui.setImageHoliday(image)

	def setImageNextHoliday(self, image):
		#проверки на валидность
		if (True):
			#установить текст view
			self.mgui.setImageNextHoliday(image)

	#если нажата клавиша расположенная внизу
	def clickButtonFlutter(self, instance):
		#первая кнопка, переход на первый слайд
		self.mgui.setCurrentSlide(instance.index)
