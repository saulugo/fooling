import turtle
import random

def do_art():
	window = turtle.Screen()
	window.bgcolor("black")
	
	brad = turtle.Turtle()
	brad.shape("turtle")
	n = 1
	x_pos = random.randint(-200,200)
	y_pos = random.randint(-200,200)
	brad.goto(x_pos,y_pos)
	colors = ['blue','red','yellow','white','pink','green','brown']
	while n==1:
		brad.speed(random.randint(5,1000))
		brad.color(colors[random.randint(1,7)-1])
		inc_ang = random.randint(1,360)
		l = 360/inc_ang
		l = int(l)
		for i in range(0,l):
			brad.left(inc_ang)
			for i in range(0,4):
				brad.forward(100)
				brad.right(90)
		x_pos = random.randint(-200,200)
		y_pos = random.randint(-200,200)
		brad.goto(x_pos,y_pos)
	
	window.exitonclick()
	
do_art()