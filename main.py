import flet
import flet.canvas as cv

class BadmintonGame(flet.Container):

    def update_game_score(self):
        player1_score = 0
        player2_score = 0
        if self.sets[0].winner == 1:
            player1_score += 1
        elif self.sets[0].winner == 2:
            player2_score += 1

        if self.sets[1].winner == 1:
            player1_score += 1
        elif self.sets[1].winner == 2:
            player2_score += 1

        if self.sets[2].winner == 1:
            player1_score += 1
        elif self.sets[2].winner == 2:
            player2_score += 1

        self.player1_score_text.value = str(player1_score)
        self.player2_score_text.value = str(player2_score)

        self.player1_score_text.update()
        self.player2_score_text.update()

    def __init__(self, player1_name, player2_name):
        super().__init__()

        self.player1_score_text = flet.Text(str(0), size=50)
        self.player2_score_text = flet.Text(str(0), size=50)

        self.sets = [
            BadmintonSet(player1_name, player2_name, 21, self),
            BadmintonSet(player1_name, player2_name, 21, self),
            BadmintonSet(player1_name, player2_name, 11, self)
        ]

        self.content = flet.Column(
            controls=[
                flet.Row(
                    alignment=flet.MainAxisAlignment.CENTER,
                    controls=[
                        self.player1_score_text,
                        flet.Text("-", size=50),
                        self.player2_score_text
                    ]
                ),
                flet.Column(
                    controls=self.sets
                )
            ]
        )

