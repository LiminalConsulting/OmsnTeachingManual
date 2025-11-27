from manim import *

OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"

class AngulosVerticalmenteOpostosLight(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Create two intersecting lines
        line1 = Line(2.5*LEFT + 1.5*DOWN, 2.5*RIGHT + 1.5*UP, stroke_color=BLACK, stroke_width=3)
        line2 = Line(2.5*LEFT + 1.5*UP, 2.5*RIGHT + 1.5*DOWN, stroke_color=BLACK, stroke_width=3)

        # Intersection point
        intersection = ORIGIN

        # Create angle arcs for vertically opposite angles
        # First pair (RED) - left and right angles
        angle1 = Arc(
            radius=0.6,
            start_angle=line2.get_angle() + PI,
            angle=line1.get_angle() - line2.get_angle(),
            arc_center=intersection,
            color=OMSN_RED,
            stroke_width=4
        )

        angle3 = Arc(
            radius=0.6,
            start_angle=line2.get_angle(),
            angle=line1.get_angle() - line2.get_angle(),
            arc_center=intersection,
            color=OMSN_RED,
            stroke_width=4
        )

        # Second pair (BLUE) - top and bottom angles
        angle2 = Arc(
            radius=0.8,
            start_angle=line1.get_angle(),
            angle=line2.get_angle() - line1.get_angle() + PI,
            arc_center=intersection,
            color=OMSN_BLUE,
            stroke_width=4
        )

        angle4 = Arc(
            radius=0.8,
            start_angle=line1.get_angle() + PI,
            angle=line2.get_angle() - line1.get_angle() + PI,
            arc_center=intersection,
            color=OMSN_BLUE,
            stroke_width=4
        )

        # Add angle labels
        alpha = MathTex(r"\alpha", color=OMSN_RED).scale(0.8)
        alpha.move_to(1.2*RIGHT + 0.3*UP)

        alpha_prime = MathTex(r"\alpha", color=OMSN_RED).scale(0.8)
        alpha_prime.move_to(1.2*LEFT + 0.3*DOWN)

        beta = MathTex(r"\beta", color=OMSN_BLUE).scale(0.8)
        beta.move_to(0.3*LEFT + 1.0*UP)

        beta_prime = MathTex(r"\beta", color=OMSN_BLUE).scale(0.8)
        beta_prime.move_to(0.3*RIGHT + 1.0*DOWN)

        # Add all objects
        self.add(line1, line2)
        self.add(angle1, angle2, angle3, angle4)
        self.add(alpha, alpha_prime, beta, beta_prime)


class AngulosVerticalmenteOpostosDark(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Create two intersecting lines
        line1 = Line(2.5*LEFT + 1.5*DOWN, 2.5*RIGHT + 1.5*UP, stroke_color=WHITE, stroke_width=3)
        line2 = Line(2.5*LEFT + 1.5*UP, 2.5*RIGHT + 1.5*DOWN, stroke_color=WHITE, stroke_width=3)

        # Intersection point
        intersection = ORIGIN

        # Create angle arcs for vertically opposite angles
        # First pair (RED) - left and right angles
        angle1 = Arc(
            radius=0.6,
            start_angle=line2.get_angle() + PI,
            angle=line1.get_angle() - line2.get_angle(),
            arc_center=intersection,
            color=OMSN_RED,
            stroke_width=4
        )

        angle3 = Arc(
            radius=0.6,
            start_angle=line2.get_angle(),
            angle=line1.get_angle() - line2.get_angle(),
            arc_center=intersection,
            color=OMSN_RED,
            stroke_width=4
        )

        # Second pair (BLUE) - top and bottom angles
        angle2 = Arc(
            radius=0.8,
            start_angle=line1.get_angle(),
            angle=line2.get_angle() - line1.get_angle() + PI,
            arc_center=intersection,
            color=OMSN_BLUE,
            stroke_width=4
        )

        angle4 = Arc(
            radius=0.8,
            start_angle=line1.get_angle() + PI,
            angle=line2.get_angle() - line1.get_angle() + PI,
            arc_center=intersection,
            color=OMSN_BLUE,
            stroke_width=4
        )

        # Add angle labels
        alpha = MathTex(r"\alpha", color=OMSN_RED).scale(0.8)
        alpha.move_to(1.2*RIGHT + 0.3*UP)

        alpha_prime = MathTex(r"\alpha", color=OMSN_RED).scale(0.8)
        alpha_prime.move_to(1.2*LEFT + 0.3*DOWN)

        beta = MathTex(r"\beta", color=OMSN_BLUE).scale(0.8)
        beta.move_to(0.3*LEFT + 1.0*UP)

        beta_prime = MathTex(r"\beta", color=OMSN_BLUE).scale(0.8)
        beta_prime.move_to(0.3*RIGHT + 1.0*DOWN)

        # Add all objects
        self.add(line1, line2)
        self.add(angle1, angle2, angle3, angle4)
        self.add(alpha, alpha_prime, beta, beta_prime)
