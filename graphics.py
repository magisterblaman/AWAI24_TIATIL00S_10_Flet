import flet
import flet.canvas as cv


def main(page: flet.Page):

    # ""
    # "player1_even"
    # "player1_odd"
    # "player2_even"
    # "player2_odd"
    serve_state = "player2_odd"

    serve_origin = cv.Circle(112.5, 30, 10,
                      paint=flet.Paint("red"))

    serve_target = cv.Circle(37.5, 70, 10,
                      paint=flet.Paint("red", stroke_width=3,
                                       style=flet.PaintingStyle.STROKE))

    if serve_state == "player1_even":
        serve_origin.x = 37.5
        serve_origin.y = 70
        serve_target.x = 112.5
        serve_target.y = 30
    elif serve_state == "player1_odd":
        serve_origin.x = 37.5
        serve_origin.y = 30
        serve_target.x = 112.5
        serve_target.y = 70
    elif serve_state == "player2_even":
        serve_target.x = 37.5
        serve_target.y = 70
        serve_origin.x = 112.5
        serve_origin.y = 30
    elif serve_state == "player2_odd":
        serve_target.x = 37.5
        serve_target.y = 30
        serve_origin.x = 112.5
        serve_origin.y = 70

    page.add(cv.Canvas(
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
            serve_origin,
            serve_target
        ]
    ))
    pass


flet.app(main)
