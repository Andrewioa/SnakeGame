from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


# create the scoreboard that updates when ever the snake eats.
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.save_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def save_score(self):
        try:
            with open("high_score.txt", 'r') as hs:
                score = hs.read()
                return int(score)
        except FileNotFoundError:
            with open("high_score.txt", 'w') as hs:
                hs.write("0")
                return 0

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score {self.high_score}", align=ALIGNMENT, font=FONT)
        with open("high_score.txt", 'w') as hss:
            hss.write(f"{self.high_score}")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def change_score(self):  # change the score
        self.score += 1
        self.update_scoreboard()
