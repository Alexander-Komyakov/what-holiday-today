import pickle, os, hashlib

if __name__ == "__main__":
	exit()

class saveProgress():
	def __init__(self):
		self.path_to_save = "save"
	def save(self, data):
		try:
			f = open('save', 'wb')
			pickle.dump(data, f)
			f.close()
		except:
			return 3
	def load(self):
		if (os.path.isfile(self.path_to_save)):
			try:
				f = open(self.path_to_save, 'rb')
				data = pickle.load(f)
				f.close()
				return data
			except:
				return 2
		return 1
	def getHash(self, path):
		if (os.path.isfile(path)):
			try:
				f = open(path, 'rb')
				data = f.read()
				f.close()
				return hashlib.md5(data).hexdigest()
			except:
				return 2
			return 1
	def saveImage(self, image, path):
		try:
			img_file = open(path, 'wb')
			img_file.write(image)
			img_file.close()
		except:
			pass

#1 - not loaded, file not found
#2 - not loaded, file not correct
#3 - permission denied or other error save
