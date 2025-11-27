from manim import *

OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"

class PiramideLight(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.set_camera_orientation(phi=65*DEGREES, theta=-50*DEGREES)

        # Define base vertices (square base)
        base_vertices = [
            np.array([-1, -1, 0]),
            np.array([1, -1, 0]),
            np.array([1, 1, 0]),
            np.array([-1, 1, 0])
        ]

        # Define apex
        apex = np.array([0, 0, 2.5])

        # Create base polygon with OMSN_RED
        base_edges = VGroup()
        for i in range(len(base_vertices)):
            edge = Line3D(
                base_vertices[i],
                base_vertices[(i + 1) % len(base_vertices)],
                color=OMSN_RED,
                stroke_width=4
            )
            base_edges.add(edge)

        # Create lateral edges from base to apex with OMSN_BLUE
        lateral_edges = VGroup()
        for vertex in base_vertices:
            edge = Line3D(
                vertex,
                apex,
                color=OMSN_BLUE,
                stroke_width=4
            )
            lateral_edges.add(edge)

        # Create dots for vertices
        base_dots = VGroup(*[
            Dot3D(point=v, color=BLACK, radius=0.08)
            for v in base_vertices
        ])
        apex_dot = Dot3D(point=apex, color=BLACK, radius=0.08)

        # Add labels
        base_label = MathTex("\\text{Base}", color=BLACK, font_size=36).to_corner(DL).shift(RIGHT*0.5 + UP*0.5)
        apex_label = MathTex("V", color=BLACK, font_size=36).move_to(apex).shift(UP*0.3 + RIGHT*0.3)

        # Assemble pyramid
        pyramid = VGroup(base_edges, lateral_edges, base_dots, apex_dot)

        self.add(pyramid)
        self.add_fixed_in_frame_mobjects(base_label)
        self.add_fixed_orientation_mobjects(apex_label)


class PiramideDark(ThreeDScene):
    def construct(self):
        self.camera.background_color = BLACK
        self.set_camera_orientation(phi=65*DEGREES, theta=-50*DEGREES)

        # Define base vertices (square base)
        base_vertices = [
            np.array([-1, -1, 0]),
            np.array([1, -1, 0]),
            np.array([1, 1, 0]),
            np.array([-1, 1, 0])
        ]

        # Define apex
        apex = np.array([0, 0, 2.5])

        # Create base polygon with OMSN_RED
        base_edges = VGroup()
        for i in range(len(base_vertices)):
            edge = Line3D(
                base_vertices[i],
                base_vertices[(i + 1) % len(base_vertices)],
                color=OMSN_RED,
                stroke_width=4
            )
            base_edges.add(edge)

        # Create lateral edges from base to apex with OMSN_BLUE
        lateral_edges = VGroup()
        for vertex in base_vertices:
            edge = Line3D(
                vertex,
                apex,
                color=OMSN_BLUE,
                stroke_width=4
            )
            lateral_edges.add(edge)

        # Create dots for vertices
        base_dots = VGroup(*[
            Dot3D(point=v, color=WHITE, radius=0.08)
            for v in base_vertices
        ])
        apex_dot = Dot3D(point=apex, color=WHITE, radius=0.08)

        # Add labels
        base_label = MathTex("\\text{Base}", color=WHITE, font_size=36).to_corner(DL).shift(RIGHT*0.5 + UP*0.5)
        apex_label = MathTex("V", color=WHITE, font_size=36).move_to(apex).shift(UP*0.3 + RIGHT*0.3)

        # Assemble pyramid
        pyramid = VGroup(base_edges, lateral_edges, base_dots, apex_dot)

        self.add(pyramid)
        self.add_fixed_in_frame_mobjects(base_label)
        self.add_fixed_orientation_mobjects(apex_label)
