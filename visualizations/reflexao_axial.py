from manim import *

OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"

class ReflexaoAxialLight(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Create a simple F-shaped polygon on the left
        points_original = [
            [-3, 1.5, 0],
            [-3, -1.5, 0],
            [-2.2, -1.5, 0],
            [-2.2, -0.3, 0],
            [-2.6, -0.3, 0],
            [-2.6, 0.3, 0],
            [-2.2, 0.3, 0],
            [-2.2, 0.9, 0],
            [-2.6, 0.9, 0],
            [-2.6, 1.5, 0],
        ]

        original_shape = Polygon(*points_original, color=OMSN_RED, fill_opacity=0.3, stroke_width=3)

        # Reflection axis (vertical line at x=0)
        axis = DashedLine(UP * 3, DOWN * 3, color=BLACK, stroke_width=2)
        axis_label = MathTex("r", color=BLACK).scale(0.8).next_to(axis, UP, buff=0.1)

        # Create reflected shape (mirror across x=0)
        points_reflected = [[p[0] * -1, p[1], p[2]] for p in points_original]
        reflected_shape = Polygon(*points_reflected, color=OMSN_BLUE, fill_opacity=0.3, stroke_width=3)

        # Show correspondence with dashed lines for a few key points
        # Top-left corner of original
        point_M = Dot(points_original[0], color=OMSN_RED, radius=0.06)
        point_M_prime = Dot(points_reflected[0], color=OMSN_BLUE, radius=0.06)
        label_M = MathTex("M", color=BLACK).scale(0.7).next_to(point_M, LEFT, buff=0.15)
        label_M_prime = MathTex("M'", color=BLACK).scale(0.7).next_to(point_M_prime, RIGHT, buff=0.15)

        # Perpendicular connection line
        perp_line = DashedLine(points_original[0], points_reflected[0], color=BLACK, stroke_width=1.5, dash_length=0.1)

        # Midpoint on axis
        midpoint = Dot([0, 1.5, 0], color=BLACK, radius=0.04)

        # Add all elements
        self.add(axis, axis_label)
        self.add(original_shape, reflected_shape)
        self.add(perp_line, point_M, point_M_prime, midpoint)
        self.add(label_M, label_M_prime)


class ReflexaoAxialDark(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Create a simple F-shaped polygon on the left
        points_original = [
            [-3, 1.5, 0],
            [-3, -1.5, 0],
            [-2.2, -1.5, 0],
            [-2.2, -0.3, 0],
            [-2.6, -0.3, 0],
            [-2.6, 0.3, 0],
            [-2.2, 0.3, 0],
            [-2.2, 0.9, 0],
            [-2.6, 0.9, 0],
            [-2.6, 1.5, 0],
        ]

        original_shape = Polygon(*points_original, color=OMSN_RED, fill_opacity=0.3, stroke_width=3)

        # Reflection axis (vertical line at x=0)
        axis = DashedLine(UP * 3, DOWN * 3, color=WHITE, stroke_width=2)
        axis_label = MathTex("r", color=WHITE).scale(0.8).next_to(axis, UP, buff=0.1)

        # Create reflected shape (mirror across x=0)
        points_reflected = [[p[0] * -1, p[1], p[2]] for p in points_original]
        reflected_shape = Polygon(*points_reflected, color=OMSN_BLUE, fill_opacity=0.3, stroke_width=3)

        # Show correspondence with dashed lines for a few key points
        # Top-left corner of original
        point_M = Dot(points_original[0], color=OMSN_RED, radius=0.06)
        point_M_prime = Dot(points_reflected[0], color=OMSN_BLUE, radius=0.06)
        label_M = MathTex("M", color=WHITE).scale(0.7).next_to(point_M, LEFT, buff=0.15)
        label_M_prime = MathTex("M'", color=WHITE).scale(0.7).next_to(point_M_prime, RIGHT, buff=0.15)

        # Perpendicular connection line
        perp_line = DashedLine(points_original[0], points_reflected[0], color=WHITE, stroke_width=1.5, dash_length=0.1)

        # Midpoint on axis
        midpoint = Dot([0, 1.5, 0], color=WHITE, radius=0.04)

        # Add all elements
        self.add(axis, axis_label)
        self.add(original_shape, reflected_shape)
        self.add(perp_line, point_M, point_M_prime, midpoint)
        self.add(label_M, label_M_prime)
