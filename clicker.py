import time, random
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics.context_instructions import PushMatrix, PopMatrix
from kivy.graphics import Rectangle, Rotate, Color
from kivy.animation import Animation
#from kivy.graphics import Rotate

if __name__ == "__main__":
	exit()

class cnvClicker():
	def __init__(self, **kwargs):
		#window size
		self.wind = Window
		self.wind_size = (self.wind.width, self.wind.height)
		#button image size (banan)
		self.size = (int(self.wind_size[0]/8), int(self.wind_size[1]/12))
		#array ball
		self.arBall = []
		self.score = 0
		#main layout
		self.layout = FloatLayout()
		self.bananSound = SoundLoader.load("./sound/boule.wav")
							
		#3 button man
		for i in range(3):
			speed = ([self.randSign(random.randrange(30, 40)/10),
					self.randSign(random.randrange(30, 40)/10)])
			ballTmp = Ball()
			ballTmp.build(speed,
						self.size, 
						"./images/sanya.png", 
						self.wind_size, 
						self.funcClick)
			self.arBall.append(ballTmp)

			#add widget
			self.layout.add_widget(self.arBall[i])
			#physic ball
		#5 button banan
		for i in range(3, 10):
			speed = ([self.randSign(random.randrange(10, 20)/10),
					self.randSign(random.randrange(10, 20)/10)])
			ballTmp = Ball()
			ballTmp.build(speed,
						self.size, 
						"./images/banan.png", 
						self.wind_size, 
						self.funcClick)
			self.arBall.append(ballTmp)

			self.layout.add_widget(self.arBall[i])

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


class Ball(Button):
	def __init__(self, **kwargs):
		super(Ball, self).__init__(**kwargs)
		self.size_hint=(0.5,0.5)
		self.size=(100,100)
		self.angle = 5
		with self.canvas.before:
			PushMatrix()
			self.rot = Rotate()
			self.rot.angle = self.angle
			self.rot.origin = self.center
			self.rot.axis = (0,0,1)
		with self.canvas.after:
			PopMatrix()

	def rotation(self, what):
		self.rot.angle += self.angle
		self.rot.origin = self.center
		self.rot.axis = (0,0,1)

	def build(self, speed, sizes, path_img, wind_size, funcClick):
		self.speed = speed
		#funcution clicker call
		self.bind(on_press=funcClick)

		self.path_img = path_img
		#window size
		self.wind_size = wind_size
		self.size = sizes
		self.pos = (random.randrange(0, self.wind_size[0]-self.size[0]),
					random.randrange(self.size[1], self.wind_size[1]-self.size[1]))
		self.pos=(self.pos[0], self.pos[1])
		self.background_down=self.path_img
		self.background_normal=self.path_img
		self.size_hint=(.2, .2)
		self.anim = Animation(angle=random.randrange(12, 18), duration=random.randrange(4,9))
		self.anim += Animation(angle=-random.randrange(12, 18), duration=random.randrange(4,9))
		self.anim.repeat = True
		self.anim.start(self)
		Clock.schedule_interval(self.rotation, 0.05)
		Clock.schedule_interval(self.move, 0.05)

	#physics button
	def move(self, instance):
		if (self.pos[1] > self.wind_size[1]):
			self.speed[1] = -self.speed[1]
		elif (self.pos[1] <= 0 ):
			self.speed[1] = -self.speed[1]
		if (self.pos[0] >= self.wind_size[0]):
			self.speed[0] = -self.speed[0]
		elif (self.pos[0] <= 0- self.size[0]):
			self.speed[0] = -self.speed[0]
		self.pos = (self.pos[0]+self.speed[0], self.pos[1]+self.speed[1])
