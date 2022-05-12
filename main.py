import random, time, hashlib
import save, clicker, pars, screens
from kivy.app import App
from kivy.base import runTouchApp, stopTouchApp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.utils import platform
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

if platform == "android":
	from android.permissions import request_permissions, Permission
	request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
				

class MyApp(App):
	def build(self):
		self.wind = Window
		self.wind_width = self.wind.width
		self.wind_height = self.wind.height
		self.path_img = {"Holiday":"./images/imageTmp.png",
						"NextHoliday":"./images/imageTmp2.png"}
		self.textHoliday = {"Holiday":"",
							"NextHoliday":""}
		self.hash_img = {"Holiday":"error",
						"NextHoliday":"error"}
		self.theme = ""
		self.userTheme = {"color_background":(0,0,0), 
						"color_font":(0,0,0), 
						"color_font_label":(1,1,1), 
						"color_button":(1,1,1)}
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
		self.createScreenManager()
		return self.scman

	#function restart
	def setFuncRestart(self, fres):
		self.fres = fres

	#restart layout
	def restart(self, theme):
		self.theme = theme
		self.saveLayout()
		self.fres()
		#self.root.clear_widgets()
		#self.stop()
		#return MyApp().run()

	def createScreenManager(self):
		self.scman = ScreenManager()
		self.menu = screens.ScreenMenu(name="Menu")
		self.holiday = screens.ScreenHoliday(name="Holiday")
		self.nextHoliday = screens.ScreenHoliday(name="NextHoliday")
		self.settingsTheme = screens.ScreenSettingsTheme(name="settingsTheme")
		self.menu.build(self.goHoliday, self.goNextHoliday, 
						self.goClicker, self.restart, self.goSetTheme, self.userTheme, self.theme)
		self.holiday.build(self.goMenu, 
						self.getImagePath("Holiday"),
						self.textHoliday["Holiday"], self.userTheme, self.theme)
		self.nextHoliday.build(self.goMenu,
						self.getImagePath("NextHoliday"),
						self.textHoliday["NextHoliday"], self.userTheme, self.theme)
		self.settingsTheme.build(self.goMenuSaveTheme, self.userTheme, self.theme)
		self.settingsTheme.set_current_theme(self.menu.getCurrentTheme())
		#add cnv clicker
		self.cnvClicker = clicker.cnvClicker()
		self.cnvClicker.setScore(self.score)
		self.clickerLayout = self.cnvClicker.getLayout()

		self.clicker = screens.ScreenClicker(name="Clicker", 
							on_touch_up=self.getScoreLayout)
		self.clicker.build(self.goMenu, self.clickerLayout, self.userTheme, self.theme)
		self.getScoreLayout(0, 0)
		self.scman.add_widget(self.menu)
		self.scman.add_widget(self.settingsTheme)
		self.scman.add_widget(self.clicker)
		self.scman.add_widget(self.holiday)
		self.scman.add_widget(self.nextHoliday)

	def goClicker(self, instance):
		self.scman.current = "Clicker"
	def getScoreLayout(self, instance, what):
		self.score = self.cnvClicker.getScore()
		self.clicker.setScore(self.score)

	def goNextHoliday(self, instance):
		name = "NextHoliday"
		self.scman.current = "NextHoliday"
		self.parser = pars.parser()
		self.parser.requestData(name, self.resultGetData)
	def goHoliday(self, instance):
		name = "Holiday"
		self.scman.current = "Holiday"
		self.parser = pars.parser()
		self.parser.requestData(name, self.resultGetData)

	def goSetTheme(self, instance):
		self.saveLayout()
		self.scman.current = "settingsTheme"
	def goMenu(self, instance):
		self.saveLayout()
		self.scman.current = "Menu"
	def goMenuSaveTheme(self, instance):
		self.userTheme = self.settingsTheme.get_current_theme()
		self.theme = "user"
		self.goMenu("goMenuSaveTheme->.")
		self.fres()

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
				self.theme = saveResult[4]
				self.userTheme = saveResult[3]
				#image and text loaded
				self.textHoliday = saveResult[0].copy()
				for i in saveResult[1].keys():
					hash_img = self.svMain.getHash(self.path_img[i])
					if (saveResult[1][i] == hash_img):
						self.hash_img[i] = hash_img
	def setUserThemeLayout(self, instance):
		self.userTheme = instance.userTheme

	def saveLayout(self):
		self.svMain.save((self.textHoliday, 
					self.hash_img,
					self.score, 
					self.userTheme,
					self.theme,
					self.cipher))

	def resultGetData(self, text, image, name):
		#save image to file
		self.svMain.saveImage(image, self.path_img[name])
		#save hash image
		self.hash_img[name] = hashlib.md5(image).hexdigest()
		#update image and text label
		self.textHoliday[name] = text
		if (name == "Holiday"):
			self.holiday.setText(text)
			self.holiday.setImage(self.getImagePath(name))
		elif(name == "NextHoliday"):
			self.nextHoliday.setText(text)
			self.nextHoliday.setImage(self.getImagePath(name))
		self.saveLayout()

def restart():
	app.root.clear_widgets()
	#app.stop()
	app.run()

if __name__ == "__main__":
	app = MyApp()
	app.setFuncRestart(restart)
	app.run()
