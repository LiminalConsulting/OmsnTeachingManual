from manim import *
import numpy as np

OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"

class TriangulosClassificacaoAngulosLight(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Acutângulo (Acute) - all angles < 90°
        acute_vertices = [
            np.array([-0.5, -0.5, 0]),
            np.array([0.5, -0.5, 0]),
            np.array([0, 0.7, 0])
        ]
        acute = Polygon(*acute_vertices, stroke_color=BLACK, stroke_width=3, fill_opacity=0)

        # Add angle arcs for acute triangle
        acute_angle1 = Arc(radius=0.3, start_angle=0, angle=60*DEGREES,
                          arc_center=acute_vertices[0], stroke_color=OMSN_RED, stroke_width=2.5)
        acute_angle2 = Arc(radius=0.3, start_angle=120*DEGREES, angle=60*DEGREES,
                          arc_center=acute_vertices[1], stroke_color=OMSN_RED, stroke_width=2.5)
        acute_angle3 = Arc(radius=0.3, start_angle=240*DEGREES, angle=60*DEGREES,
                          arc_center=acute_vertices[2], stroke_color=OMSN_RED, stroke_width=2.5)

        acute_label = Text("Acutângulo", font_size=24, color=BLACK).next_to(acute, DOWN, buff=0.3)
        acute_group = VGroup(acute, acute_angle1, acute_angle2, acute_angle3, acute_label)
        acute_group.shift(LEFT * 4)

        # Retângulo (Right) - one 90° angle
        right_vertices = [
            np.array([-0.6, -0.5, 0]),
            np.array([0.6, -0.5, 0]),
            np.array([-0.6, 0.7, 0])
        ]
        right_tri = Polygon(*right_vertices, stroke_color=BLACK, stroke_width=3, fill_opacity=0)

        # Right angle square indicator
        right_angle_square = Square(side_length=0.2, stroke_color=OMSN_BLUE, stroke_width=2.5, fill_opacity=0)
        right_angle_square.move_to(right_vertices[0] + np.array([0.1, 0.1, 0]))

        # Other angles
        right_angle1 = Arc(radius=0.3, start_angle=0, angle=45*DEGREES,
                          arc_center=right_vertices[1], stroke_color=OMSN_RED, stroke_width=2.5)
        right_angle2 = Arc(radius=0.3, start_angle=270*DEGREES, angle=45*DEGREES,
                          arc_center=right_vertices[2], stroke_color=OMSN_RED, stroke_width=2.5)

        right_label = Text("Retângulo", font_size=24, color=BLACK).next_to(right_tri, DOWN, buff=0.3)
        right_group = VGroup(right_tri, right_angle_square, right_angle1, right_angle2, right_label)

        # Obtusângulo (Obtuse) - one angle > 90°
        obtuse_vertices = [
            np.array([-0.7, -0.5, 0]),
            np.array([0.7, -0.5, 0]),
            np.array([-0.4, 0.7, 0])
        ]
        obtuse = Polygon(*obtuse_vertices, stroke_color=BLACK, stroke_width=3, fill_opacity=0)

        # Add angle arcs for obtuse triangle
        obtuse_angle1 = Arc(radius=0.35, start_angle=0, angle=110*DEGREES,
                           arc_center=obtuse_vertices[0], stroke_color=OMSN_BLUE, stroke_width=2.5)
        obtuse_angle2 = Arc(radius=0.3, start_angle=140*DEGREES, angle=40*DEGREES,
                           arc_center=obtuse_vertices[1], stroke_color=OMSN_RED, stroke_width=2.5)
        obtuse_angle3 = Arc(radius=0.3, start_angle=250*DEGREES, angle=30*DEGREES,
                           arc_center=obtuse_vertices[2], stroke_color=OMSN_RED, stroke_width=2.5)

        obtuse_label = Text("Obtusângulo", font_size=24, color=BLACK).next_to(obtuse, DOWN, buff=0.3)
        obtuse_group = VGroup(obtuse, obtuse_angle1, obtuse_angle2, obtuse_angle3, obtuse_label)
        obtuse_group.shift(RIGHT * 4)

        # Add all groups to scene
        self.add(acute_group, right_group, obtuse_group)


class TriangulosClassificacaoAngulosDark(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Acutângulo (Acute) - all angles < 90°
        acute_vertices = [
            np.array([-0.5, -0.5, 0]),
            np.array([0.5, -0.5, 0]),
            np.array([0, 0.7, 0])
        ]
        acute = Polygon(*acute_vertices, stroke_color=WHITE, stroke_width=3, fill_opacity=0)

        # Add angle arcs for acute triangle
        acute_angle1 = Arc(radius=0.3, start_angle=0, angle=60*DEGREES,
                          arc_center=acute_vertices[0], stroke_color=OMSN_RED, stroke_width=2.5)
        acute_angle2 = Arc(radius=0.3, start_angle=120*DEGREES, angle=60*DEGREES,
                          arc_center=acute_vertices[1], stroke_color=OMSN_RED, stroke_width=2.5)
        acute_angle3 = Arc(radius=0.3, start_angle=240*DEGREES, angle=60*DEGREES,
                          arc_center=acute_vertices[2], stroke_color=OMSN_RED, stroke_width=2.5)

        acute_label = Text("Acutângulo", font_size=24, color=WHITE).next_to(acute, DOWN, buff=0.3)
        acute_group = VGroup(acute, acute_angle1, acute_angle2, acute_angle3, acute_label)
        acute_group.shift(LEFT * 4)

        # Retângulo (Right) - one 90° angle
        right_vertices = [
            np.array([-0.6, -0.5, 0]),
            np.array([0.6, -0.5, 0]),
            np.array([-0.6, 0.7, 0])
        ]
        right_tri = Polygon(*right_vertices, stroke_color=WHITE, stroke_width=3, fill_opacity=0)

        # Right angle square indicator
        right_angle_square = Square(side_length=0.2, stroke_color=OMSN_BLUE, stroke_width=2.5, fill_opacity=0)
        right_angle_square.move_to(right_vertices[0] + np.array([0.1, 0.1, 0]))

        # Other angles
        right_angle1 = Arc(radius=0.3, start_angle=0, angle=45*DEGREES,
                          arc_center=right_vertices[1], stroke_color=OMSN_RED, stroke_width=2.5)
        right_angle2 = Arc(radius=0.3, start_angle=270*DEGREES, angle=45*DEGREES,
                          arc_center=right_vertices[2], stroke_color=OMSN_RED, stroke_width=2.5)

        right_label = Text("Retângulo", font_size=24, color=WHITE).next_to(right_tri, DOWN, buff=0.3)
        right_group = VGroup(right_tri, right_angle_square, right_angle1, right_angle2, right_label)

        # Obtusângulo (Obtuse) - one angle > 90°
        obtuse_vertices = [
            np.array([-0.7, -0.5, 0]),
            np.array([0.7, -0.5, 0]),
            np.array([-0.4, 0.7, 0])
        ]
        obtuse = Polygon(*obtuse_vertices, stroke_color=WHITE, stroke_width=3, fill_opacity=0)

        # Add angle arcs for obtuse triangle
        obtuse_angle1 = Arc(radius=0.35, start_angle=0, angle=110*DEGREES,
                           arc_center=obtuse_vertices[0], stroke_color=OMSN_BLUE, stroke_width=2.5)
        obtuse_angle2 = Arc(radius=0.3, start_angle=140*DEGREES, angle=40*DEGREES,
                           arc_center=obtuse_vertices[1], stroke_color=OMSN_RED, stroke_width=2.5)
        obtuse_angle3 = Arc(radius=0.3, start_angle=250*DEGREES, angle=30*DEGREES,
                           arc_center=obtuse_vertices[2], stroke_color=OMSN_RED, stroke_width=2.5)

        obtuse_label = Text("Obtusângulo", font_size=24, color=WHITE).next_to(obtuse, DOWN, buff=0.3)
        obtuse_group = VGroup(obtuse, obtuse_angle1, obtuse_angle2, obtuse_angle3, obtuse_label)
        obtuse_group.shift(RIGHT * 4)

        # Add all groups to scene
        self.add(acute_group, right_group, obtuse_group)