class BadmintonSet(flet.Container):

    def player1_increase_score(self, e):
        if self.winner != 0:
            return

        self.player1_score += 1

        if ((self.player1_score >= self.max_score and self.player1_score - self.player2_score >= 2)
                or self.player1_score >= 30):
            self.winner = 1
        else:
            if self.player1_score % 2 == 0:
                self.serve_state = "player1_even"
            else:
                self.serve_state = "player1_odd"

            self.update_serve_graphics()

        # ändra texten så den stämmer med variabeln
        self.player1_score_text.value = str(self.player1_score)

        # säg till Flet att en uppdatering har
        # skett så att den visas
        self.player1_score_text.update()

        self.game.update_game_score()
        pass
    def player1_decrease_score(self, e):
        if self.winner == 1:
            self.winner = 0

        # ändra variabelvärdet
        if self.player1_score > 0:
            self.player1_score -= 1

        # ändra texten så den stämmer med variabeln
        self.player1_score_text.value = str(self.player1_score)

        # säg till Flet att en uppdatering har
        # skett så att den visas
        self.player1_score_text.update()

        self.game.update_game_score()
        pass
    def player2_increase_score(self, e):
        if self.winner != 0:
            return

        self.player2_score += 1

        if ((self.player2_score >= self.max_score and self.player2_score - self.player1_score >= 2)
                or self.player2_score >= 30):
            self.winner = 2
        else:
            if self.player2_score % 2 == 0:
                self.serve_state = "player2_even"
            else:
                self.serve_state = "player2_odd"

            self.update_serve_graphics()

        # ändra texten så den stämmer med variabeln
        self.player2_score_text.value = str(self.player2_score)

        # säg till Flet att en uppdatering har
        # skett så att den visas
        self.player2_score_text.update()

        self.game.update_game_score()
        pass
    def player2_decrease_score(self, e):
        if self.winner == 2:
            self.winner = 0

        # ändra variabelvärdet
        if self.player2_score > 0:
            self.player2_score -= 1

        # ändra texten så den stämmer med variabeln
        self.player2_score_text.value = str(self.player2_score)

        # säg till Flet att en uppdatering har
        # skett så att den visas
        self.player2_score_text.update()

        self.game.update_game_score()
        pass

    def update_serve_graphics(self):
        if self.serve_state == "player1_even":
            self.serve_origin.x = 37.5
            self.serve_origin.y = 70
            self.serve_target.x = 112.5
            self.serve_target.y = 30
        elif self.serve_state == "player1_odd":
            self.serve_origin.x = 37.5
            self.serve_origin.y = 30
            self.serve_target.x = 112.5
            self.serve_target.y = 70
        elif self.serve_state == "player2_even":
            self.serve_target.x = 37.5
            self.serve_target.y = 70
            self.serve_origin.x = 112.5
            self.serve_origin.y = 30
        elif self.serve_state == "player2_odd":
            self.serve_target.x = 37.5
            self.serve_target.y = 30
            self.serve_origin.x = 112.5
            self.serve_origin.y = 70

        self.serve_origin.update()
        self.serve_target.update()

    def __init__(self, player1_name, player2_name, max_score, game):
        super().__init__()

        self.bgcolor = "#ffdddd"
        self.gradient = flet.LinearGradient(
            begin=flet.alignment.top_left,
            end=flet.alignment.bottom_right,
            colors=["#ff0000", "#ffff00", "#00ffff"]
        )

        self.max_score = max_score

        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

        self.player1_score_text = flet.Text(str(self.player1_score), size=30)
        self.player2_score_text = flet.Text(str(self.player2_score), size=30)

        self.serve_state = ""

        self.serve_origin = cv.Circle(112.5, 30, 10,
                                 paint=flet.Paint("red"))

        self.serve_target = cv.Circle(37.5, 70, 10,
                                 paint=flet.Paint("red", stroke_width=3,
                                                  style=flet.PaintingStyle.STROKE))

        self.winner = 0

        self.game = game

        self.content = flet.Column(
            controls=[
                cv.Canvas(
                    width=150,
                    height=100,
                    shapes=[
                        cv.Rect(0, 0, 150, 100,
                                paint=flet.Paint("blue")),
                        cv.Line(5, 5, 145, 5,
                                paint=flet.Paint("white", stroke_width=2)),
                        cv.Line(5, 90, 145, 90,
                                paint=flet.Paint("white", stroke_width=2)),
                        cv.Line(5, 10, 145, 10,
                                paint=flet.Paint("white", stroke_width=2)),
                        cv.Line(5, 95, 145, 95,
                                paint=flet.Paint("white", stroke_width=2)),
                        cv.Line(5, 5, 5, 95,
                                paint=flet.Paint("white", stroke_width=2)),
                        cv.Line(145, 5, 145, 95,
                                paint=flet.Paint("white", stroke_width=2)),
                        cv.Line(15, 5, 15, 95,
                                paint=flet.Paint("white", stroke_width=2)),
                        cv.Line(135, 5, 135, 95,
                                paint=flet.Paint("white", stroke_width=2)),
                        cv.Line(60, 5, 60, 95,
                                paint=flet.Paint("white", stroke_width=2)),
                        cv.Line(90, 5, 90, 95,
                                paint=flet.Paint("white", stroke_width=2)),
                        cv.Line(5, 50, 60, 50,
                                paint=flet.Paint("white", stroke_width=2)),
                        cv.Line(90, 50, 145, 50,
                                paint=flet.Paint("white", stroke_width=2)),
                        cv.Line(75, 5, 75, 95,
                                paint=flet.Paint("white", stroke_width=1,
                                                 stroke_dash_pattern=[3, 5])
                                ),
                        self.serve_origin,
                        self.serve_target
                    ]
                ),
                flet.Row(
                    alignment=flet.MainAxisAlignment.CENTER,
                    controls=[
                        flet.Text(self.player1_name, size=20),
                        flet.IconButton(icon=flet.icons.REMOVE, on_click=self.player1_decrease_score),
                        flet.IconButton(icon=flet.icons.ADD, on_click=self.player1_increase_score),
                        self.player1_score_text,
                        flet.Text("-", size=30),
                        self.player2_score_text,
                        flet.IconButton(icon=flet.icons.REMOVE, on_click=self.player2_decrease_score),
                        flet.IconButton(icon=flet.icons.ADD, on_click=self.player2_increase_score),
                        flet.Text(self.player2_name, size=20)
                    ]
                )
            ]
        )

        # self.content = flet.Row(
        #     alignment=flet.MainAxisAlignment.CENTER,
        #     controls=[
        #         flet.Text(self.player1_name, size=20),
        #         flet.IconButton(icon=flet.icons.REMOVE, on_click=self.player1_decrease_score),
        #         flet.IconButton(icon=flet.icons.ADD, on_click=self.player1_increase_score),
        #         self.player1_score_text,
        #         flet.Text("-", size=30),
        #         self.player2_score_text,
        #         flet.IconButton(icon=flet.icons.REMOVE, on_click=self.player2_decrease_score),
        #         flet.IconButton(icon=flet.icons.ADD, on_click=self.player2_increase_score),
        #         flet.Text(self.player2_name, size=20)
        #     ]
        # )



def main(page: flet.Page):

    def start_game(e):
        nonlocal player1_input_field
        nonlocal player2_input_field

        game_column.controls.insert(0, BadmintonGame(player1_input_field.value, player2_input_field.value))
        game_column.update()


    game_column = flet.Column(

    )

    player1_input_field = flet.TextField(label="Spelare 1")
    player2_input_field = flet.TextField(label="Spelare 2")

    page.add(player1_input_field)
    page.add(player2_input_field)
    page.add(flet.TextButton("Starta match", on_click=start_game))

    page.add(game_column)



flet.app(main)
