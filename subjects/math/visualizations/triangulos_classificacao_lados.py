from manim import *

OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"

class TriangulosClassificacaoLadosLight(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Equilateral triangle (all sides equal)
        equi = Polygon(
            [-2.5, -1, 0],
            [-1, 1.5, 0],
            [-4, 1.5, 0],
            stroke_color=BLACK,
            stroke_width=3,
            fill_opacity=0
        )

        # Mark all three sides as equal with single tick marks
        # Right side
        equi_side1_center = (np.array([-2.5, -1, 0]) + np.array([-1, 1.5, 0])) / 2
        equi_mark1 = Line(UP * 0.15, DOWN * 0.15, color=OMSN_RED, stroke_width=6).rotate(70 * DEGREES).move_to(equi_side1_center)

        # Top side
        equi_side2_center = (np.array([-1, 1.5, 0]) + np.array([-4, 1.5, 0])) / 2
        equi_mark2 = Line(LEFT * 0.15, RIGHT * 0.15, color=OMSN_RED, stroke_width=6).move_to(equi_side2_center)

        # Left side
        equi_side3_center = (np.array([-4, 1.5, 0]) + np.array([-2.5, -1, 0])) / 2
        equi_mark3 = Line(UP * 0.15, DOWN * 0.15, color=OMSN_RED, stroke_width=6).rotate(-70 * DEGREES).move_to(equi_side3_center)

        equi_label = Text("Equilátero", font_size=24, color=BLACK).next_to(equi, DOWN, buff=0.3)

        # Isosceles triangle (two sides equal)
        isos = Polygon(
            [0, -1, 0],
            [1, 1.5, 0],
            [-1, 1.5, 0],
            stroke_color=BLACK,
            stroke_width=3,
            fill_opacity=0
        )

        # Mark two equal sides with double tick marks
        # Right side
        isos_side1_center = (np.array([0, -1, 0]) + np.array([1, 1.5, 0])) / 2
        isos_mark1 = VGroup(
            Line(UP * 0.12, DOWN * 0.12, color=OMSN_BLUE, stroke_width=6).rotate(68 * DEGREES).shift(LEFT * 0.05),
            Line(UP * 0.12, DOWN * 0.12, color=OMSN_BLUE, stroke_width=6).rotate(68 * DEGREES).shift(RIGHT * 0.05)
        ).move_to(isos_side1_center)

        # Left side
        isos_side2_center = (np.array([0, -1, 0]) + np.array([-1, 1.5, 0])) / 2
        isos_mark2 = VGroup(
            Line(UP * 0.12, DOWN * 0.12, color=OMSN_BLUE, stroke_width=6).rotate(-68 * DEGREES).shift(LEFT * 0.05),
            Line(UP * 0.12, DOWN * 0.12, color=OMSN_BLUE, stroke_width=6).rotate(-68 * DEGREES).shift(RIGHT * 0.05)
        ).move_to(isos_side2_center)

        isos_label = Text("Isósceles", font_size=24, color=BLACK).next_to(isos, DOWN, buff=0.3)

        # Scalene triangle (all sides different)
        scal = Polygon(
            [3, -1, 0],
            [4.5, 1.5, 0],
            [2, 1, 0],
            stroke_color=BLACK,
            stroke_width=3,
            fill_opacity=0
        )

        scal_label = Text("Escaleno", font_size=24, color=BLACK).next_to(scal, DOWN, buff=0.3)

        # Add all objects
        self.add(equi, equi_mark1, equi_mark2, equi_mark3, equi_label)
        self.add(isos, isos_mark1, isos_mark2, isos_label)
        self.add(scal, scal_label)


class TriangulosClassificacaoLadosDark(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Equilateral triangle (all sides equal)
        equi = Polygon(
            [-2.5, -1, 0],
            [-1, 1.5, 0],
            [-4, 1.5, 0],
            stroke_color=WHITE,
            stroke_width=3,
            fill_opacity=0
        )

        # Mark all three sides as equal with single tick marks
        # Right side
        equi_side1_center = (np.array([-2.5, -1, 0]) + np.array([-1, 1.5, 0])) / 2
        equi_mark1 = Line(UP * 0.15, DOWN * 0.15, color=OMSN_RED, stroke_width=6).rotate(70 * DEGREES).move_to(equi_side1_center)

        # Top side
        equi_side2_center = (np.array([-1, 1.5, 0]) + np.array([-4, 1.5, 0])) / 2
        equi_mark2 = Line(LEFT * 0.15, RIGHT * 0.15, color=OMSN_RED, stroke_width=6).move_to(equi_side2_center)

        # Left side
        equi_side3_center = (np.array([-4, 1.5, 0]) + np.array([-2.5, -1, 0])) / 2
        equi_mark3 = Line(UP * 0.15, DOWN * 0.15, color=OMSN_RED, stroke_width=6).rotate(-70 * DEGREES).move_to(equi_side3_center)

        equi_label = Text("Equilátero", font_size=24, color=WHITE).next_to(equi, DOWN, buff=0.3)

        # Isosceles triangle (two sides equal)
        isos = Polygon(
            [0, -1, 0],
            [1, 1.5, 0],
            [-1, 1.5, 0],
            stroke_color=WHITE,
            stroke_width=3,
            fill_opacity=0
        )

        # Mark two equal sides with double tick marks
        # Right side
        isos_side1_center = (np.array([0, -1, 0]) + np.array([1, 1.5, 0])) / 2
        isos_mark1 = VGroup(
            Line(UP * 0.12, DOWN * 0.12, color=OMSN_BLUE, stroke_width=6).rotate(68 * DEGREES).shift(LEFT * 0.05),
            Line(UP * 0.12, DOWN * 0.12, color=OMSN_BLUE, stroke_width=6).rotate(68 * DEGREES).shift(RIGHT * 0.05)
        ).move_to(isos_side1_center)

        # Left side
        isos_side2_center = (np.array([0, -1, 0]) + np.array([-1, 1.5, 0])) / 2
        isos_mark2 = VGroup(
            Line(UP * 0.12, DOWN * 0.12, color=OMSN_BLUE, stroke_width=6).rotate(-68 * DEGREES).shift(LEFT * 0.05),
            Line(UP * 0.12, DOWN * 0.12, color=OMSN_BLUE, stroke_width=6).rotate(-68 * DEGREES).shift(RIGHT * 0.05)
        ).move_to(isos_side2_center)

        isos_label = Text("Isósceles", font_size=24, color=WHITE).next_to(isos, DOWN, buff=0.3)

        # Scalene triangle (all sides different)
        scal = Polygon(
            [3, -1, 0],
            [4.5, 1.5, 0],
            [2, 1, 0],
            stroke_color=WHITE,
            stroke_width=3,
            fill_opacity=0
        )

        scal_label = Text("Escaleno", font_size=24, color=WHITE).next_to(scal, DOWN, buff=0.3)

        # Add all objects
        self.add(equi, equi_mark1, equi_mark2, equi_mark3, equi_label)
        self.add(isos, isos_mark1, isos_mark2, isos_label)
        self.add(scal, scal_label)
