from kivy.network.urlrequest import UrlRequest
import io
from kivy.core.image import Image as CoreImage

if __name__ == "main":
	exit()

#класс парсинга с сайта calend.ru 
class ParserCalend():
	def __init__(self):
		self.url = "https://www.calend.ru"
		self.timeout = 3

	#проверка работоспособности сайта
	#0 - работает; 1 - не работает
	def startPars(self):
		self.response = UrlRequest(self.url,
							on_success=self.parsing,
							on_redirect=self.parsError,
							on_failure=self.parsError,
							on_error=self.parsError, 
							timeout=self.timeout)
	#устанавливаем что вызывать по результату работы парсера
	def bindGetResult(self, func):
		#варианты результата
		#1 - ошибка, (text, texture) - успешный результат
		self.func = func

	#начинаем парсинг
	def parsing(self, response, *args):
		#получаем html код
		self.resultHtml = response.result
		#выбираем из этого текст
		self.resultText = self.getText(self.resultHtml)
		#запрашиваем изображение
		self.startGetImage(self.resultHtml)

	#получаем текст из полученной страницы
	def getText(self, htmlCode):
		resp_begin = htmlCode.find("<li class=\"one-two\">")
		resp_end = htmlCode.find("<div class=\"caption\">")
		htmlCode = htmlCode[resp_begin:resp_end]
		text = htmlCode[htmlCode.find("alt=")+5:htmlCode.find("\' />")]
		return text
	
	#получаем ссылку на изображение
	#запрашиваем изображение
	def startGetImage(self, htmlCode):
		resp_begin = htmlCode.find("<li class=\"one-two\">")
		resp_end = htmlCode.find("<div class=\"caption\">")
		htmlCode = htmlCode[resp_begin:resp_end]
		urlImage = htmlCode[htmlCode.find("url('")+5:htmlCode.find("')")]
		self.Img = UrlRequest(urlImage, on_success=self.saveImage,
										on_redirect=self.parsError,
										on_failure=self.parsError,
										on_error=self.parsError, 
										timeout=self.timeout)
	
	def saveImage(self, response, *args):
		data = io.BytesIO(response.result)
		self.image = CoreImage(data, ext="png")
		#ВЫХОД УДАЧНЫЙ
		self.func((self.resultText, self.image.texture))

	#ошибка во время парсинга
	def parsError(self, req, *args):
		self.result = 1
		#ВЫХОД НЕУДЧАНЫЙ
		self.func(self.result)
