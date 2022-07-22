import sys
sys.path.append('./parser')
from parserCalend import ParserCalend

class ControllerParserHoliday():
	def __init__(self):
		self.parsers = (ParserCalend(), ParserCalend())
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
		cap = ("За нашу историю произошло несчетное количество знаменательных событый. Каждый день праздник.", b'ff')
		#если ошибка
		if (result == 1):
			#если это последний парсер
			if (self.numberPars == len(self.parsers)-1):
				#возвращаем заглушку
				self.func(cap[0], cap[1])
			else:
				#выбираем следующий парсер
				self.numberPars += 1
				#начинаем парсинг
				self.startPars()
		else:
			self.func(text=result[0], image=result[1])

	def startPars(self):
		#вызываем начало парсинга в текущем используемом парсере
		self.parsers[self.numberPars].startPars()
