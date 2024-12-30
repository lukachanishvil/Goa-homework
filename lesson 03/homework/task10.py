import turtle

# კუს (turtle) ობიექტის შექმნა
screen = turtle.Screen()
screen.bgcolor("skyblue")  # ფონური ფერი ცისფერია

# კუს შექმნა
t = turtle.Turtle()
t.speed(5)

# მთა
def draw_mountains():
    t.penup()
    t.goto(-300, -50)
    t.pendown()
    t.color("gray")
    t.begin_fill()
    t.setheading(60)
    for _ in range(3):
        t.forward(200)
        t.right(120)
    t.end_fill()

# სახლი
def draw_house():
    t.penup()
    t.goto(-100, -150)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for _ in range(4):
        t.forward(200)
        t.left(90)
    t.end_fill()

    # სახლის სახურავი
    t.color("red")
    t.begin_fill()
    t.setheading(45)
    for _ in range(2):
        t.forward(140)
        t.right(90)
    t.end_fill()

    # ფანჯარა
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    t.color("lightblue")
    t.begin_fill()
    for _ in range(4):
        t.forward(40)
        t.left(90)
    t.end_fill()

# გზა
def draw_road():
    t.penup()
    t.goto(-400, -150)
    t.pendown()
    t.color("gray")
    t.begin_fill()
    t.setheading(0)
    t.forward(800)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(800)
    t.right(90)
    t.forward(100)
    t.end_fill()

# მდინარე
def draw_river():
    t.penup()
    t.goto(-400, -250)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    t.setheading(0)
    t.forward(800)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(800)
    t.right(90)
    t.forward(50)
    t.end_fill()

# ხეები
def draw_tree(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for _ in range(4):
        t.forward(20)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(x - 20, y + 20)
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

# მზე
def draw_sun():
    t.penup()
    t.goto(200, 200)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

# ყველაფერი رسمი
draw_mountains()
draw_house()
draw_road()
draw_river()
draw_tree(-200, -100)
draw_tree(100, -100)
draw_sun()

# ეკრანის დარჩენა ღია
t.hideturtle()
turtle.done()
