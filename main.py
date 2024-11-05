import flet


def main(page: flet.Page):
    player1_score = 0
    player2_score = 0

    player1_score_text = flet.Text(str(player1_score), size=30)
    player2_score_text = flet.Text(str(player2_score), size=30)

    def player1_increase_score(e):
        nonlocal player1_score
        nonlocal player1_score_text

        # ändra variabelvärdet
        player1_score += 1

        # ändra texten så den stämmer med variabeln
        player1_score_text.value = str(player1_score)

        # säg till Flet att en uppdatering har
        # skett så att den visas
        player1_score_text.update()
        pass
    def player1_decrease_score(e):
        nonlocal player1_score
        nonlocal player1_score_text

        # ändra variabelvärdet
        player1_score -= 1

        # ändra texten så den stämmer med variabeln
        player1_score_text.value = str(player1_score)

        # säg till Flet att en uppdatering har
        # skett så att den visas
        player1_score_text.update()
        pass
    def player2_increase_score(e):
        nonlocal player2_score
        nonlocal player2_score_text

        # ändra variabelvärdet
        player2_score += 1

        # ändra texten så den stämmer med variabeln
        player2_score_text.value = str(player2_score)

        # säg till Flet att en uppdatering har
        # skett så att den visas
        player2_score_text.update()
        pass
    def player2_decrease_score(e):
        nonlocal player2_score
        nonlocal player2_score_text

        # ändra variabelvärdet
        player2_score -= 1

        # ändra texten så den stämmer med variabeln
        player2_score_text.value = str(player2_score)

        # säg till Flet att en uppdatering har
        # skett så att den visas
        player2_score_text.update()
        pass

    page.add(flet.Container(
        bgcolor="#ffdddd",
        content=flet.Row(
            alignment="center",
            controls=[
                flet.Text("Bertil", size=20),
                flet.IconButton(icon=flet.icons.REMOVE, on_click=player1_decrease_score),
                flet.IconButton(icon=flet.icons.ADD, on_click=player1_increase_score),
                player1_score_text,
                flet.Text("-", size=30),
                player2_score_text,
                flet.IconButton(icon=flet.icons.REMOVE, on_click=player2_decrease_score),
                flet.IconButton(icon=flet.icons.ADD, on_click=player2_increase_score),
                flet.Text("Wlem", size=20)
            ]
        )

    ))



flet.app(main)
