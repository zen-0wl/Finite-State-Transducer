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
        output_str = self.transduce(list(input_str))
        return " ".join(output_str)

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
fst_info_text = Text(window, height=100, width=100)
fst_info_text.pack()

# Display the FST information in the Tkinter window
fst_info_text.insert(END, f.__str__())

# Draw the FST using networkx, pydot, and matplotlib
G = nx.DiGraph()

# Add nodes and edges to the graph
for arc_label in f.arcs():
    src_state = f.src(arc_label)
    dst_state = f.dst(arc_label)
    in_string = f.in_string(arc_label)
    out_string = f.out_string(arc_label)

    if src_state == f.initial_state:
        G.add_node(src_state, shape='circle', color='green', style='filled')
    elif f.is_final(src_state):
        G.add_node(src_state, shape='doublecircle', color='red', style='filled')
    else:
        G.add_node(src_state, shape='circle')

    label = f"{in_string}/{out_string}"
    G.add_edge(src_state, dst_state, label=label)

# Create a pydot graph from the networkx graph
pydot_graph = nx.drawing.nx_pydot.to_pydot(G)

# Save the graph to a file
graph_file_path = "fst_graph.png"
pydot_graph.write_png(graph_file_path)

# Display the saved image using PIL and IPython
img = Image.open(graph_file_path)
display(IPImage(graph_file_path))

# Run the Tkinter main loop
window.mainloop()

# Test the FST with given inputs and save the mappings in the .dat file
test_inputs = ["bēngdài", "āmóníyà", "āsīpílín", "shìduōpílí", "bèiguǒ", 
               "sāngná", "bānzhuóqín", "mǎkèbēi", "bālěi", "màikèfēng", 
               "bùlǔsī", "mǎshājī", "bāshì", "níngméng", "kāfēiyīn", 
               "jiākè", "kǎlùlǐ", "sùkèdá", "kǎtōng", "xiāngbō", "zhīshì", 
               "shìduōpílí", "qiǎokèlì", "jítā", "kāfēi", "hāní", "qǔqí", 
               "léishè", "shāfā", "nílóng", "gālí", "dīshì", "wéitāmìng", "yújiā"]

output_file_path = "Chinglish-trans.dat"

# Open the file in write mode
with open(output_file_path, 'w') as output_file:
    # Iterate through test inputs
    for input_str in test_inputs:
        # Use the recognize function to get the output
        output_str = f.recognize(input_str)
        
        # Print the mapping to the console
        print(f"{input_str} --> {output_str}")

        # Write the mapping to the output file
        output_file.write(f"{input_str} --> {output_str}\n")
