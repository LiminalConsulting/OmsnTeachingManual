from manim import *

OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"


def build_quadrilaterals(scene, stroke_color, text_color):
    """Build quadrilateral types visualization"""

    # Parallelogram
    para = Polygon(
        [-1.2, -0.4, 0], [1.2, -0.4, 0], [1.6, 0.6, 0], [-0.8, 0.6, 0],
        color=stroke_color, stroke_width=3
    ).shift(LEFT * 4.5 + UP * 1.5)
    para_label = Text("Paralelogramo", font_size=18, color=text_color).next_to(para, DOWN, buff=0.15)

    # Rhombus (Losango)
    losango = Polygon(
        [0, -0.6, 0], [0.8, 0, 0], [0, 0.6, 0], [-0.8, 0, 0],
        color=stroke_color, stroke_width=3, fill_color=OMSN_RED, fill_opacity=0.2
    ).shift(LEFT * 1.5 + UP * 1.5)
    losango_label = Text("Losango", font_size=18, color=text_color).next_to(losango, DOWN, buff=0.15)

    # Rectangle (Retângulo)
    ret = Rectangle(width=1.6, height=1, color=stroke_color, stroke_width=3).shift(RIGHT * 1.5 + UP * 1.5)
    ret_label = Text("Retângulo", font_size=18, color=text_color).next_to(ret, DOWN, buff=0.15)

    # Square (Quadrado)
    quad = Square(side_length=1, color=stroke_color, stroke_width=3, fill_color=OMSN_BLUE, fill_opacity=0.2).shift(RIGHT * 4.5 + UP * 1.5)
    quad_label = Text("Quadrado", font_size=18, color=text_color).next_to(quad, DOWN, buff=0.15)

    # Trapezoid (Trapézio)
    trap = Polygon(
        [-0.6, -0.5, 0], [0.6, -0.5, 0], [1, 0.5, 0], [-1, 0.5, 0],
        color=stroke_color, stroke_width=3
    ).shift(LEFT * 3 + DOWN * 1.5)
    trap_label = Text("Trapézio", font_size=18, color=text_color).next_to(trap, DOWN, buff=0.15)

    # Kite (Papagaio)
    papagaio = Polygon(
        [0, 0.8, 0], [0.5, 0, 0], [0, -0.6, 0], [-0.5, 0, 0],
        color=stroke_color, stroke_width=3
    ).shift(RIGHT * 3 + DOWN * 1.5)
    papagaio_label = Text("Papagaio", font_size=18, color=text_color).next_to(papagaio, DOWN, buff=0.15)

    scene.add(para, para_label)
    scene.add(losango, losango_label)
    scene.add(ret, ret_label)
    scene.add(quad, quad_label)
    scene.add(trap, trap_label)
    scene.add(papagaio, papagaio_label)


class QuadrilaterosLight(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        build_quadrilaterals(self, stroke_color=BLACK, text_color=BLACK)


class QuadrilaterosDark(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        build_quadrilaterals(self, stroke_color=WHITE, text_color=WHITE)
