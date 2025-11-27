from manim import *

OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"

class CilindroLight(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.set_camera_orientation(phi=65*DEGREES, theta=-50*DEGREES)

        # Create cylinder with two circular bases
        radius = 1.5
        height = 3

        # Bottom base (circle in 3D)
        bottom_circle = Circle(radius=radius, color=OMSN_RED, stroke_width=3)
        bottom_circle.rotate(90*DEGREES, axis=RIGHT)
        bottom_circle.shift(DOWN * height/2)

        # Top base (circle in 3D)
        top_circle = Circle(radius=radius, color=OMSN_BLUE, stroke_width=3)
        top_circle.rotate(90*DEGREES, axis=RIGHT)
        top_circle.shift(UP * height/2)

        # Axis connecting centers
        axis = Line(
            start=DOWN * height/2,
            end=UP * height/2,
            color=BLACK,
            stroke_width=2
        )

        # Generator lines (vertical lines on the surface)
        generators = VGroup()
        num_generators = 8
        for i in range(num_generators):
            angle = i * TAU / num_generators
            x_pos = radius * np.cos(angle)
            z_pos = radius * np.sin(angle)

            gen_line = Line(
                start=[x_pos, -height/2, z_pos],
                end=[x_pos, height/2, z_pos],
                color=BLACK,
                stroke_width=1.5,
                stroke_opacity=0.4
            )
            generators.add(gen_line)

        # Center dots
        bottom_center = Dot3D(point=DOWN * height/2, color=OMSN_RED, radius=0.06)
        top_center = Dot3D(point=UP * height/2, color=OMSN_BLUE, radius=0.06)

        # Add all elements
        self.add(bottom_circle, top_circle, generators, axis, bottom_center, top_center)


class CilindroDark(ThreeDScene):
    def construct(self):
        self.camera.background_color = BLACK
        self.set_camera_orientation(phi=65*DEGREES, theta=-50*DEGREES)

        # Create cylinder with two circular bases
        radius = 1.5
        height = 3

        # Bottom base (circle in 3D)
        bottom_circle = Circle(radius=radius, color=OMSN_RED, stroke_width=3)
        bottom_circle.rotate(90*DEGREES, axis=RIGHT)
        bottom_circle.shift(DOWN * height/2)

        # Top base (circle in 3D)
        top_circle = Circle(radius=radius, color=OMSN_BLUE, stroke_width=3)
        top_circle.rotate(90*DEGREES, axis=RIGHT)
        top_circle.shift(UP * height/2)

        # Axis connecting centers
        axis = Line(
            start=DOWN * height/2,
            end=UP * height/2,
            color=WHITE,
            stroke_width=2
        )

        # Generator lines (vertical lines on the surface)
        generators = VGroup()
        num_generators = 8
        for i in range(num_generators):
            angle = i * TAU / num_generators
            x_pos = radius * np.cos(angle)
            z_pos = radius * np.sin(angle)

            gen_line = Line(
                start=[x_pos, -height/2, z_pos],
                end=[x_pos, height/2, z_pos],
                color=WHITE,
                stroke_width=1.5,
                stroke_opacity=0.4
            )
            generators.add(gen_line)

        # Center dots
        bottom_center = Dot3D(point=DOWN * height/2, color=OMSN_RED, radius=0.06)
        top_center = Dot3D(point=UP * height/2, color=OMSN_BLUE, radius=0.06)

        # Add all elements
        self.add(bottom_circle, top_circle, generators, axis, bottom_center, top_center)
