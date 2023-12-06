## produces graph + mapping content but in nltk window (not in .dat) 
from nltk.nltk_contrib.fst.fst import *  
from tkinter import *
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import networkx as nx
import pydotplus 
import pydot
from IPython.display import Image as IPImage, display
import codecs

class ChinglishFST(FST):
    def recognize(self, input_str):
        # Use the transduce function to get the output for the entire input
        output = self.transduce(list(input_str.split()))

        return output
    
    def transduce(self, input_str):
        """
        Transduce the input Pinyin string to English.
        """
        current_state = self.initial_state
        output_str = []

        for symbol in input_str:
            # Find the outgoing arc for the current state and input symbol
            outgoing_arcs = self._outgoing.get(current_state, [])
            possible_arcs = []

        for arc in outgoing_arcs:
            # Check if the input symbol matches the Pinyin symbol in the arc
            if symbol == self._in_string[arc][0]:
                possible_arcs.append(arc)

        if not possible_arcs:
            # If no matching arc is found, print debug information
            print(f"No matching arc for symbol '{symbol}' in state {current_state}")
            print(f"Current state: {current_state}")
            print(f"Input string: {' '.join(input_str)}")
            print(f"Output string so far: {''.join(output_str)}")
            return None
        
        # If there are multiple possible arcs, choose the one with the longest input string
        chosen_arc = max(possible_arcs, key=lambda arc: len(self._in_string[arc]))

        # Update the current state and output string
        current_state = self._dst[chosen_arc]
        output_str.extend(self._out_string[chosen_arc])
        
        # After processing the entire input, update the current state
        self.initial_state = current_state

        return ''.join(output_str)
    
# Define the states and transitions
f = ChinglishFST('chinglish_transliteration')
state_labels = {}

# Function to add state and return the label
def add_state(label):
    state_labels[label] = True
    f.add_state(label)
    return label

# Added arcs | Mapping of Pinyin to English Loan Word
f.add_arc(add_state('1'), add_state('2'), ('beng', 'dai'), ('band', 'age'))
f.add_arc(add_state('3'), add_state('4'), ('amo', 'niya'), ('ammo', 'nia'))
f.add_arc(add_state('5'), add_state('6'), ('asi', 'pi', 'lin'), ('as', 'pi', 'rin'))
f.add_arc(add_state('7'), add_state('8'), ('shi', 'duo', 'pi', 'li'), ('straw', 'ber', 'ry'))
f.add_arc(add_state('9'), add_state('10'), ('bei', 'guo'), ('ba', 'gel'))
f.add_arc(add_state('11'), add_state('12'), ('sang', 'na'), ('hea', 'lth'))
f.add_arc(add_state('13'), add_state('14'), ('banz', 'huo', 'qin'), ('ban', 'jo'))
f.add_arc(add_state('15'), add_state('16'), ('ma', 'ke', 'bei'), ('mu', 'g'))
f.add_arc(add_state('17'), add_state('18'), ('ba', 'lei'), ('bal', 'let'))
f.add_arc(add_state('19'), add_state('20'), ('mai', 'ke', 'feng'), ('mi', 'cro', 'phone'))
f.add_arc(add_state('21'), add_state('22'), ('bu', 'lu', 'si'), ('b', 'lu', 'es'))
f.add_arc(add_state('23'), add_state('24'), ('ma', 'sha', 'ji'), ('mas', 'sage'))
f.add_arc(add_state('25'), add_state('26'), ('ba', 'shi'), ('b', 'us'))
f.add_arc(add_state('27'), add_state('28'), ('ning', 'meng'), ('le', 'mon'))
f.add_arc(add_state('29'), add_state('30'), ('ka', 'fei', 'yin'), ('caf', 'fei', 'ne'))
f.add_arc(add_state('31'), add_state('32'), ('jia', 'ke'), ('jac', 'ket'))
f.add_arc(add_state('33'), add_state('34'), ('ka', 'lu', 'li'), ('ca', 'lo', 'rie'))
f.add_arc(add_state('35'), add_state('36'), ('su', 'ke', 'da'), ('scoo', 'ter'))
f.add_arc(add_state('37'), add_state('38'), ('ka', 'tong'), ('car', 'toon'))
f.add_arc(add_state('39'), add_state('40'), ('xiang', 'bo'), ('sham', 'poo'))
f.add_arc(add_state('41'), add_state('42'), ('zhi', 'shi'), ('che', 'ese'))
f.add_arc(add_state('43'), add_state('44'), ('shi', 'duo', 'pi', 'li'), ('straw', 'ber', 'ry'))
f.add_arc(add_state('45'), add_state('46'), ('qiao', 'ke', 'li'), ('cho', 'co', 'late'))
f.add_arc(add_state('47'), add_state('48'), ('ji', 'ta'), ('gui', 'tar'))
f.add_arc(add_state('49'), add_state('50'), ('ka', 'fei'), ('cof', 'fee'))
f.add_arc(add_state('51'), add_state('52'), ('ha', 'ni'), ('ho', 'ney'))
f.add_arc(add_state('53'), add_state('54'), ('qu', 'qi'), ('coo', 'kie'))
f.add_arc(add_state('55'), add_state('56'), ('lei', 'she'), ('la', 'ser'))
f.add_arc(add_state('57'), add_state('58'), ('sha', 'fa'), ('so', 'fa'))
f.add_arc(add_state('59'), add_state('60'), ('ni', 'long'), ('ny', 'lon'))
f.add_arc(add_state('61'), add_state('62'), ('ga', 'li'), ('cur', 'ry'))
f.add_arc(add_state('63'), add_state('64'), ('di', 'shi'), ('ta', 'xi'))
f.add_arc(add_state('65'), add_state('66'), ('wei', 'ta', 'ming'), ('vi', 'ta', 'min'))
f.add_arc(add_state('67'), add_state('68'), ('yu', 'jia'), ('yo', 'ga'))

# Set the initial state and final state
f.initial_state = '1'
f.set_final('68')

# Tkinter window for FST construction
window = Tk()
window.title("FST Construction")

# Text widget to display FST information
fst_info_text = Text(window, height=80, width=90)
fst_info_text.pack()

# Display the FST information in the Tkinter window
fst_info_text.insert(END, f.__str__())

# Draw the FST using networkx and matplotlib
G = nx.DiGraph()

for state in f.states():
    for arc_label in f._outgoing[state]:
        source = state
        target = f._dst[arc_label]
        input_str = f._in_string[arc_label]
        output_str = f._out_string[arc_label]
        G.add_edge(source, target, label=f"{input_str} / {output_str}")
    
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue', node_size=1500, font_size=8, arrowsize=20)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Save the graph to a file
graph_file_path = "fst_graph.png"
plt.savefig(graph_file_path)
plt.show()

# Display the saved image using PIL and IPython
img = Image.open(graph_file_path)
display(IPImage(graph_file_path))

# Run the Tkinter main loop
window.mainloop()

# Tests FST with given inputs and save mappings in the .dat file
test_inputs = ["ga li", "ka lu li", "wei ta ming", "ka fei", "lei she", "beng dai", "ha ni", "amo niya"]

output_file_path = "Chinglish-trans.dat"

# Opens file in write mode
with open(output_file_path, 'w') as output_file:
    # Iterate through test inputs
    for input_str in test_inputs:
        # Uses the recognize function to get the output for the entire input
        output = f.recognize(input_str)

        # Writes the entire input and its English output to the .dat file
        output_file.write(f"{input_str} --> {output}\n")

        # Displays the test input and its recognition result in the nltk window
        result = output if output else "None"
        print(f"Test Input: {input_str} \t {result}")