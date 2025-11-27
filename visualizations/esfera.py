from manim import *

OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"

class EsferaLight(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.set_camera_orientation(phi=65*DEGREES, theta=-50*DEGREES)

        # Create sphere
        sphere = Sphere(radius=2, resolution=(30, 30))
        sphere.set_color(OMSN_BLUE)
        sphere.set_opacity(0.3)
        sphere.set_stroke(BLACK, width=0.5)

        # Center point
        center = Dot3D(point=ORIGIN, color=BLACK, radius=0.08)
        center_label = MathTex("O", color=BLACK).scale(0.8)
        center_label.move_to(ORIGIN + 0.3*DOWN + 0.3*LEFT)

        # Radius line
        radius_end = np.array([2, 0, 0])
        radius_line = Line3D(start=ORIGIN, end=radius_end, color=OMSN_RED, thickness=0.03)

        # Point on surface
        surface_point = Dot3D(point=radius_end, color=BLACK, radius=0.08)

        # Radius label
        radius_label = MathTex("r", color=OMSN_RED).scale(0.8)
        radius_label.move_to(np.array([1, 0, 0]) + 0.4*DOWN)

        # Add reference circle (equator)
        equator = Circle(radius=2, color=BLACK, stroke_width=2)
        equator.rotate(90*DEGREES, axis=RIGHT)

        # Add all objects
        self.add(sphere, equator, center, radius_line, surface_point, center_label, radius_label)


class EsferaDark(ThreeDScene):
    def construct(self):
        self.camera.background_color = BLACK
        self.set_camera_orientation(phi=65*DEGREES, theta=-50*DEGREES)

        # Create sphere
        sphere = Sphere(radius=2, resolution=(30, 30))
        sphere.set_color(OMSN_BLUE)
        sphere.set_opacity(0.3)
        sphere.set_stroke(WHITE, width=0.5)

        # Center point
        center = Dot3D(point=ORIGIN, color=WHITE, radius=0.08)
        center_label = MathTex("O", color=WHITE).scale(0.8)
        center_label.move_to(ORIGIN + 0.3*DOWN + 0.3*LEFT)

        # Radius line
        radius_end = np.array([2, 0, 0])
        radius_line = Line3D(start=ORIGIN, end=radius_end, color=OMSN_RED, thickness=0.03)

        # Point on surface
        surface_point = Dot3D(point=radius_end, color=WHITE, radius=0.08)

        # Radius label
        radius_label = MathTex("r", color=OMSN_RED).scale(0.8)
        radius_label.move_to(np.array([1, 0, 0]) + 0.4*DOWN)

        # Add reference circle (equator)
        equator = Circle(radius=2, color=WHITE, stroke_width=2)
        equator.rotate(90*DEGREES, axis=RIGHT)

        # Add all objects
        self.add(sphere, equator, center, radius_line, surface_point, center_label, radius_label)
