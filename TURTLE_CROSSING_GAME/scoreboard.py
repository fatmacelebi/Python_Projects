from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-230, 260)
        self.hideturtle()
        self.score = 0
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over_print(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
