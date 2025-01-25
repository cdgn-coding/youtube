from manim import *

"""
1. Agrega una cita de una persona sobre la computación

2. Un símbolo de archivo con bordes verdes y dentro escrito .py para representar un programa. El símbolo de archivo es parecido a un ícono, como un rectángulo pequeño con bordes redondeados.

3. Aparece un programa de hola mundo en python con una flecha hacia el símbolo de archivo. Representa que el contenido del archivo es un programa "Hola Mundo".

4. Aparece el programa de Hola mundo de nuevo, mas grande, sin el simbolo de archivo y se transforma en 1s y 0s

5. Aparece un simbolo de un procesador, como un ícono vectorial y dentro dice CPU

6. Los 1s y 0s se mueven hacia el CPU uno a uno como si fueran bufferizados, una vez que colisionan con la CPU, desaparece el digito binario

7. Aparece un una ventana que dice hola mundo y una flecha desde el CPU hacia ella

8. Luego, se queda solo la pantalla con el mensaje y se ve mas grande
"""

class Intro(Scene):
    def construct(self):
        #self.show_quote()
        self.show_file_and_program()
        self.show_binary_transformation()
        # self.show_cpu_processing()
        # self.show_final_output()

    def show_quote(self):
        quote_line1 = Text(
            '"La computación no es sobre computadoras,',
            font_size=36,
            slant=ITALIC
        ).move_to(UP * 0.5)
        
        quote_line2 = Text(
            'más que la astronomía es sobre telescopios"',
            font_size=36,
            slant=ITALIC
        )
        
        author = Text(
            "- Edsger Dijkstra",
            font_size=32
        ).next_to(quote_line2, DOWN).align_on_border(RIGHT, buff=1)
        
        quote_group = VGroup(quote_line1, quote_line2, author)
        
        self.play(Write(quote_group))
        self.wait(6)
        self.play(FadeOut(quote_group))

    def create_file_symbol(self):
        # Create the main file rectangle
        file_symbol = RoundedRectangle(corner_radius=0.2, width=2.5, height=3, color=GREEN)
        
        # Create lines representing content
        start_y = file_symbol.get_top()[1] - 0.5
        lines = VGroup()
        
        # Calculate vertical spacing to evenly distribute lines
        total_height = file_symbol.height - 1  # Leave some padding
        num_lines = 6  # Change this value to test different numbers of lines
        spacing = total_height / (num_lines - 1)  # Evenly space between lines
        
        for i in range(num_lines):
            line_width = np.random.uniform(1.0, 1.8)  # Random width for variety
            start_point = file_symbol.get_left() + RIGHT * 0.3  # Start from left with small padding
            line = Line(
                start_point,
                start_point + RIGHT * line_width,
                color=GREEN_C,
                stroke_width=2
            ).move_to([0, start_y - i*spacing, 0])
            lines.add(line)
        # Add the lines to the file symbol
        file_content = VGroup(file_symbol, lines)
        
        # Add the filename text
        py_text = Text("program.py", font_size=24).move_to(file_symbol.get_bottom() + DOWN * 0.5)
        
        # Group everything and position
        return VGroup(file_content, py_text).move_to(LEFT * 3)


    def show_file_and_program(self):
        # Define multiple program examples with proper formatting
        programs = [
            'print("Hola Mundo")',
            '''for i in range(5):
    print(i)''',
            '''def sum(a, b):
    return a + b

print(sum(2, 3))'''
        ]
        
        # Show each program sequentially
        for i, program in enumerate(programs):
            program_text = Code(
                code_string=program,
                language="python",
                add_line_numbers=False,
                background="rectangle",
                formatter_style="one-dark",
            ).move_to(ORIGIN)  # Center the code examples
            
            if i == 0:
                self.play(Write(program_text))
                old_program = program_text
            else:
                self.play(ReplacementTransform(old_program, program_text))
                self.wait(2)
                old_program = program_text
        
        # Final fadeout
        self.play(FadeOut(old_program))

    def show_binary_transformation(self):
        # Limpiar escena anterior
        self.clear()
        
        # Crear y mostrar programa ampliado
        program = VGroup(
            Text('print(', font_size=54, color="#E5C07B"),  # One Dark mustard yellow for function
            Text('"Hola Mundo"', font_size=54, color="#98C379"),  # One Dark pale green for strings
            Text(')', font_size=54, color=WHITE)
        ).arrange(RIGHT, buff=0).move_to(ORIGIN)
        
        # Format binary in multiple lines con color
        binary_text = """01001000 01101111 
01100001 00100000 
01110101 01101110 
01101111 01100100"""

        binary = Text(
            binary_text,
            font_size=36,
            line_spacing=1.5,
            font="Monospace",
            color=BLUE_B  # Añadimos color al 
        ).move_to(ORIGIN)
        
        self.play(Write(program))
        self.wait(1)
        self.play(Transform(program, binary))
        self.wait(1)
        
        # Definir posiciones específicas usando el ancho de la pantalla
        left_pos = LEFT * 4  # Ajustado de 3 a 4 para más separación
        right_pos = RIGHT * 4  # Ajustado de 3 a 4 para más separación
        
        # Mover el binario a la izquierda manteniendo su tamaño
        self.play(
            program.animate.move_to(left_pos),
            run_time=1
        )
        self.wait(1)
        
        # Crear y mostrar CPU usando SVG, ahora con color
        cpu_svg = SVGMobject(
            "assets/cpu.svg",
            stroke_width=2.5,
            fill_opacity=0.2,  # Añadimos un poco de opacidad al relleno
            stroke_color=GREEN_A,  # Color del borde
            fill_color=GREEN_D    # Color del relleno
        ).scale(1.5).move_to(right_pos)
        
        self.play(FadeIn(cpu_svg))
        self.wait(0.5)
        
        # Crear flecha punteada con gradiente de color
        arrow = DashedLine(
            start=program.get_right() + RIGHT * 0.5,
            end=cpu_svg.get_left() + LEFT * 0.5,
            dash_length=0.15,
            dashed_ratio=0.5,
            stroke_width=2,
            color=WHITE  # Color de la flecha
        ).add_tip(tip_length=0.2)
        
        # Calcular el centro exacto de la pantalla
        center_point = ORIGIN + RIGHT * 0.5  # Movemos el centro medio punto a la derecha
        
        # Ajustar la posición de la flecha para que esté exactamente centrada
        arrow_center = arrow.get_center()
        arrow.shift(center_point - arrow_center)
        
        self.play(Create(arrow))
        self.wait(1)
        
        return binary

    def create_cpu_symbol(self):
        cpu_symbol = RoundedRectangle(corner_radius=0.2, width=2, height=2, color=WHITE)
        cpu_label = Text("CPU", font_size=24, font="Monospace").move_to(cpu_symbol.get_center())
        return VGroup(cpu_symbol, cpu_label).move_to(RIGHT * 3)

    def show_cpu_processing(self):
        cpu_group = self.create_cpu_symbol()
        binary_stream = Text(
            "01001000 01101111",  # Versión reducida para la animación
            font_size=24
        ).scale(0.5).move_to(LEFT * 3)
        
        self.play(Create(cpu_group))
        self.play(Write(binary_stream))
        
        # Animación de procesamiento
        for _ in range(3):  # Reducido a 3 iteraciones para ejemplo
            digit = binary_stream[0].copy()
            self.play(
                digit.animate.move_to(cpu_group.get_center()),
                FadeOut(digit),
                run_time=0.5
            )
        
        return cpu_group

    def create_output_window(self):
        window = RoundedRectangle(corner_radius=0.2, width=5, height=2.5, color=WHITE)
        hello_text = Text("Hola Mundo", font_size=36).move_to(window.get_center())
        return VGroup(window, hello_text).move_to(UP * 2)

    def show_final_output(self):
        window_group = self.create_output_window()
        cpu_group = self.create_cpu_symbol()
        
        arrow = Arrow(cpu_group.get_top(), window_group.get_bottom(), buff=0.2)
        
        self.play(
            Create(window_group),
            Create(arrow)
        )
        self.wait(2)
        
        # Escena final
        self.play(
            FadeOut(cpu_group),
            FadeOut(arrow),
            window_group.animate.scale(1.5).move_to(ORIGIN)
        )
        self.wait(3)
