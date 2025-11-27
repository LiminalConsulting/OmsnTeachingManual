from manim import *

OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"

class ConeLight(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.set_camera_orientation(phi=70*DEGREES, theta=-60*DEGREES)

        # Create cone surface (wireframe style)
        cone = Cone(
            base_radius=1.5,
            height=2.5,
            direction=UP,
            resolution=(20, 20)
        )
        cone.set_fill(opacity=0)
        cone.set_stroke(color=BLACK, width=0.5, opacity=0.3)

        # Base circle (highlighted in red)
        base_circle = Circle(radius=1.5, color=OMSN_RED, stroke_width=4)
        base_circle.rotate(90*DEGREES, axis=RIGHT)
        base_circle.move_to([0, 0, -1.25])

        # Vertex point (apex) in blue
        vertex = Dot3D(point=[0, 0, 1.25], color=OMSN_BLUE, radius=0.1)
        vertex_label = MathTex("V", color=BLACK).scale(0.8)
        vertex_label.next_to([0, 0, 1.25], OUT + UP, buff=0.2)

        # Axis (center of base to vertex)
        axis = Line3D(
            start=[0, 0, -1.25],
            end=[0, 0, 1.25],
            color=BLACK,
            stroke_width=3
        )

        # Center of base
        base_center = Dot3D(point=[0, 0, -1.25], color=BLACK, radius=0.06)

        # Generatrices (4 lines from vertex to base circumference)
        generatrices = VGroup()
        angles = [0, 90, 180, 270]
        for angle in angles:
            rad = angle * DEGREES
            base_point = [1.5 * np.cos(rad), 1.5 * np.sin(rad), -1.25]
            gen = Line3D(
                start=[0, 0, 1.25],
                end=base_point,
                color=BLACK,
                stroke_width=2,
                stroke_opacity=0.5
            )
            generatrices.add(gen)

        # Add all elements
        self.add(cone)
        self.add(base_circle)
        self.add(axis)
        self.add(generatrices)
        self.add(vertex)
        self.add(base_center)
        self.add(vertex_label)


class ConeDark(ThreeDScene):
    def construct(self):
        self.camera.background_color = BLACK
        self.set_camera_orientation(phi=70*DEGREES, theta=-60*DEGREES)

        # Create cone surface (wireframe style)
        cone = Cone(
            base_radius=1.5,
            height=2.5,
            direction=UP,
            resolution=(20, 20)
        )
        cone.set_fill(opacity=0)
        cone.set_stroke(color=WHITE, width=0.5, opacity=0.3)

        # Base circle (highlighted in red)
        base_circle = Circle(radius=1.5, color=OMSN_RED, stroke_width=4)
        base_circle.rotate(90*DEGREES, axis=RIGHT)
        base_circle.move_to([0, 0, -1.25])

        # Vertex point (apex) in blue
        vertex = Dot3D(point=[0, 0, 1.25], color=OMSN_BLUE, radius=0.1)
        vertex_label = MathTex("V", color=WHITE).scale(0.8)
        vertex_label.next_to([0, 0, 1.25], OUT + UP, buff=0.2)

        # Axis (center of base to vertex)
        axis = Line3D(
            start=[0, 0, -1.25],
            end=[0, 0, 1.25],
            color=WHITE,
            stroke_width=3
        )

        # Center of base
        base_center = Dot3D(point=[0, 0, -1.25], color=WHITE, radius=0.06)

        # Generatrices (4 lines from vertex to base circumference)
        generatrices = VGroup()
        angles = [0, 90, 180, 270]
        for angle in angles:
            rad = angle * DEGREES
            base_point = [1.5 * np.cos(rad), 1.5 * np.sin(rad), -1.25]
            gen = Line3D(
                start=[0, 0, 1.25],
                end=base_point,
                color=WHITE,
                stroke_width=2,
                stroke_opacity=0.5
            )
            generatrices.add(gen)

        # Add all elements
        self.add(cone)
        self.add(base_circle)
        self.add(axis)
        self.add(generatrices)
        self.add(vertex)
        self.add(base_center)
        self.add(vertex_label)
