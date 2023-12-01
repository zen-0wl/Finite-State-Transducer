import tkinter as tk
from matplotlib.pyplot import draw_all
from nltk.nltk_contrib.fst.fst import FST

class ChineseEnglishTransliterator(FST):
    def __init__(self, label):
        super().__init__(label=label)

        # Define states
        for _ in range(40):
            self.add_state()

        # Set final states
        for i in range(6, 40, 3):
            self.set_final(i)

        # Set initial state
        self.set_start(0) 

        # Defined arcs based on the provided table
        self.add_arc(0, 1, 'b', 'b')
        self.add_arc(1, 1, 'ē', 'e')
        self.add_arc(1, 1, 'n', 'n')
        self.add_arc(1, 2, 'g', 'g')
        self.add_arc(2, 2, 'd', 'd')
        self.add_arc(2, 2, 'ài', 'a')
        self.add_arc(2, 2, '#', '#')

        # Added arcs 
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

        # Added arcs 
        self.add_arc(0, 6, 'ā', 'c')
        self.add_arc(6, 6, 'm', 'm')
        self.add_arc(6, 6, 'ó', 'o')
        self.add_arc(6, 6, 'ní', 'n')
        self.add_arc(6, 7, 'yà', 'y')
        self.add_arc(7, 7, '#', '#')

        # Added arcs 
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

        # Added arcs 
        self.add_arc(0, 12, 'b', 'b')
        self.add_arc(12, 12, 'ā', 'a')
        self.add_arc(12, 12, 'n', 'n')
        self.add_arc(12, 12, 'zuó', 'zuo')
        self.add_arc(12, 13, '#', '#')
        self.add_arc(13, 13, 'g', 'g')
        self.add_arc(13, 13, 'uǒ', 'uo')
        self.add_arc(13, 13, 'g', 'g')

    

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

# Create an instance of the ChineseEnglishTransliterator
transliterator = ChineseEnglishTransliterator(label='chinese_english_transliterator')

# Define the input and output for recognition
inp = "ab##bb"
outp = "10111#"
print(inp)

# Use the recognize function defined in ChineseEnglishTransliterator
if transliterator.recognize(inp, outp):
    print(outp)
    print("accept")
else:
    print("reject")

# Displays the FST using Tkinter
class FSTDisplay:
    def __init__(self, fst):
        self.fst = fst
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.pack()

        self.draw_states()
        self.draw_arcs()

    def draw_states(self):
        for state in self.fst.get_states():
            x, y = state * 20, 100
            self.canvas.create_oval(x, y, x + 10, y + 10, fill="white", outline="black")
            self.canvas.create_text(x + 5, y + 5, text=str(state), font=('Helvetica', 8, 'bold'))

    def draw_arcs(self):
        for state in self.fst.get_states():
            for next_state, ilabel, olabel in self.fst.arcs(state):
                x1, y1 = state * 20 + 10, 120
                x2, y2 = next_state * 20, 140
                self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)
                self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=f"{ilabel}:{olabel}", font=('Helvetica', 8))

    def display(self):
        self.window.title("FST Display")
        self.window.mainloop()

# Display the FST using Tkinter
display = FSTDisplay(transliterator)
display.display()