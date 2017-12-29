import tkinter, random,time

class game():
	def __init__(self):
		self.canvas=tkinter.Canvas(height=400,width=400,bg='white')
		self.canvas.pack()

		self.move=1
		self.pipes_to_win=10

		self.canvas.bind_all('<space>',self.bird_move)

		self.prekazka()
		self.bird()
		self.bird_fall()
		self.pipes_move()

		self.canvas.mainloop()

	def prekazka(self):
		#sirka trubok
		x1=200
		x2=280

		for i in range(self.pipes_to_win):
			#rozmedzie vysok
			r=random.randrange(110, 250, 20)
			#nove suradnice trubok xsove
			x=[x1,x2]
			#nove suradnice trubok ysove z hora
			y=[0,r]
			#nove suradnice trubok ysove z dola
			y1=[420,r+80]
			#trubky
			self.canvas.create_rectangle(x[0],y[0],x[1],y[1],tags='pipes')
			self.canvas.create_rectangle(x[0],y1[0],x[1],y1[1],tags='pipes')
			#o kolko sa posunu do strany
			x1+=180
			x2+=180
	#pohyb flappyho dohora
	def bird_move(self,event):
		self.canvas.move('bird',0,-20)
	#padanie flappyho
	def bird_fall(self):
		if self.move==1:
			self.canvas.move('bird',0,+4)
			self.canvas.after(80,self.bird_fall)
	#flappy
	def bird(self):
		self.canvas.create_oval(10,180,50,210,tags='bird')
	#pohyb trubiek
	def pipes_move(self):
		if self.move==1:
			
			self.canvas.move('pipes',-2,0)
			self.canvas.after(30,self.pipes_move )

			tagged_objects = self.canvas.find_withtag('pipes')
			overlapping_objects = self.canvas.find_overlapping(*self.canvas.coords('bird'))

			for item in overlapping_objects:
				if item in tagged_objects:
					self.move=0

		self.canvas.update()

game()