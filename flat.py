import math
import flet as ft
import flet.canvas as cv

def main(page: ft.Page):
    page.padding = 0
    page.window_height = 525
    page.window_width = 500
    num = 83
    page.window_title_bar_hidden = True
    stroke_paint = ft.Paint(stroke_width=15, style=ft.PaintingStyle.STROKE, color=ft.colors.BLUE)

    # Загрузка шрифта
    page.fonts = {
        "speed": "/fonts/spdfont"
    }

    cp = cv.Canvas(
        [
            cv.Circle(250, 250, 242, stroke_paint),
            cv.Path(
                [
                    cv.Path.MoveTo(50, 250),
                    cv.Path.LineTo(450, 250),
                    cv.Path.Close(),
                ],
                paint=ft.Paint(
                    stroke_width=4,
                    style=ft.PaintingStyle.STROKE,
                    color=ft.colors.GREY,
                ),
            ),
            cv.Text(
                240,
                160,
                str(num) + " km/h",
                ft.TextStyle(weight=ft.FontWeight.BOLD, size=60, font_family=page.fonts["speed"]),  # Использование загруженного шрифта
                alignment=ft.alignment.top_center,
            ),
            cv.Text(
                240,
                270,
                "Comfort",
                ft.TextStyle(weight=ft.FontWeight.BOLD, size=40, font_family=page.fonts["speed"]),  # Использование загруженного шрифта
                alignment=ft.alignment.top_center,
            ),
            cv.Text(
                240,
                400,
                "53 минуты",
                ft.TextStyle(weight=ft.FontWeight.BOLD, size=30, font_family=page.fonts["speed"]),  # Использование загруженного шрифта
                alignment=ft.alignment.top_center,
            ),
        ],
        width=float("inf"),
        expand=True,
    )

    page.add(cp)

ft.app(main)