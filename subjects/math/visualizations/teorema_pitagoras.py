from manim import *

OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"

class TeoremaPitagorasLight(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Right triangle with sides 3, 4, 5 (scaled)
        scale = 1.2
        a = 3 * scale  # vertical cathetus
        b = 4 * scale  # horizontal cathetus
        c = 5 * scale  # hypotenuse

        # Triangle vertices
        A = np.array([-b/2, -a/2, 0])  # bottom left (right angle)
        B = np.array([b/2, -a/2, 0])   # bottom right
        C = np.array([-b/2, a/2, 0])   # top left

        # Create triangle
        triangle = Polygon(A, B, C, stroke_color=BLACK, stroke_width=3, fill_opacity=0)

        # Right angle marker
        right_angle_size = 0.4
        right_angle = VGroup(
            Line(A, A + RIGHT * right_angle_size, stroke_color=BLACK, stroke_width=2),
            Line(A + RIGHT * right_angle_size, A + RIGHT * right_angle_size + UP * right_angle_size,
                 stroke_color=BLACK, stroke_width=2),
            Line(A + UP * right_angle_size, A, stroke_color=BLACK, stroke_width=2)
        )

        # Square on cathetus a (vertical) - RED
        square_a_vertices = [
            C,
            C + LEFT * a,
            A + LEFT * a,
            A
        ]
        square_a = Polygon(*square_a_vertices, stroke_color=BLACK, stroke_width=2,
                          fill_color=OMSN_RED, fill_opacity=0.3)

        # Square on cathetus b (horizontal) - BLUE
        square_b_vertices = [
            A,
            B,
            B + DOWN * b,
            A + DOWN * b
        ]
        square_b = Polygon(*square_b_vertices, stroke_color=BLACK, stroke_width=2,
                          fill_color=OMSN_BLUE, fill_opacity=0.3)

        # Square on hypotenuse c - no fill
        # Direction vector from B to C
        BC_vector = C - B
        BC_unit = BC_vector / np.linalg.norm(BC_vector)
        # Perpendicular vector (rotated 90 degrees)
        perp_vector = np.array([-BC_unit[1], BC_unit[0], 0]) * c

        square_c_vertices = [
            B,
            C,
            C + perp_vector,
            B + perp_vector
        ]
        square_c = Polygon(*square_c_vertices, stroke_color=BLACK, stroke_width=2,
                          fill_opacity=0)

        # Labels for triangle sides
        label_a = MathTex("a", color=BLACK, font_size=36).next_to(
            Line(A, C).get_center(), LEFT, buff=0.25
        )
        label_b = MathTex("b", color=BLACK, font_size=36).next_to(
            Line(A, B).get_center(), DOWN, buff=0.25
        )
        label_c = MathTex("c", color=BLACK, font_size=36).next_to(
            Line(B, C).get_center(), UR, buff=0.25
        )

        # Labels for squares (a², b², c²)
        label_a2 = MathTex("a^2", color=BLACK, font_size=32).move_to(
            square_a.get_center()
        )
        label_b2 = MathTex("b^2", color=BLACK, font_size=32).move_to(
            square_b.get_center()
        )
        label_c2 = MathTex("c^2", color=BLACK, font_size=32).move_to(
            square_c.get_center()
        )

        # Add all elements
        self.add(square_a, square_b, square_c)
        self.add(triangle, right_angle)
        self.add(label_a, label_b, label_c)
        self.add(label_a2, label_b2, label_c2)


class TeoremaPitagorasDark(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Right triangle with sides 3, 4, 5 (scaled)
        scale = 1.2
        a = 3 * scale  # vertical cathetus
        b = 4 * scale  # horizontal cathetus
        c = 5 * scale  # hypotenuse

        # Triangle vertices
        A = np.array([-b/2, -a/2, 0])  # bottom left (right angle)
        B = np.array([b/2, -a/2, 0])   # bottom right
        C = np.array([-b/2, a/2, 0])   # top left

        # Create triangle
        triangle = Polygon(A, B, C, stroke_color=WHITE, stroke_width=3, fill_opacity=0)

        # Right angle marker
        right_angle_size = 0.4
        right_angle = VGroup(
            Line(A, A + RIGHT * right_angle_size, stroke_color=WHITE, stroke_width=2),
            Line(A + RIGHT * right_angle_size, A + RIGHT * right_angle_size + UP * right_angle_size,
                 stroke_color=WHITE, stroke_width=2),
            Line(A + UP * right_angle_size, A, stroke_color=WHITE, stroke_width=2)
        )

        # Square on cathetus a (vertical) - RED
        square_a_vertices = [
            C,
            C + LEFT * a,
            A + LEFT * a,
            A
        ]
        square_a = Polygon(*square_a_vertices, stroke_color=WHITE, stroke_width=2,
                          fill_color=OMSN_RED, fill_opacity=0.3)

        # Square on cathetus b (horizontal) - BLUE
        square_b_vertices = [
            A,
            B,
            B + DOWN * b,
            A + DOWN * b
        ]
        square_b = Polygon(*square_b_vertices, stroke_color=WHITE, stroke_width=2,
                          fill_color=OMSN_BLUE, fill_opacity=0.3)

        # Square on hypotenuse c - no fill
        # Direction vector from B to C
        BC_vector = C - B
        BC_unit = BC_vector / np.linalg.norm(BC_vector)
        # Perpendicular vector (rotated 90 degrees)
        perp_vector = np.array([-BC_unit[1], BC_unit[0], 0]) * c

        square_c_vertices = [
            B,
            C,
            C + perp_vector,
            B + perp_vector
        ]
        square_c = Polygon(*square_c_vertices, stroke_color=WHITE, stroke_width=2,
                          fill_opacity=0)

        # Labels for triangle sides
        label_a = MathTex("a", color=WHITE, font_size=36).next_to(
            Line(A, C).get_center(), LEFT, buff=0.25
        )
        label_b = MathTex("b", color=WHITE, font_size=36).next_to(
            Line(A, B).get_center(), DOWN, buff=0.25
        )
        label_c = MathTex("c", color=WHITE, font_size=36).next_to(
            Line(B, C).get_center(), UR, buff=0.25
        )

        # Labels for squares (a², b², c²)
        label_a2 = MathTex("a^2", color=WHITE, font_size=32).move_to(
            square_a.get_center()
        )
        label_b2 = MathTex("b^2", color=WHITE, font_size=32).move_to(
            square_b.get_center()
        )
        label_c2 = MathTex("c^2", color=WHITE, font_size=32).move_to(
            square_c.get_center()
        )

        # Add all elements
        self.add(square_a, square_b, square_c)
        self.add(triangle, right_angle)
        self.add(label_a, label_b, label_c)
        self.add(label_a2, label_b2, label_c2)
