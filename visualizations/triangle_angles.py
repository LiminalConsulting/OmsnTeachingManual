from manim import *

# OMSN Color Scheme
OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"


class TriangleAnglesSumLight(Scene):
    """
    Light mode (white background) - for print manual
    Concept: Grade 5 - "A soma dos ângulos internos de um triângulo é igual a um ângulo raso"
    """
    def construct(self):
        self.camera.background_color = WHITE
        stroke_color = BLACK
        text_color = BLACK

        self._build_scene(stroke_color, text_color)

    def _build_scene(self, stroke_color, text_color):
        # Create a triangle
        A = np.array([-2.5, -1, 0])
        B = np.array([2.5, -1, 0])
        C = np.array([0, 2, 0])

        triangle = Polygon(A, B, C, color=stroke_color, stroke_width=3)

        # Labels for vertices
        label_A = MathTex("A", color=text_color).next_to(A, DOWN, buff=0.15)
        label_B = MathTex("B", color=text_color).next_to(B, DOWN, buff=0.15)
        label_C = MathTex("C", color=text_color).next_to(C, UP, buff=0.15)

        # Create angle arcs
        angle_A = Angle.from_three_points(B, A, C, radius=0.4, color=OMSN_RED)
        angle_B = Angle.from_three_points(C, B, A, radius=0.4, color=OMSN_BLUE)
        angle_C = Angle.from_three_points(A, C, B, radius=0.4, color=stroke_color)

        # Angle labels
        alpha = MathTex(r"\alpha", color=OMSN_RED, font_size=26).move_to(
            Angle.from_three_points(B, A, C, radius=0.7).point_from_proportion(0.5)
        )
        beta = MathTex(r"\beta", color=OMSN_BLUE, font_size=26).move_to(
            Angle.from_three_points(C, B, A, radius=0.7).point_from_proportion(0.5)
        )
        gamma = MathTex(r"\gamma", color=text_color, font_size=26).move_to(
            Angle.from_three_points(A, C, B, radius=0.65).point_from_proportion(0.5)
        )

        # Formula
        formula = MathTex(r"\alpha", "+", r"\beta", "+", r"\gamma", "=", r"180^\circ", font_size=42)
        formula.set_color(text_color)
        formula[0].set_color(OMSN_RED)
        formula[2].set_color(OMSN_BLUE)
        formula.to_edge(DOWN, buff=0.8)

        # Build the scene (no title - handled by LaTeX)
        self.add(triangle)
        self.add(label_A, label_B, label_C)
        self.add(angle_A, angle_B, angle_C)
        self.add(alpha, beta, gamma)
        self.add(formula)


class TriangleAnglesSumDark(Scene):
    """
    Dark mode (black background) - for digital version
    """
    def construct(self):
        self.camera.background_color = BLACK
        stroke_color = WHITE
        text_color = WHITE

        # Reuse the same build logic
        A = np.array([-2.5, -1, 0])
        B = np.array([2.5, -1, 0])
        C = np.array([0, 2, 0])

        triangle = Polygon(A, B, C, color=stroke_color, stroke_width=3)

        label_A = MathTex("A", color=text_color).next_to(A, DOWN, buff=0.15)
        label_B = MathTex("B", color=text_color).next_to(B, DOWN, buff=0.15)
        label_C = MathTex("C", color=text_color).next_to(C, UP, buff=0.15)

        angle_A = Angle.from_three_points(B, A, C, radius=0.4, color=OMSN_RED)
        angle_B = Angle.from_three_points(C, B, A, radius=0.4, color=OMSN_BLUE)
        angle_C = Angle.from_three_points(A, C, B, radius=0.4, color=stroke_color)

        alpha = MathTex(r"\alpha", color=OMSN_RED, font_size=26).move_to(
            Angle.from_three_points(B, A, C, radius=0.7).point_from_proportion(0.5)
        )
        beta = MathTex(r"\beta", color=OMSN_BLUE, font_size=26).move_to(
            Angle.from_three_points(C, B, A, radius=0.7).point_from_proportion(0.5)
        )
        gamma = MathTex(r"\gamma", color=text_color, font_size=26).move_to(
            Angle.from_three_points(A, C, B, radius=0.65).point_from_proportion(0.5)
        )

        formula = MathTex(r"\alpha", "+", r"\beta", "+", r"\gamma", "=", r"180^\circ", font_size=42)
        formula.set_color(text_color)
        formula[0].set_color(OMSN_RED)
        formula[2].set_color(OMSN_BLUE)
        formula.to_edge(DOWN, buff=0.8)

        self.add(triangle)
        self.add(label_A, label_B, label_C)
        self.add(angle_A, angle_B, angle_C)
        self.add(alpha, beta, gamma)
        self.add(formula)
