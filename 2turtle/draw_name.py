import turtle

#def draw_name():

def draw_h(pen):
	pen.down()
	pen.right(90)
	pen.forward(100)
	pen.backward(50)
	pen.left(90)
	pen.forward(50)
	pen.right(90)
	pen.forward(50)
	pen.backward(100)
	pen.left(90)

def draw_j(pen):
	pen.up()
	pen.forward(25)
	pen.down()
	pen.forward(50)
	pen.backward(25)
	pen.right(90)
	pen.forward(100)
	pen.right(90)
	pen.forward(25)
	pen.right(90)
	pen.forward(25)
	pen.right(90)

def draw_y(pen):
	x = pen.xcor()
	y = pen.ycor()
	pen.goto(x+25,y-50)
	pen.goto(x+50,y)
	pen.goto(x+25,y-50)
	pen.right(90)
	pen.forward(50)
	pen.left(90)

def draw_flower(pen):
	for i in range(0,36):
		for i in range(0,2):
			pen.forward(50)
			pen.right(60)
			pen.forward(50)
			pen.right(120)
		pen.right(10)
	pen.right(90)
	pen.forward(200)


def draw_art():
	pen = turtle.Turtle()
	pen.color("yellow")
	pen.shape("turtle")
	pen.speed(8)
	window = turtle.Screen()
	window.bgcolor("red")	
	draw_h(pen)
	pen.up()
	pen.forward(10)
	draw_j(pen)
	pen.up()
	pen.goto(170,0)
	pen.down()
	draw_y(pen)
	pen.up()
	pen.goto(-100,100)
	pen.down()
	draw_flower(pen)
	window.exitonclick()


draw_art()
