def class Thread():
	def __init__(self, producer, id_number, color_name=None):
		self.producer = producer	# "dmc"/other
		self.id_number = id_number
		self.RGB = (0, 0, 0)	# TODO: function/lookup here
		self.color_name = color_name
	
	
	
def class Recipe():
	def __init__(self, name, threads, pattern=None):
		self.name = name
		self.threads = threads
		amounts_pr_thread = {}
		self.pattern = pattern		# 2D-array of threads
		if pattern:
			self.shape = (len(pattern), len(pattern[0])
			amounts_pr_thread = {}
			for i in range(len(pattern)):
				for j in range(len(pattern[i])):
					thread_ij = pattern[i][j]
					if thread_ij in amounts_pr_thread:
						amounts_pr_thread[thread_ij] += 1
					else:
						amounts_pr_thread[thread_ij] = 1
			self.amounts_pr_thread = amounts_pr_thread
						
	
	def __str__(self):
		return str(self.name)
					  
					  
	def __len__(self):
		return len(self.threads)
	
	def __contains__(self,key):
		return key in threads

		

def class RecipeBook():
	def __init__(self, recipes, author, pages=None):
		self.author = author
		self.recipes = recipes
