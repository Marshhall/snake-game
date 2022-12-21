from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ("Courier", 24, "normal")
RECORD_FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.highest_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=SCORE_FONT)
        self.goto(230, 270)
        self.write(f"Record: {self.highest_score}", move=False, align=ALIGNMENT, font=RECORD_FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highest_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
