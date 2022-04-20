import requests
from kivy.network.urlrequest import UrlRequest


if __name__ == "main":
	exit()

class parser():
	def requestData(self, nameReq, funcReturnData):
		self.nameReq = nameReq
		self.timeout = 60
		self.funcReturnData = funcReturnData
		print("GET REQUEST: ", nameReq)
		if (nameReq == "toDHoliday"):
			url = "https://www.calend.ru"
			self.response = UrlRequest(url, on_success=self.requestsGet, timeout=self.timeout)
		if (nameReq == "nextDHoliday"):
			url = "https://www.calend.ru"
			self.response = UrlRequest(url, on_success=self.requestsGet, timeout=self.timeout)


	def requestsGet(self, req, *args):
		self.resp_t = req.result
		self.text = self.getTextWSite(self.nameReq, self.resp_t)
		self.getImageWSite(self.nameReq, self.resp_t)
		#continue later download image
		#def ifImageDownload

	def getTextWSite(self, name, hcode):
		if (name == "toDHoliday"):
			resp_begin = hcode.find("<li class=\"one-two\">")
			resp_end = hcode.find("<div class=\"caption\">")
			hcode = hcode[resp_begin:resp_end]
			text_image = hcode[hcode.find("alt=")+5:hcode.find("\' />")]
			return text_image
		if (name == "nextDHoliday"):
			resp_begin = hcode.rfind("<li class=\"one-two\">")
			resp_end = hcode.rfind("<div class=\"caption\">")
			hcode = hcode[resp_begin:resp_end]
			text_image = hcode[hcode.find("alt=")+5:hcode.find("\' />")]
			return text_image
	def getImageWSite(self, name, hcode):
		if (name == "toDHoliday"):
			resp_begin = hcode.find("<li class=\"one-two\">")
			resp_end = hcode.find("<div class=\"caption\">")
			hcode = hcode[resp_begin:resp_end]
			urlImage = hcode[hcode.find("url('")+5:hcode.find("')")]
			self.calendImg = UrlRequest(urlImage, on_success=self.ifImageDownload, timeout=self.timeout)
		if (name == "nextDHoliday"):
			resp_begin = hcode.rfind("<li class=\"one-two\">")
			resp_end = hcode.rfind("<div class=\"caption\">")
			hcode = hcode[resp_begin:resp_end]
			urlImage = hcode[hcode.find("url('")+5:hcode.find("')")]
			self.calendImg = UrlRequest(urlImage, on_success=self.ifImageDownload, timeout=self.timeout)

	def ifImageDownload(self, req, *args):
		print("REQUEST: ", self.nameReq, " READY")
		self.funcReturnData(self.text, req.result, self.nameReq)
