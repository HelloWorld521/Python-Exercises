## 题目

来源： [优达学城--编程基础：python](https://cn.udacity.com/course/programming-foundations-with-python--ud036)  
内容：使用 turtle 画出你想象。  
效果演示：
![python_show2.png](http://upload-images.jianshu.io/upload_images/4988302-0f120380498707d1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![mindstorms.gif](http://upload-images.jianshu.io/upload_images/4988302-f7006a930912e436.gif?imageMogr2/auto-orient/strip)

## 我的解法
```python
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
```
```python
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
```
## 步骤
1. 获取画布`turtle.Screen()`，设置背景色
2. 获取画笔 `turtle.Turtle()`，设置画笔形状颜色速度等
3. 画出想要的图案

