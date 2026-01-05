from manim import *

# OMSN Color Scheme
OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"


def build_prism(scene, stroke_color):
    """Build triangular prism geometry - shared between light/dark modes"""
    # Camera angle for good view of both bases
    scene.set_camera_orientation(phi=65 * DEGREES, theta=-50 * DEGREES)

    # Define prism vertices - prism lying on its side for clearer base visibility
    # Base 1 (left)
    A1 = np.array([-1.8, -1, -0.8])
    B1 = np.array([-1.8, 1, -0.8])
    C1 = np.array([-1.8, 0, 1.2])

    # Base 2 (right)
    A2 = np.array([1.8, -1, -0.8])
    B2 = np.array([1.8, 1, -0.8])
    C2 = np.array([1.8, 0, 1.2])

    # Base 1 edges (red)
    base1 = VGroup(
        Line3D(A1, B1, color=OMSN_RED, thickness=0.04),
        Line3D(B1, C1, color=OMSN_RED, thickness=0.04),
        Line3D(C1, A1, color=OMSN_RED, thickness=0.04),
    )

    # Base 2 edges (blue)
    base2 = VGroup(
        Line3D(A2, B2, color=OMSN_BLUE, thickness=0.04),
        Line3D(B2, C2, color=OMSN_BLUE, thickness=0.04),
        Line3D(C2, A2, color=OMSN_BLUE, thickness=0.04),
    )

    # Lateral edges
    laterals = VGroup(
        Line3D(A1, A2, color=stroke_color, thickness=0.025),
        Line3D(B1, B2, color=stroke_color, thickness=0.025),
        Line3D(C1, C2, color=stroke_color, thickness=0.025),
    )

    # Faces with transparency
    face_base1 = Polygon(A1, B1, C1, fill_color=OMSN_RED, fill_opacity=0.25, stroke_width=0)
    face_base2 = Polygon(A2, B2, C2, fill_color=OMSN_BLUE, fill_opacity=0.25, stroke_width=0)
    face_lat1 = Polygon(A1, B1, B2, A2, fill_color=stroke_color, fill_opacity=0.08, stroke_width=0)
    face_lat2 = Polygon(B1, C1, C2, B2, fill_color=stroke_color, fill_opacity=0.08, stroke_width=0)
    face_lat3 = Polygon(C1, A1, A2, C2, fill_color=stroke_color, fill_opacity=0.08, stroke_width=0)

    # Add geometry
    scene.add(face_base1, face_base2, face_lat1, face_lat2, face_lat3)
    scene.add(base1, base2, laterals)


class PrismaTriangularLight(ThreeDScene):
    """
    Light mode - Triangular prism showing parallel bases
    Grade 6: Sólidos geométricos
    """
    def construct(self):
        self.camera.background_color = WHITE
        build_prism(self, stroke_color=BLACK)


class PrismaTriangularDark(ThreeDScene):
    """
    Dark mode - Triangular prism
    """
    def construct(self):
        self.camera.background_color = BLACK
        build_prism(self, stroke_color=WHITE)
