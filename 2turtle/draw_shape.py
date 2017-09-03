import turtle

def draw_circle(angie):	
	angie.circle(50)

def draw_triangle(triangle):
	for y in range(0,3):
		triangle.forward(100)
		triangle.right(120)


def draw_square(turtle):
	for i in range(0,4):
		turtle.forward(100)
		turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.speed(15)

	# 循环方形
	for i in range(0,36):
		brad.color("pink")
		draw_triangle(brad)
		brad.color("blue")
		draw_circle(brad)
		brad.color("yellow")
		draw_square(brad)	
		brad.right(10)
	brad.right(90)
	brad.forward(200)

	window.exitonclick()

# 方形画圆
draw_art()
# 添加音乐