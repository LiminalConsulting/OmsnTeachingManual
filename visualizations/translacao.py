from manim import *

OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"

class TranslacaoLight(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Create a simple triangle as the original shape
        triangle = Polygon(
            [-2, -1, 0],
            [-1.5, 0.5, 0],
            [-3, 0, 0],
            stroke_color=BLACK,
            stroke_width=3,
            fill_color=OMSN_RED,
            fill_opacity=0.3
        )

        # Translation vector
        translation = np.array([3, 2, 0])

        # Create translated triangle
        triangle_translated = triangle.copy()
        triangle_translated.shift(translation)
        triangle_translated.set_stroke(color=BLACK)
        triangle_translated.set_fill(color=OMSN_BLUE, opacity=0.3)

        # Create translation vector arrow
        arrow = Arrow(
            start=triangle.get_center(),
            end=triangle_translated.get_center(),
            color=BLACK,
            stroke_width=3,
            buff=0,
            max_tip_length_to_length_ratio=0.15
        )

        # Add vector label
        vector_label = MathTex(r"\vec{v}", color=BLACK).scale(0.8)
        vector_label.next_to(arrow, UP, buff=0.1)

        # Add vertex labels for original triangle
        A = MathTex("A", color=BLACK).scale(0.7)
        B = MathTex("B", color=BLACK).scale(0.7)
        C = MathTex("C", color=BLACK).scale(0.7)

        A.next_to(triangle.get_vertices()[0], LEFT, buff=0.15)
        B.next_to(triangle.get_vertices()[1], UP, buff=0.15)
        C.next_to(triangle.get_vertices()[2], DOWN, buff=0.15)

        # Add vertex labels for translated triangle
        A_prime = MathTex("A'", color=BLACK).scale(0.7)
        B_prime = MathTex("B'", color=BLACK).scale(0.7)
        C_prime = MathTex("C'", color=BLACK).scale(0.7)

        A_prime.next_to(triangle_translated.get_vertices()[0], RIGHT, buff=0.15)
        B_prime.next_to(triangle_translated.get_vertices()[1], UP, buff=0.15)
        C_prime.next_to(triangle_translated.get_vertices()[2], DOWN, buff=0.15)

        # Add all objects to scene
        self.add(triangle, triangle_translated, arrow, vector_label)
        self.add(A, B, C, A_prime, B_prime, C_prime)


class TranslacaoDark(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Create a simple triangle as the original shape
        triangle = Polygon(
            [-2, -1, 0],
            [-1.5, 0.5, 0],
            [-3, 0, 0],
            stroke_color=WHITE,
            stroke_width=3,
            fill_color=OMSN_RED,
            fill_opacity=0.3
        )

        # Translation vector
        translation = np.array([3, 2, 0])

        # Create translated triangle
        triangle_translated = triangle.copy()
        triangle_translated.shift(translation)
        triangle_translated.set_stroke(color=WHITE)
        triangle_translated.set_fill(color=OMSN_BLUE, opacity=0.3)

        # Create translation vector arrow
        arrow = Arrow(
            start=triangle.get_center(),
            end=triangle_translated.get_center(),
            color=WHITE,
            stroke_width=3,
            buff=0,
            max_tip_length_to_length_ratio=0.15
        )

        # Add vector label
        vector_label = MathTex(r"\vec{v}", color=WHITE).scale(0.8)
        vector_label.next_to(arrow, UP, buff=0.1)

        # Add vertex labels for original triangle
        A = MathTex("A", color=WHITE).scale(0.7)
        B = MathTex("B", color=WHITE).scale(0.7)
        C = MathTex("C", color=WHITE).scale(0.7)

        A.next_to(triangle.get_vertices()[0], LEFT, buff=0.15)
        B.next_to(triangle.get_vertices()[1], UP, buff=0.15)
        C.next_to(triangle.get_vertices()[2], DOWN, buff=0.15)

        # Add vertex labels for translated triangle
        A_prime = MathTex("A'", color=WHITE).scale(0.7)
        B_prime = MathTex("B'", color=WHITE).scale(0.7)
        C_prime = MathTex("C'", color=WHITE).scale(0.7)

        A_prime.next_to(triangle_translated.get_vertices()[0], RIGHT, buff=0.15)
        B_prime.next_to(triangle_translated.get_vertices()[1], UP, buff=0.15)
        C_prime.next_to(triangle_translated.get_vertices()[2], DOWN, buff=0.15)

        # Add all objects to scene
        self.add(triangle, triangle_translated, arrow, vector_label)
        self.add(A, B, C, A_prime, B_prime, C_prime)
