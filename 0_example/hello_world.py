from manim import *
from manim import *
import sys
from manim import config
from manim.__main__ import main
import os

class Animation(Scene):
    def construct(self):
        text = Text("Hello, World!")
        self.play(Write(text))
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