from manim import *

OMSN_RED = "#FF644E"
OMSN_BLUE = "#00A2FF"

class ClassificacaoAngulosLight(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Create five angle examples arranged in a grid
        angles_data = [
            ("Agudo", 45, 0),
            ("Reto", 90, 1),
            ("Obtuso", 135, 2),
            ("Raso", 180, 3),
            ("Giro", 360, 4)
        ]

        angle_groups = VGroup()

        for name, degrees, idx in angles_data:
            # Create angle at origin
            radius = 0.8

            # Start ray (horizontal to the right)
            start_ray = Line(ORIGIN, RIGHT * radius, stroke_color=BLACK, stroke_width=3)

            # End ray (rotated by the angle)
            angle_rad = degrees * DEGREES
            end_point = RIGHT * radius
            end_point = np.array([
                np.cos(angle_rad) * radius,
                np.sin(angle_rad) * radius,
                0
            ])
            end_ray = Line(ORIGIN, end_point, stroke_color=BLACK, stroke_width=3)

            # Arc to show the angle
            if degrees == 360:
                # For full angle, draw a complete circle
                arc = Circle(radius=radius * 0.3, stroke_color=OMSN_BLUE, stroke_width=2.5)
            else:
                arc = Arc(
                    radius=radius * 0.3,
                    start_angle=0,
                    angle=angle_rad,
                    stroke_color=OMSN_BLUE,
                    stroke_width=2.5
                )

            # Label with angle name and degree measure
            label_text = Text(name, font_size=20, color=BLACK, weight=BOLD)
            degree_text = Text(f"{degrees}°", font_size=18, color=BLACK)

            # Position labels below the angle
            label_text.next_to(ORIGIN, DOWN, buff=0.5)
            degree_text.next_to(label_text, DOWN, buff=0.1)

            # Group all elements
            angle_group = VGroup(start_ray, end_ray, arc, label_text, degree_text)

            angle_groups.add(angle_group)

        # Arrange in a row with spacing
        angle_groups.arrange(RIGHT, buff=1.2)

        # Scale to fit nicely
        angle_groups.scale(0.85)

        self.add(angle_groups)


class ClassificacaoAngulosDark(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Create five angle examples arranged in a grid
        angles_data = [
            ("Agudo", 45, 0),
            ("Reto", 90, 1),
            ("Obtuso", 135, 2),
            ("Raso", 180, 3),
            ("Giro", 360, 4)
        ]

        angle_groups = VGroup()

        for name, degrees, idx in angles_data:
            # Create angle at origin
            radius = 0.8

            # Start ray (horizontal to the right)
            start_ray = Line(ORIGIN, RIGHT * radius, stroke_color=WHITE, stroke_width=3)

            # End ray (rotated by the angle)
            angle_rad = degrees * DEGREES
            end_point = RIGHT * radius
            end_point = np.array([
                np.cos(angle_rad) * radius,
                np.sin(angle_rad) * radius,
                0
            ])
            end_ray = Line(ORIGIN, end_point, stroke_color=WHITE, stroke_width=3)

            # Arc to show the angle
            if degrees == 360:
                # For full angle, draw a complete circle
                arc = Circle(radius=radius * 0.3, stroke_color=OMSN_BLUE, stroke_width=2.5)
            else:
                arc = Arc(
                    radius=radius * 0.3,
                    start_angle=0,
                    angle=angle_rad,
                    stroke_color=OMSN_BLUE,
                    stroke_width=2.5
                )

            # Label with angle name and degree measure
            label_text = Text(name, font_size=20, color=WHITE, weight=BOLD)
            degree_text = Text(f"{degrees}°", font_size=18, color=WHITE)

            # Position labels below the angle
            label_text.next_to(ORIGIN, DOWN, buff=0.5)
            degree_text.next_to(label_text, DOWN, buff=0.1)

            # Group all elements
            angle_group = VGroup(start_ray, end_ray, arc, label_text, degree_text)

            angle_groups.add(angle_group)

        # Arrange in a row with spacing
        angle_groups.arrange(RIGHT, buff=1.2)

        # Scale to fit nicely
        angle_groups.scale(0.85)

        self.add(angle_groups)
