import flet
import flet.canvas as cv

def main(page: flet.Page):
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
        ]
    ))
    pass

flet.app(main)