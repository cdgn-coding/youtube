from manim import *
import sys
from manim import config
from manim.__main__ import main
import os

class Animation(Scene):
    def construct(self):
        # Crear un mensaje de bienvenida
        welcome_text = Text("¡Bienvenido a Manim!", font_size=48).to_edge(UP)

        # Crear la cinta de Möbius
        mobius_strip = Surface(
            lambda u, v: np.array([
                (1 + 0.5 * v * np.cos(u / 2)) * np.cos(u),
                (1 + 0.5 * v * np.cos(u / 2)) * np.sin(u),
                0.5 * v * np.sin(u / 2)
            ]),
            u_range=[0, TAU],
            v_range=[-1, 1],
            checkerboard_colors=[BLUE_E, BLUE_D],
            resolution=(50, 10)
        )
        mobius_strip.scale(2)

        # Animar el mensaje de bienvenida
        self.play(Write(welcome_text))
        self.wait(1)

        # Mostrar la cinta de Möbius con rotación
        self.play(FadeIn(mobius_strip, shift=DOWN))
        self.play(Rotate(mobius_strip, angle=PI, axis=UP, run_time=4))
        self.wait(2)

        # Despedida
        goodbye_text = Text("¡Vamos a crear algo increíble!", font_size=36).to_edge(DOWN)
        self.play(Write(goodbye_text))
        self.wait(2)

if __name__ == "__main__":
    # Get the current file name dynamically
    current_file = os.path.abspath(__file__)

    # Check for quality parameter
    quality = sys.argv[1] if len(sys.argv) > 1 else "low"
    quality_flag = "-pql" if quality == "low" else "-pqh"

    # Configure settings
    config.media_dir = "./media"

    # Set sys.argv to run the animation with the current file name
    sys.argv = ["manim", current_file, "Animation", quality_flag]
    main()