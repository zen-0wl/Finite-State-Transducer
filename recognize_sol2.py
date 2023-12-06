from nltk.nltk_contrib.fst.fst import *
from nltk.draw.util import *
from tkinter import *
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import networkx as nx
from IPython.display import Image as IPImage, display

class ChinglishFST(FST):
    def __init__(self):
        self.mapping = {i: {} for i in range(1, 5)}
        self.output_file = open("Chinglish-trans.dat", "w")

        # Tkinter window for FST construction
        self.window = Tk()
        self.window.title("Chinglish FST Construction")
        
        self.canvas = Canvas(self.window, width=800, height=400)
        self.canvas.pack()
        
        self.graph = nx.DiGraph()

    def add_syllables(self, syllables, translation):
        self.mapping[len(syllables.split())][syllables] = translation

    def get_syllables(self, syllables):
        return self.mapping[len(syllables.split())][syllables]

    def _extract_syllables(self, text):
        if len(text.split()) == 1:
            return text.strip()

        for i in range(4, 0, -1):
            for j in range(len(text.split()) - 1):
                span = ' '.join(text.split()[j:j + i])
                if span in self.mapping[i] and text.index(span) == 0:
                    return span

    def get_chains(self, text):
        chains = []

        while text:
            chain = self._extract_syllables(text)

            if chain:
                text = text.replace(chain, '', 1).strip()
                chains.append(chain)

        return chains

    def translate_chains(self, chains):
        new = []

        for chain in chains:
            new.append(self.get_syllables(chain))

        return ' '.join(new)

    def translate(self, text):
        chains = self.get_chains(text)
        result = self.translate_chains(chains)

        # Write to output file
        self.output_file.write(f"{text} --> {result}\n")

        # Update Tkinter FST construction
        self._update_fst_construction(text, result)

        return result

    def _update_fst_construction(self, input_text, output_text):
        self.graph.add_node(input_text)
        self.graph.add_node(output_text)
        self.graph.add_edge(input_text, output_text)

        pos = nx.spring_layout(self.graph)
        
        labels = {node: node for node in self.graph.nodes()}
        
        nx.draw_networkx_nodes(self.graph, pos, node_size=700, node_color='skyblue')
        nx.draw_networkx_edges(self.graph, pos, width=1.0, alpha=0.5, edge_color='gray')
        nx.draw_networkx_labels(self.graph, pos, labels, font_size=10)

        img = ImageTk.PhotoImage(Image.open("fst_graph.png"))
        self.canvas.create_image(20, 20, anchor=NW, image=img)

    def close_output_file(self):
        self.output_file.close()

# Instance of the translator
translator = ChinglishFST()

# Added syllables and translations
translator.add_syllables('ga', 'cur')
translator.add_syllables('li', 'ry')
translator.add_syllables('ka', 'ca')
translator.add_syllables('lu', 'lo')
translator.add_syllables('lu li', 'lo rie')
translator.add_syllables('wei ta ming', 'vi ta min') 
translator.add_syllables('ka fei', 'cof fee')
translator.add_syllables('beng dai', 'band age')
translator.add_syllables('a mo ni ya', 'am mo ni a')
translator.add_syllables('a si pi lin', 'a s pi rin')
translator.add_syllables('bei guo', 'ba gel') 
translator.add_syllables('ban zhuo qin', 'b an jo') 
translator.add_syllables('ba lei', 'bal let')
translator.add_syllables('bu lu si', 'b lu es') 
translator.add_syllables('ba shi', 'b us') 
translator.add_syllables('ka fei yin', 'caf fei ne')
translator.add_syllables('ka tong', 'car toon') 
translator.add_syllables('zhi shi', 'che ese') 
translator.add_syllables('qiao ke li', 'cho co late') 
translator.add_syllables('qu qi', 'coo kie') 
translator.add_syllables('sha fa', 'so fa') 
translator.add_syllables('tu si', 'toa st') 
translator.add_syllables('de lu feng', 'te le phone') 
translator.add_syllables('shi duo pi li', 'st raw ber ry')
translator.add_syllables('sang na', 'heal th') 
translator.add_syllables('ma ke bei', 'm u g') 
translator.add_syllables('mai ke feng', 'mi cro phone') 
translator.add_syllables('ma sha ji', 'mas sa ge')
translator.add_syllables('ning meng', 'le mon') 
translator.add_syllables('jia ke', 'jac ket') 
translator.add_syllables('su ke da', 'sc oo ter') 
translator.add_syllables('xiang bo', 'sham poo') 
translator.add_syllables('ji ta', 'gui tar') 
translator.add_syllables('ha ni', 'ho ney') 
translator.add_syllables('lei she', 'la ser') 
translator.add_syllables('ni long', 'ny lon') 
translator.add_syllables('di shi', 'ta xi') 
translator.add_syllables('yu jia', 'yo ga') 

# Test Inputs (Figure 1)
print(translator.translate("ga"))          # cur
print(translator.translate("li"))          # ry
print(translator.translate("ka lu li"))    # ca lo rie
print(translator.translate("wei ta ming")) # vi ta min
print(translator.translate("ka fei"))      # cof fee 
print(translator.translate("lei she"))     # la ser

# Test Inputs (Rest of all mappings)
print(translator.translate("beng dai"))    # band age
print(translator.translate("a mo ni ya"))  # am mo ni a
print(translator.translate("a si pi lin")) # a s pi rin
print(translator.translate("bei guo"))     # ba gel 
print(translator.translate("ban zhuo qin")) # b an jo
print(translator.translate("ba lei"))      # bal let
print(translator.translate("bu lu si"))    # b lu es
print(translator.translate("ba shi"))      # b us
print(translator.translate("ka fei yin"))  # caf fei ne
print(translator.translate("ka tong"))     # car toon
print(translator.translate("zhi shi"))     # che ese
print(translator.translate("qiao ke li"))  # cho co late
print(translator.translate("qu qi"))       # coo kie
print(translator.translate("sha fa"))      # so fa
print(translator.translate("tu si"))       # toa st
print(translator.translate("de lu feng"))  # te le phone
print(translator.translate("shi duo pi li"))# st raw ber ry
print(translator.translate("sang na"))      # heal th
print(translator.translate("ma ke bei"))    # m u g
print(translator.translate("mai ke feng"))  # mi cro phone
print(translator.translate("ma sha ji"))   # mas sa ge
print(translator.translate("ning meng"))   # le mon
print(translator.translate("jia ke"))      # jac ket
print(translator.translate("su ke da"))    # sc oo ter
print(translator.translate("xiang bo"))    # sham poo
print(translator.translate("ji ta"))       # gui tar
print(translator.translate("ha ni"))       # ho ney
print(translator.translate("ni long"))     # ny lon
print(translator.translate("di shi"))      # ta xi
print(translator.translate("yu jia"))      # yo ga

# Close output file
translator.close_output_file()

# Tkinter mainloop
translator.window.mainloop()