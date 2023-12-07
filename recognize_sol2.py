from nltk.nltk_contrib.fst.fst import *
from nltk.draw import * 
from tkinter import *

class ChinglishFST(FST):
    def __init__(self, name):
        super().__init__(name)
        self.mappings = []

    def add_arc(self, from_state, to_state, in_symbol, out_symbol):
        super().add_arc(from_state, to_state, in_symbol, out_symbol)
        # Keep track of mappings
        mapping = f"{(in_symbol)} --> {(out_symbol)}"
        self.mappings.append(mapping)

    def write_mappings_to_file(self, filename):
        with open(filename, 'w') as file:
            for mapping in self.mappings:
                file.write(f"{mapping}\n")
                
    def recognize(self, inp, outp):
        # transduced_output = self.transduce(inp)

        # # tranduced output matches expected output 
        # return transduced_output == outp
        self.inp = list(inp) 
        self.outp = list(outp)
        
        if list(outp) == self.transduce(list(inp)):
            print(" ".join(f.transduce(inp.split())))        
            return True
        else:
            return False

# Defines FST
f = ChinglishFST('chinglish-transliterations')

# Adds the states in the FST
for i in range(1,79):
    f.add_state(str(i)) 
    
# Initial state
f.initial_state = '1' # -> 1
    
# Added all transitions 
f.add_arc('1', '2', ('ga'), ('cur'))
f.add_arc('3', '4', ('li'), ('ry'))
f.add_arc('5', '6', ('ka'), ('ca'))
f.add_arc('7', '8', ('lu'), ('lo'))
f.add_arc('9', '10', ('lu li'), ('lo rie'))
f.add_arc('11', '12', ('wei ta ming'), ('vi ta min')) 
f.add_arc('13', '14', ('ka fei'), ('cof fee'))
f.add_arc('15', '16', ('beng dai'), ('band age'))
f.add_arc('17', '18',('a mo ni ya'), ('am mo ni a'))
f.add_arc('19', '20', ('a si pi lin'), ('a s pi rin'))
f.add_arc('21', '22', ('bei guo'), ('ba gel')) 
f.add_arc('23', '24', ('ban zhuo qin'), ('b an jo')) 
f.add_arc('25', '26', ('ba lei'), ('ba llet'))
f.add_arc('27', '28', ('bu lu si'), ('b lu es')) 
f.add_arc('29', '30', ('ba shi'), ('b us'))
f.add_arc('31', '32', ('ka fei yin'), ('caf fei ne'))
f.add_arc('33', '34', ('ka tong'), ('car toon')) 
f.add_arc('35', '36', ('zhi shi'), ('che ese')) 
f.add_arc('37', '38', ('qiao ke li'), ('cho co late'))
f.add_arc('39', '40', ('qu qi'), ('coo kie')) 
f.add_arc('41', '42', ('sha fa'), ('so fa')) 
f.add_arc('43', '44', ('tu si'), ('toa st')) 
f.add_arc('45', '46', ('de lu feng'), ('te le phone')) 
f.add_arc('47', '48', ('shi duo pi li'), ('st raw ber ry'))
f.add_arc('49', '50', ('sang na'), ('heal th')) 
f.add_arc('51', '52', ('ma ke bei'), ('m u g')) 
f.add_arc('53', '54', ('mai ke feng'), ('mi cro phone')) 
f.add_arc('55', '56', ('ma sha ji'), ('mas sa ge'))
f.add_arc('57', '58', ('ning meng'), ('le mon')) 
f.add_arc('59', '60', ('jia ke'), ('jac ket')) 
f.add_arc('61', '62', ('su ke da'), ('sc oo ter')) 
f.add_arc('63', '64', ('xiang bo'), ('sham poo')) 
f.add_arc('65', '66', ('ji ta'), ('gui tar')) 
f.add_arc('67', '68', ('ha ni'), ('ho ney')) 
f.add_arc('69', '70', ('lei she'), ('la ser')) 
f.add_arc('71', '72', ('ni long'), ('ny lon')) 
f.add_arc('73', '74', ('di shi'), ('ta xi')) 
f.add_arc('75', '76', ('yu jia'), ('yo ga')) 
f.add_arc('77', '78', ('ka lu li'), ('ca lo rie'))

# Final/accepting state(s)
f.set_final('2')
f.set_final('3')
f.set_final('6')
f.set_final('9')
f.set_final('10')
f.set_final('12')
f.set_final('14')
f.set_final('24')
f.set_final('30')
f.set_final('32')
f.set_final('38')
f.set_final('40')
f.set_final('44')
f.set_final('48')
f.set_final('50')
f.set_final('54')
f.set_final('58')
f.set_final('60')
f.set_final('64')
f.set_final('66')
f.set_final('70')
f.set_final('74')
f.set_final('76')
f.set_final('78')

# recognize function defined in ChinglishFST
inp = ['ga', 'li', 'ga li', 'gu qi', 'ka fe', 'ka', 'ka', 'lu', 'li', 'shi duo pi li', 'mai', 'ke', 'feng', 'ba', 'lei']
outp = ['cur', 'ry', 'cur ry', 'coo kie', 'cof fee', 'cof', 'ca', 'lo', 'lie', 'straw ber ry', 'mi', 'cro', 'wind', 'ba', 'lay']

for i, (input_str, output_str) in enumerate(zip(inp, outp)):
    if f.recognize([input_str], [output_str]):
        print(f"{input_str} --> {output_str}   accept")
    else:   
        print(f"{input_str} --> {output_str}   reject") 
   
# outputs file to print all mappings 
f.write_mappings_to_file('Chinglish-trans.dat')

# constructs fst in window 
FSTDisplay(f).cf.mainloop()