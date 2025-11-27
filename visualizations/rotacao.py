from manim import *

OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"

class RotacaoLight(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Center of rotation
        O = ORIGIN
        center_dot = Dot(O, color=BLACK, radius=0.08)
        center_label = MathTex("O", color=BLACK).scale(0.8).next_to(center_dot, DOWN, buff=0.15)

        # Create a simple triangle as the original shape
        triangle_vertices = [
            np.array([1.5, 0.5, 0]),
            np.array([2.5, 0.3, 0]),
            np.array([2.0, 1.3, 0])
        ]
        triangle = Polygon(*triangle_vertices, color=OMSN_RED, stroke_width=3, fill_opacity=0.15, fill_color=OMSN_RED)

        # Mark original point M (centroid of triangle)
        M = np.array([2.0, 0.7, 0])
        M_dot = Dot(M, color=OMSN_RED, radius=0.08)
        M_label = MathTex("M", color=OMSN_RED).scale(0.8).next_to(M_dot, RIGHT, buff=0.15)

        # Line from O to M
        line_OM = Line(O, M, color=BLACK, stroke_width=2, stroke_opacity=0.4)

        # Rotation angle (60 degrees counterclockwise)
        angle = 60 * DEGREES

        # Create rotated triangle
        rotated_triangle = triangle.copy()
        rotated_triangle.rotate(angle, about_point=O)
        rotated_triangle.set_color(OMSN_BLUE)
        rotated_triangle.set_fill(OMSN_BLUE, opacity=0.15)

        # Rotated point M'
        M_prime = np.array([
            M[0] * np.cos(angle) - M[1] * np.sin(angle),
            M[0] * np.sin(angle) + M[1] * np.cos(angle),
            0
        ])
        M_prime_dot = Dot(M_prime, color=OMSN_BLUE, radius=0.08)
        M_prime_label = MathTex("M'", color=OMSN_BLUE).scale(0.8).next_to(M_prime_dot, LEFT, buff=0.15)

        # Line from O to M'
        line_OM_prime = Line(O, M_prime, color=BLACK, stroke_width=2, stroke_opacity=0.4)

        # Angle arc showing rotation
        angle_arc = Arc(
            radius=0.8,
            start_angle=Line(O, M).get_angle(),
            angle=angle,
            color=BLACK,
            stroke_width=2,
            arc_center=O
        )

        # Alpha label for angle
        alpha_label = MathTex(r"\alpha", color=BLACK).scale(0.7)
        alpha_label.move_to(O + 1.1 * np.array([np.cos(angle/2 + Line(O, M).get_angle()),
                                                   np.sin(angle/2 + Line(O, M).get_angle()), 0]))

        # Add all elements
        self.add(line_OM, line_OM_prime, angle_arc)
        self.add(triangle, rotated_triangle)
        self.add(center_dot, center_label)
        self.add(M_dot, M_label, M_prime_dot, M_prime_label)
        self.add(alpha_label)


class RotacaoDark(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Center of rotation
        O = ORIGIN
        center_dot = Dot(O, color=WHITE, radius=0.08)
        center_label = MathTex("O", color=WHITE).scale(0.8).next_to(center_dot, DOWN, buff=0.15)

        # Create a simple triangle as the original shape
        triangle_vertices = [
            np.array([1.5, 0.5, 0]),
            np.array([2.5, 0.3, 0]),
            np.array([2.0, 1.3, 0])
        ]
        triangle = Polygon(*triangle_vertices, color=OMSN_RED, stroke_width=3, fill_opacity=0.15, fill_color=OMSN_RED)

        # Mark original point M (centroid of triangle)
        M = np.array([2.0, 0.7, 0])
        M_dot = Dot(M, color=OMSN_RED, radius=0.08)
        M_label = MathTex("M", color=OMSN_RED).scale(0.8).next_to(M_dot, RIGHT, buff=0.15)

        # Line from O to M
        line_OM = Line(O, M, color=WHITE, stroke_width=2, stroke_opacity=0.4)

        # Rotation angle (60 degrees counterclockwise)
        angle = 60 * DEGREES

        # Create rotated triangle
        rotated_triangle = triangle.copy()
        rotated_triangle.rotate(angle, about_point=O)
        rotated_triangle.set_color(OMSN_BLUE)
        rotated_triangle.set_fill(OMSN_BLUE, opacity=0.15)

        # Rotated point M'
        M_prime = np.array([
            M[0] * np.cos(angle) - M[1] * np.sin(angle),
            M[0] * np.sin(angle) + M[1] * np.cos(angle),
            0
        ])
        M_prime_dot = Dot(M_prime, color=OMSN_BLUE, radius=0.08)
        M_prime_label = MathTex("M'", color=OMSN_BLUE).scale(0.8).next_to(M_prime_dot, LEFT, buff=0.15)

        # Line from O to M'
        line_OM_prime = Line(O, M_prime, color=WHITE, stroke_width=2, stroke_opacity=0.4)

        # Angle arc showing rotation
        angle_arc = Arc(
            radius=0.8,
            start_angle=Line(O, M).get_angle(),
            angle=angle,
            color=WHITE,
            stroke_width=2,
            arc_center=O
        )

        # Alpha label for angle
        alpha_label = MathTex(r"\alpha", color=WHITE).scale(0.7)
        alpha_label.move_to(O + 1.1 * np.array([np.cos(angle/2 + Line(O, M).get_angle()),
                                                   np.sin(angle/2 + Line(O, M).get_angle()), 0]))

        # Add all elements
        self.add(line_OM, line_OM_prime, angle_arc)
        self.add(triangle, rotated_triangle)
        self.add(center_dot, center_label)
        self.add(M_dot, M_label, M_prime_dot, M_prime_label)
        self.add(alpha_label)
