import random, time, hashlib
import save, clicker, pars
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import (Canvas, Ellipse, Color, Rectangle, Translate, Rotate, PushMatrix, PopMatrix)
from kivy.clock import Clock
#from kivy.core.image import Image
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.utils import platform
from kivy.loader import Loader
from kivy.lang import Builder

if platform == "android":
	from android.permissions import request_permissions, Permission
	request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
				

class MyApp(App):
	def build(self):
		self.wind = Window
		self.wind_width = self.wind.width
		self.wind_height = self.wind.height
		self.path_img = {"toDHoliday":"./images/imageTmp.png",
						"nextDHoliday":"./images/imageTmp2.png"}
		self.color_button = [46, 46, 46, 1]
		self.color_font = [0, 0, 0, 1]
		self.f_name = "./fontsTtf/Omni.ttf"
		self.f_size = 70
		self.createMenu()

		self.textHoliday = {"toDHoliday":"",
							"nextDHoliday":""}
		self.hash_img = {"toDHoliday":"error",
						"nextDHoliday":"error"}
		self.score = 0
		#value check file 'save'
		self.cipher = "abstraction"
		self.svMain = save.saveProgress()
		self.loadingSaveFile()
		self.parser = []
		#pre loading text and image
		j = 0
		for i in self.path_img.keys():
			self.parser.append(pars.parser())
			self.parser[j].requestData(i, self.resultGetData)
			j += 1
		return self.flArea
	def createMenu(self):
		self.bxAreaMenu = BoxLayout(size=(300, 300),
							orientation="vertical",
							padding=[10, 10, 10, 10],
							spacing=10)
		self.flArea = FloatLayout()
		self.flArea.add_widget(self.bxAreaMenu)
		self.bxAreaMenu.add_widget(Label(text="Бесконечность не предел", 
								padding=[10, 10],
								font_name=self.f_name,
								font_size=self.f_size))
		self.bxAreaMenu.add_widget(Button(text="Какой сегодня праздник?", 
			font_name=self.f_name,
			font_size=self.f_size,
			on_press=self.goDescription,
			background_color=self.color_button,
			size_hint=(1, .25),
			color=self.color_font))
		self.bxAreaMenu.add_widget(Button(text="Какой завтра праздник?", 
			font_name=self.f_name,
			font_size=self.f_size,
			on_press=self.goDescription,
			background_color=self.color_button,
			size_hint=(1, .25),
			color=self.color_font))


		self.bxAreaMenu.add_widget(Button(text="БАНАНЫ!!!", 
			font_name=self.f_name,
			font_size=self.f_size,
			on_press=self.goClicker,
			color=self.color_font,
			size_hint=(1, .25),
			background_color=self.color_button))

	def goClicker(self, instance):
		self.bxAreaMenu.pos = (0, 9999)

		self.bxAreaDish = FloatLayout(pos=(0,0))
		self.flArea.add_widget(self.bxAreaDish)
		#add cnv clicker
		self.cnvClicker = clicker.cnvClicker()
		self.cnvClicker.setScore(self.score)
		self.bxAreaDish.add_widget(self.cnvClicker.getLayout())
		self.bxAreaDish.add_widget(Button(text="Бананов: "+str(self.score), 
										font_name=self.f_name,
										font_size=self.f_size,
										on_touch_down=self.getScoreLayout,
										background_color=self.color_button,
										size_hint=(1, .10),
										pos=(0,0),
										color=self.color_font))
		self.bxAreaDish.add_widget(Button(text="Сохранить и выйти", 
										font_name=self.f_name,
										font_size=self.f_size,
										size_hint=(1, .10),
										pos=(0,self.wind_height/10),
										on_press=self.goMenu,
										background_color=self.color_button,
										color=self.color_font))

	def getScoreLayout(self, instance, what):
		self.score = self.cnvClicker.getScore()
		instance.text = "Бананов: " + str(self.cnvClicker.getScore())

	def goDescription(self, instance):
		self.bxAreaMenu.pos = (0, 9999)
		if (instance.text == "Какой сегодня праздник?"):
			name = "toDHoliday"
		if (instance.text == "Какой завтра праздник?"):
			name = "nextDHoliday"
		self.bxAreaDish = BoxLayout(orientation="vertical",
							size_hint=(1, 1),
							padding=[5, 5, 5, 5],
							spacing=5)
		self.flArea.add_widget(self.bxAreaDish)

		self.DescriptionLabel = Label(text=self.textHoliday[name], 
								font_name=self.f_name,
								font_size=self.f_size,
								text_size=(self.wind_width, None))
		self.bxAreaDish.add_widget(self.DescriptionLabel)

		self.butNews = Image(source=self.getImagePath(name),
							pos_hint={"center_x":.5, "center_y":.5},
							size_hint=(.8, .6))
		#reload image
		self.butNews.reload()

		self.parser = pars.parser()
		self.parser.requestData(name, self.resultGetData)
		self.bxAreaDish.add_widget(self.butNews)
		self.bxAreaDish.add_widget(Button(text="Назад", 
									font_name=self.f_name,
									font_size=self.f_size,
									on_press=self.goMenu,
									background_color=self.color_button,
									size_hint=(1, .20),
									color=self.color_font,
									pos=(100, 100)))
		self.bxAreaDish.pos = (0, 0)

	def goMenu(self, instance):
		self.saveLayout()
		self.bxAreaMenu.pos = (0, 0)
		self.flArea.remove_widget(self.bxAreaDish)

	def updateHolidayImgTxt(self, name):
		try:
			#update image and text label
			self.butNews.source = self.path_img[name]
			self.butNews.reload()
			self.DescriptionLabel.text = self.textHoliday[name]
		except:
			pass
	def getImagePath(self, name):
		#if image correct
		if (self.svMain.getHash(self.path_img[name]) == self.hash_img[name]):
			return self.path_img[name]
		return ""

	def loadingSaveFile(self):
		#loaded
		saveResult = self.svMain.load()	
		if (not(saveResult in (1,2))):
			#loaded and correct
			if (saveResult[-1] == self.cipher):
				self.score = saveResult[2]
				#image and text loaded
				self.textHoliday = saveResult[0].copy()
				for i in saveResult[1].keys():
					hash_img = self.svMain.getHash(self.path_img[i])
					if (saveResult[1][i] == hash_img):
						self.hash_img[i] = hash_img
	def saveLayout(self):
		self.svMain.save((self.textHoliday, 
					self.hash_img,
					self.score, 
					self.cipher))

	def resultGetData(self, text, image, name):
		#save image to file
		self.svMain.saveImage(image, self.path_img[name])
		#save hash image
		self.hash_img[name] = hashlib.md5(image).hexdigest()
		#update image and text label
		self.textHoliday[name] = text
		self.updateHolidayImgTxt(name)
		self.saveLayout()


if __name__ == "__main__":
	MyApp().run()
