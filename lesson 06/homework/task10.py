import turtle


# შექმნათ ფანჯარა
screen = turtle.Screen()
screen.bgcolor("white")  # ფონის ფერი

# შექმენით turtle ობიექტი
pen = turtle.Turtle()
pen.shape("turtle")  # მოცულობის ფორმა
pen.color("blue")    # მეხი ფერი
pen.speed(10)        # სიჩქარე

# ამოძრავებს turtle იმ მიმართულებით და დააკრავს ფორმას
def draw_circle(radius):
    for i in range(36):  # 360 გრადუსი დაყოფილია 10
        pen.circle(radius)  # ხატავს წრეს
        pen.right(10)  # 10 გრადუსით მარჯვნივ გადახვევა

# ვაწარმოებთ შემობრუნებას მრავალჯერ
for i in range(12):
    draw_circle(100)  # ხატავს წრეს 100 პიქსელის რადიუსით
    pen.right(30)  # 30 გრადუსით მარჯვნივ

# ნამუშევარი დასრულდა
pen.hideturtle()  # დამალავს turtle-ს

# შემოჩერდება ფანჯარაში
screen.mainloop()