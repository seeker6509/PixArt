import turtle

turtle.color("Black")
turtle.fillcolor("White")
turtle.speed(10000)
PIXEL_SIZE = 30
x=-315
y=315


def reposition(x1,y1,headingV):
    turtle.penup()
    turtle.setpos(x1,y1)
    turtle.pendown()
    turtle.setheading(headingV)
# determining heading and positions
def square(colors1):
    turtle.fillcolor(colors1)
    turtle.begin_fill()
    for i in range(4):    
        turtle.forward(PIXEL_SIZE)
        turtle.left(90)
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)
# The pixel's color is drawn and filled using this function.

def pixel_Coloring(coloring):
    for inputColor in coloring:
        if (inputColor=="0"):
                square("black")
        elif (inputColor=="1"):
                square("white")
        elif (inputColor=="2"):
                square("red")
        elif (inputColor=="3"):
                square("yellow")
        elif (inputColor=="4"):
                square("orange")
        elif (inputColor=="5"):
                square("green")
        elif (inputColor=="6"):
                square("yellowgreen")
        elif (inputColor=="7"):
                square("sienna")
        elif (inputColor=="8"):
                square("tan")
        elif (inputColor=="9"):
                square("gray")
        elif (inputColor=="A"):
                square("darkgray")
        else:
            return False
def pixart():
        reposition(x,y,0)
        draw=input("Enter text file name: ")
        fp = open(draw, 'r')
        for line in fp:
                for i in line:
                        pixel_Coloring(i)
                reposition(x,turtle.ycor()-PIXEL_SIZE,0)

def main():
    pixart()
main()
turtle.exitonclick()
