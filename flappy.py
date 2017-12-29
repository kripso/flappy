import tkinter, random,time

class game():
	def __init__(self):
		self.canvasWidth = 400
		self.canvasHeight = 500
		self.canvas=tkinter.Canvas(height=self.canvasHeight,width=self.canvasWidth,bg='white')
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
			r=random.randrange(self.canvasHeight/2-55,self.canvasHeight/2+55, 10)
			#nove suradnice trubok xsove
			x=[x1,x2]
			#nove suradnice trubok ysove z hora
			y=[0,r]
			#nove suradnice trubok ysove z dola
			#V je vzdialenost medzi trubkami
			v=80
			y1=[self.canvasHeight+20,r+v]
			#trubky
			self.canvas.create_rectangle(x[0],y[0],x[1],y[1],fill='light green',tags='pipes')
			self.canvas.create_rectangle(x[0],y1[0],x[1],y1[1],fill='light green',tags='pipes')
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
		self.canvas.create_oval(10,self.canvasHeight/2-15,50,self.canvasHeight/2+15,fill='yellow',tags='bird')
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