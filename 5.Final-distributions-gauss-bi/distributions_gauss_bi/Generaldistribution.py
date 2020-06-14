class Distribution:
	
	def __init__(self, mu=0, sigma=1):
		self.mean = mu
		self.stdev = sigma
		self.data = []


	def read_data_file(self, file_name):		
		with open(file_name) as file:
			data_list = []
			line = file.readline()
			while line:
				data_list.append(int(line))
				line = file.readline()
		file.close()
	
		self.data = data_list