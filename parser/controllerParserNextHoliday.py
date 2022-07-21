import sys
sys.path.append('./parser')
from parserCalendNext import ParserCalendNext

class ControllerParserNextHoliday():
	def __init__(self):
		self.parsers = (ParserCalendNext(), ParserCalendNext())
		#номер используемого парсера
		self.numberPars = 0
		#перебираем все парсеры конкретных сайтов
		for i in self.parsers:
			#задаем куда возвращаеть результат
			i.bindGetResult(self.responseParser)
	

	#установка метода вызываемого, если результат парсинга получен
	def bindGetTextImage(self, func):
		self.func = func

	def responseParser(self, result):
		cap = (("Этот текст заглушка в случае ошибки. Что тут писать", "слудующий день"), (b'ff', b'ff'))
		#если ошибка
		if (result == 1):
			#если это последний парсер
			if (self.numberPars >= len(self.parsers)):
				#возвращаем заглушку
				self.func(cap)
			else:
				#выбираем следующий парсер
				self.numberPars += 1
				#начинаем парсинг
				self.startPars
		else:
			self.func(text=result[0], image=result[1])

	def startPars(self):
		#вызываем начало парсинга в текущем используемом парсере
		self.parsers[self.numberPars].startPars()
