# Draw class for NAO 
# Allow draw hangman
# Author ImoucheG
class DrawHangman :
	# max_components : Limit of errors
	def __init__(self,max_components=10) :
		self.max_components = max_components
		self.current_component = 0
	# Draw a component of Hangman
	# iteration : int The number of iteration of errors 	
	def drawn_hangman(self,iteration) :
			if iteration == 1 :
				print(self.drawn_socle())
				self.increase_iteration_component()
			elif iteration == 2 :
				print(self.drawn_timber())
			elif iteration == 3 :
				print(self.drawn_support())
			elif iteration == 4 :
				print(self.drawn_rope_support())
			elif iteration == 5 :
				print(self.drawn_head())
			elif iteration == 6 :
				print(self.drawn_body())
			elif iteration == 7 :
				print(self.drawn_left_hand())
			elif iteration == 8 :
				print(self.drawn_right_hand())
			elif iteration == 9 :
				print(self.drawn_left_foot())
			elif iteration == 10 :
				print(self.drawn_right_foot())
			elif iteration >= self.max_components :
				return False
			self.increase_iteration_component()
			return True
	# Draw a socle
	def drawn_socle(self) :
		return "Drawn socle"
	# Draw a timber
	def drawn_timber(self) :
		return "Drawn timber"
	#Draw a support
	def drawn_support(self) :
		return "Drawn support"
	#Draw a rope support
	def drawn_rope_support(self) :
		return "Drawn rope support"
	# Draw head of man
	def drawn_head(self) :
		return "Drawn head"
	# Draw body of man
	def drawn_body(self) :
		return "Drawn body"
	# Draw left hand of man
	def drawn_left_hand(self) :
		return "Drawn left hand"
	# Draw right hand of man 
	def drawn_right_hand(self) :
		return "Drawn right hand"
	# Draw left foot of man
	def drawn_left_foot(self) :
		return "Drawn left foot"
	# Draw right foot of man
	def drawn_right_foot(self) :
		return "Drawn right foot"
	# Increase iteration of errors
	def increase_iteration_component(self) :
		self.current_component += 1