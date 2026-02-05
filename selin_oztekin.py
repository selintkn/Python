import turtle
wd = turtle.Screen()
selin = turtle.Turtle()



def draw_bar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height)  # Draw up the left side
    t.right(90)
    t.forward(40)  # Width of bar, along the top
    t.right(90)
    t.forward(height)  # And down again!
    t.left(90)  # Put the turtle facing the way we found it.
    t.end_fill()
    t.penup()
    t.forward(10)    # Leave small gap after each bar
    t.pendown()

def draw_down(t,height):
    t.begin_fill()
    t.right(90)
    t.forward(height)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(height)
    t.right(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()




xs = [-48, 117, 200, -240, 160, 260, 220]
for v in xs:
    if v >= 200:
        selin.color("red","red")
        draw_bar(selin,v)
    elif v < 100:
        selin.color("green","green")
        draw_bar(selin, v)
    elif v>=100:
        selin.color("yellow","yellow")
        draw_bar(selin, v)
    elif v<0:
        selin.color("grey","grey")
        draw_down(selin,v)


wd.mainloop()
