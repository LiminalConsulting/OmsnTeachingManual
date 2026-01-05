from manim import *

OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"

class CircunferenciaElementosLight(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Create circle
        circle = Circle(radius=2, stroke_color=BLACK, stroke_width=3)

        # Center point
        center = Dot(ORIGIN, color=BLACK)
        center_label = MathTex(r"\text{Centro}", color=BLACK, font_size=32)
        center_label.next_to(center, DOWN, buff=0.3)

        # Radius
        radius_end = circle.point_at_angle(PI/6)
        radius = Line(ORIGIN, radius_end, stroke_color=OMSN_RED, stroke_width=3)
        radius_label = MathTex(r"\text{Raio}", color=OMSN_RED, font_size=32)
        radius_label.next_to(radius, RIGHT, buff=0.2).shift(UP*0.2)

        # Diameter
        diameter_start = circle.point_at_angle(5*PI/6)
        diameter_end = circle.point_at_angle(-PI/6)
        diameter = Line(diameter_start, diameter_end, stroke_color=OMSN_BLUE, stroke_width=3)
        diameter_label = MathTex(r"\text{Di}\hat{\text{a}}\text{metro}", color=OMSN_BLUE, font_size=32)
        diameter_label.move_to(diameter.get_center() + UP*0.4)

        # Chord (not through center)
        chord_start = circle.point_at_angle(3*PI/4)
        chord_end = circle.point_at_angle(PI/4)
        chord = Line(chord_start, chord_end, stroke_color=BLACK, stroke_width=3)
        chord_label = MathTex(r"\text{Corda}", color=BLACK, font_size=32)
        chord_label.next_to(chord, LEFT, buff=0.2)

        # Arc
        arc = Arc(
            radius=2,
            start_angle=-5*PI/6,
            angle=PI/2,
            stroke_color=OMSN_RED,
            stroke_width=5
        )
        arc_label = MathTex(r"\text{Arco}", color=OMSN_RED, font_size=32)
        arc_label.move_to(circle.point_at_angle(-7*PI/12) + LEFT*0.8 + DOWN*0.3)

        # Add all elements
        self.add(circle)
        self.add(center, center_label)
        self.add(radius, radius_label)
        self.add(diameter, diameter_label)
        self.add(chord, chord_label)
        self.add(arc, arc_label)


class CircunferenciaElementosDark(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Create circle
        circle = Circle(radius=2, stroke_color=WHITE, stroke_width=3)

        # Center point
        center = Dot(ORIGIN, color=WHITE)
        center_label = MathTex(r"\text{Centro}", color=WHITE, font_size=32)
        center_label.next_to(center, DOWN, buff=0.3)

        # Radius
        radius_end = circle.point_at_angle(PI/6)
        radius = Line(ORIGIN, radius_end, stroke_color=OMSN_RED, stroke_width=3)
        radius_label = MathTex(r"\text{Raio}", color=OMSN_RED, font_size=32)
        radius_label.next_to(radius, RIGHT, buff=0.2).shift(UP*0.2)

        # Diameter
        diameter_start = circle.point_at_angle(5*PI/6)
        diameter_end = circle.point_at_angle(-PI/6)
        diameter = Line(diameter_start, diameter_end, stroke_color=OMSN_BLUE, stroke_width=3)
        diameter_label = MathTex(r"\text{Di}\hat{\text{a}}\text{metro}", color=OMSN_BLUE, font_size=32)
        diameter_label.move_to(diameter.get_center() + UP*0.4)

        # Chord (not through center)
        chord_start = circle.point_at_angle(3*PI/4)
        chord_end = circle.point_at_angle(PI/4)
        chord = Line(chord_start, chord_end, stroke_color=WHITE, stroke_width=3)
        chord_label = MathTex(r"\text{Corda}", color=WHITE, font_size=32)
        chord_label.next_to(chord, LEFT, buff=0.2)

        # Arc
        arc = Arc(
            radius=2,
            start_angle=-5*PI/6,
            angle=PI/2,
            stroke_color=OMSN_RED,
            stroke_width=5
        )
        arc_label = MathTex(r"\text{Arco}", color=OMSN_RED, font_size=32)
        arc_label.move_to(circle.point_at_angle(-7*PI/12) + LEFT*0.8 + DOWN*0.3)

        # Add all elements
        self.add(circle)
        self.add(center, center_label)
        self.add(radius, radius_label)
        self.add(diameter, diameter_label)
        self.add(chord, chord_label)
        self.add(arc, arc_label)
