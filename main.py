import flet

class BadmintonGame(flet.Container):
    def __init__(self):
        super().__init__()

        self.player1_score_text = flet.Text(str(0), size=50)
        self.player2_score_text = flet.Text(str(0), size=50)


        self.content = flet.Column(
            controls=[
                flet.Row(
                    controls=[
                        self.player1_score_text,
                        flet.Text("-", size=50),
                        self.player2_score_text
                    ]
                )
            ]
        )

class BadmintonSet(flet.Container):

    def player1_increase_score(self, e):
        # ändra variabelvärdet
        if self.player1_score < self.max_score or (self.player1_score - self.player2_score < 2 and self.player1_score < 30):
            self.player1_score += 1

        # ändra texten så den stämmer med variabeln
        self.player1_score_text.value = str(self.player1_score)

        # säg till Flet att en uppdatering har
        # skett så att den visas
        self.player1_score_text.update()
        pass
    def player1_decrease_score(self, e):
        # ändra variabelvärdet
        if self.player1_score > 0:
            self.player1_score -= 1

        # ändra texten så den stämmer med variabeln
        self.player1_score_text.value = str(self.player1_score)

        # säg till Flet att en uppdatering har
        # skett så att den visas
        self.player1_score_text.update()
        pass
    def player2_increase_score(self, e):
        # ändra variabelvärdet
        if self.player2_score < self.max_score or (self.player2_score - self.player1_score < 2 and self.player2_score < 30):
            self.player2_score += 1

        # ändra texten så den stämmer med variabeln
        self.player2_score_text.value = str(self.player2_score)

        # säg till Flet att en uppdatering har
        # skett så att den visas
        self.player2_score_text.update()
        pass
    def player2_decrease_score(self, e):
        # ändra variabelvärdet
        if self.player2_score > 0:
            self.player2_score -= 1

        # ändra texten så den stämmer med variabeln
        self.player2_score_text.value = str(self.player2_score)

        # säg till Flet att en uppdatering har
        # skett så att den visas
        self.player2_score_text.update()
        pass

    def __init__(self, player1_name, player2_name, max_score):
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

        self.content = flet.Row(
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



def main(page: flet.Page):

    def start_game(e):
        nonlocal player1_input_field
        nonlocal player2_input_field
        nonlocal set_column

        set_column.controls.append(
            BadmintonSet(player1_input_field.value, player2_input_field.value, 21)
        )
        set_column.controls.append(
            BadmintonSet(player1_input_field.value, player2_input_field.value, 21)
        )
        set_column.controls.append(
            BadmintonSet(player1_input_field.value, player2_input_field.value, 11)
        )
        set_column.update()


    player1_input_field = flet.TextField(label="Spelare 1")
    player2_input_field = flet.TextField(label="Spelare 2")

    #page.add(player1_input_field)
    #page.add(player2_input_field)
    #page.add(flet.TextButton("Starta match", on_click=start_game))

    set_column = flet.Column(
        scroll=flet.ScrollMode.AUTO,
        expand=True,
        controls=[

        ]
    )

    #page.add(set_column)
    page.add(BadmintonGame())



flet.app(main)
