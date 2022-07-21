import sys
sys.path.append('./parser')
from controllergui import ControllerGui
from controllerParserHoliday import ControllerParserHoliday
from controllerParserNextHoliday import ControllerParserNextHoliday
from kivy.app import App
from threading import Thread


class MyApp(App):
	def build(self):
		#controller gui
		self.contrGui = ControllerGui()
		#создаем контроллер парсера сегодняшнего праздника
		self.contrParsHoliday = ControllerParserHoliday()
		#указываем, что вызываеть для получения результата
		self.contrParsHoliday.bindGetTextImage(self.getResultParserHoliday)

		self.contrParsNextHoliday = ControllerParserNextHoliday()
		self.contrParsNextHoliday.bindGetTextImage(self.getResultParserNextHoliday)

		#начинаем парсинг
		self.contrParsHoliday.startPars()
		self.contrParsNextHoliday.startPars()
		return self.contrGui.getMainApp()
	
	def getResultParserHoliday(self, text="", image=b'ff'):
		self.contrGui.setTextHoliday(text)
		self.contrGui.setImageHoliday(image)

	def getResultParserNextHoliday(self, text="", image=b'ff'):
		self.contrGui.setTextNextHoliday(text)
		self.contrGui.setImageNextHoliday(image)

if __name__ == "__main__":
	app = MyApp()
	app.run()
