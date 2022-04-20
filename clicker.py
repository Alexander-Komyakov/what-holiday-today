import time, random
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.clock import Clock

if __name__ == "__main__":
	exit()

class cnvClicker(Widget):
	def __init__(self, **kwargs):
		#window size
		self.wind = Window
		self.wind_size = (self.wind.width, self.wind.height)
		#button image size (banan)
		self.size = (int(self.wind_size[0]/6), int(self.wind_size[1]/10))
		#array ball
		self.arBall = []
		self.score = 0
		#main layout
		self.layout = FloatLayout()
		self.bananSound = SoundLoader.load("./sound/boule.wav")
							
		super(cnvClicker, self).__init__(**kwargs)
		#3 button man
		for i in range(3):
			speed = ([self.randSign(random.randrange(10, 20)/10),
					self.randSign(random.randrange(10, 20)/10)])
			self.arBall.append(Ball(speed, 
								self.size, 
								"sanya", 
								self.wind_size, 
								self.funcClick))

			#add widget
			self.layout.add_widget(self.arBall[i].btn)
			#physic ball
			Clock.schedule_interval(self.arBall[i].move, 0.0001)
		#5 button banan
		for i in range(3, 9):
			speed = ([self.randSign(random.randrange(10, 20)/10),
					self.randSign(random.randrange(10, 20)/10)])
			self.arBall.append(Ball(speed, 
								self.size, 
								"banan", 
								self.wind_size, 
								self.funcClick))
			self.layout.add_widget(self.arBall[i].btn)
			Clock.schedule_interval(self.arBall[i].move, 0.0001)

	def setScore(self, score):
		self.score = score

	def funcClick(self, instance):
		if (instance.background_normal[9:14] == "sanya"):
			self.score -= 10
			if self.score < 0:
				self.score = 0
		elif (instance.background_normal[9:14] == "banan"):
			self.score += 1
			self.bananSound.play()

	def getScore(self):
		return self.score
	def getLayout(self):
		return self.layout

	def randSign(self, numb):
		if (random.randrange(1, 3) == 1): return numb
		else: return -numb


class Ball():
	def __init__(self, speed, sizes, path_img, wind_size, funcClick):
		self.speed = speed
		#funcution clicker call
		self.funcClick = funcClick
		self.sizes = sizes
		#frame animation
		self.animCount = random.randrange(0, 18)
		self.img_name = path_img
		self.dir_img = "./images/" + path_img + "/"
		self.path_img = self.dir_img+self.img_name+str(self.animCount)+".png"
		#window size
		self.wind_size = wind_size
		#time animation
		self.time_save = time.time()
		self.integ = "0987654321"
		self.pos = (random.randrange(self.sizes[0], self.wind_size[0]-self.sizes[0]),
					random.randrange(self.sizes[1], self.wind_size[1]-self.sizes[1]))
		#main button
		self.btn = Button(pos=(self.pos[0], self.pos[1]),
							background_down=self.path_img,
							background_normal=self.path_img,
							size=self.sizes,
							on_press=self.funcClick,
							size_hint=(.2, .2))

	#physics button
	def move(self, instance):
		if (self.pos[1] > self.wind_size[1]):
			self.speed[1] = -self.speed[1]
		elif (self.pos[1] <= 0):
			self.speed[1] = -self.speed[1]
		if (self.pos[0] >= self.wind_size[0]):
			self.speed[0] = -self.speed[0]
		elif (self.pos[0] <= 0):
			self.speed[0] = -self.speed[0]
		self.pos = (self.pos[0]+self.speed[0], self.pos[1]+self.speed[1])
		self.btn.pos = self.pos
		#animation button
		self.anim()

	def getBall(self):
		return self.btn

	def anim(self):
		if (self.time_save + 0.04 < time.time()):
			self.animCount = self.animCount + 1
			if (self.animCount > 18):
				self.animCount = 1
			path = self.dir_img+self.img_name+str(self.animCount)+".png"
			self.btn.background_normal = path
			self.btn.background_down = path
			self.time_save = time.time()
