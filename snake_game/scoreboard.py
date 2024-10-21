from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")




class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as score_data:
            saved_score = score_data.read()
        self.score = 0
        self.high_score = saved_score
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High_Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):

        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as new_score:
                new_score.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


