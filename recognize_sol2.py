import tkinter as tk
import pyfst

class ChineseEnglishTransliterator(pyfst.Fst):
    def __init__(self):
        super().__init__()

        # Define states
        for i in range(40):
            self.add_state()

        self.set_start(0)
        for i in range(6, 40, 3):
            self.set_final(i)

        # Define arcs based on the provided table
        self.add_arc(0, 1, 'b', 'b')
        self.add_arc(1, 1, 'ē', 'e')
        self.add_arc(1, 1, 'n', 'n')
        self.add_arc(1, 2, 'g', 'g')
        self.add_arc(2, 2, 'd', 'd')
        self.add_arc(2, 2, 'ài', 'a')
        self.add_arc(2, 2, '#', '#')

        # Add arcs for other words based on the table...
        self.add_arc(0, 3, 'l', 'l')
        self.add_arc(3, 3, 'ě', 'e')
        self.add_arc(3, 3, 'i', 'i')
        self.add_arc(3, 4, 'g', 'g')
        self.add_arc(4, 4, 'q', 'q')
        self.add_arc(4, 4, 'í', 'i')
        self.add_arc(4, 4, '#', '#')

        self.add_arc(0, 5, 'g', 'g')
        self.add_arc(5, 5, 'a', 'a')
        self.add_arc(5, 5, '#', '#')
        self.add_arc(5, 5, 'l', 'l')
        self.add_arc(5, 5, 'i', 'i')

        # Add arcs for other words based on the table...
        self.add_arc(0, 6, 'ā', 'c')
        self.add_arc(6, 6, 'm', 'm')
        self.add_arc(6, 6, 'ó', 'o')
        self.add_arc(6, 6, 'ní', 'n')
        self.add_arc(6, 7, 'yà', 'y')
        self.add_arc(7, 7, '#', '#')

        # Add arcs for other words based on the table...
        self.add_arc(0, 8, 'ā', 'a')
        self.add_arc(8, 8, 's', 's')
        self.add_arc(8, 8, 'ī', 'i')
        self.add_arc(8, 8, 'p', 'p')
        self.add_arc(8, 8, 'l', 'l')
        self.add_arc(8, 8, 'ín', 'in')
        self.add_arc(8, 9, '#', '#')

        self.add_arc(0, 10, 'b', 'b')
        self.add_arc(10, 10, 'èi', 'ei')
        self.add_arc(10, 10, 'g', 'g')
        self.add_arc(10, 10, 'uǒ', 'uo')
        self.add_arc(10, 11, '#', '#')
        self.add_arc(11, 11, 's', 's')
        self.add_arc(11, 11, 'ī', 'i')

        # Add arcs for other words based on the table...
        self.add_arc(0, 12, 'b', 'b')
        self.add_arc(12, 12, 'ā', 'a')
        self.add_arc(12, 12, 'n', 'n')
        self.add_arc(12, 12, 'zuó', 'zuo')
        self.add_arc(12, 13, '#', '#')
        self.add_arc(13, 13, 'g', 'g')
        self.add_arc(13, 13, 'uǒ', 'uo')
        self.add_arc(13, 13, 'g', 'g')

        # Add arcs for other words based on the table...

    def arcs(self, state):
        return [(arc.nextstate, arc.ilabel, arc.olabel) for arc in self.arcs(state)]

    def recognize(self, input_syllable):
        output_transliteration = self.shortest_path(input_syllable)
        if output_transliteration:
            return ' '.join(output_transliteration)
        else:
            return None

    def get_states(self):
        return list(range(self.num_states()))

class FSTDisplay:
    def __init__(self, fst):
        self.fst = fst
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.pack()

    def draw_state(self, state):
        x, y = state * 20, 100
        self.canvas.create_oval(x, y, x + 10, y + 10, fill="white", outline="black")
        self.canvas.create_text(x + 5, y + 5, text=str(state), font=('Helvetica', 8, 'bold'))

    def draw_arc(self, from_state, to_state, label):
        x1, y1 = from_state * 20 + 10, 120
        x2, y2 = to_state * 20, 140
        self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)
        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=label, font=('Helvetica', 8))

    def display(self):
        self.window.title("FST Display")
        states = self.fst.get_states()
        for state in states:
            self.draw_state(state)
            for next_state, ilabel, olabel in self.fst.arcs(state):
                self.draw_arc(state, next_state, f"{ilabel}:{olabel}")
        self.window.mainloop()

# Create an instance of the ChineseEnglishTransliterator
transliterator = ChineseEnglishTransliterator()

# Display the FST using Tkinter
display = FSTDisplay(transliterator)
display.display()
