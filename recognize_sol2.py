from nltk.nltk_contrib.fst.fst import *
from nltk.draw import * 
import tkinter as tk 

class ChinglishFST(FST):
    def __init__(self, name):
        super().__init__(name)
        self.mappings = []

    def add_arc(self, from_state, to_state, in_symbol, out_symbol):
        super().add_arc(from_state, to_state, in_symbol, out_symbol)
        # Keep track of mappings
        mapping = f"{' '.join(in_symbol)} --> {' '.join(out_symbol)}"
        self.mappings.append(mapping)

    def write_mappings_to_file(self, filename):
        with open(filename, 'w') as file:
            for mapping in self.mappings:
                file.write(f"{mapping}\n")
                
    def recognize(self, iput, oput):
        self.inp = iput.split() 
        self.outp = oput.split()
        
        if self.transduce(self.inp) == self.outp:
            return True
        else: 
            return False 

# Defines FST
f = ChinglishFST('chinglish-transliterations')

# Adds the states in the FST
for i in range(1,6):
    f.add_state(str(i)) 
    
# Initial state
f.initial_state = '1'
    
# Added all transitions 
f.add_arc('1', '2', ['beng'], ['ban'])
f.add_arc('2', '3', ['dai'], ['dage'])
f.add_arc('1', '2', ['a'], ['am'])
f.add_arc('2', '3', ['mo'], ['mo'])
f.add_arc('3', '4', ['ni'], ['ni'])
f.add_arc('4', '5', ['ya'], ['a'])
f.add_arc('1', '2', ['asi'], ['as'])
f.add_arc('2', '3', ['pi'], ['pi'])
f.add_arc('3', '4', ['lin'], ['rin'])
f.add_arc('1', '2', ['bei'], ['ba'])
f.add_arc('2', '3', ['guo'], ['gel'])
f.add_arc('1', '2', ['ban'], ['ban'])
f.add_arc('2', '3', ['zhuoqin'], ['jo'])
f.add_arc('1', '2', ['ba'], ['bal'])
f.add_arc('2', '3', ['lei'], ['let'])
f.add_arc('1', '2', ['bulu'], ['blu'])
f.add_arc('2', '3', ['si'], ['es'])
f.add_arc('1', '2', ['bashi'], ['bus'])
f.add_arc('1', '3', ['ka'], ['caf'])
f.add_arc('3', '4', ['fei'], ['fei'])
f.add_arc('4', '5', ['yin'], ['ne'])
f.add_arc('1', '5', ['ka'], ['car'])
f.add_arc('5', '5', ['tong'], ['toon'])
f.add_arc('1', '2', ['qiao'], ['choco'])
f.add_arc('2', '3', ['keli'], ['late'])
f.add_arc('1', '2', ['ka'], ['cof'])
f.add_arc('2', '3', ['fei'], ['fee'])
f.add_arc('1', '2', ['qu'], ['coo'])
f.add_arc('2', '3', ['qi'], ['kie'])
f.add_arc('1', '2', ['sha'], ['so'])
f.add_arc('2', '3', ['fa'], ['fa'])
f.add_arc('1', '2', ['ga'], ['cur'])
f.add_arc('2', '3', ['li'], ['ry'])
f.add_arc('1', '2', ['wei'], ['vi'])
f.add_arc('2', '3', ['ta'], ['ta'])
f.add_arc('3', '4', ['ming'],['min'])
f.add_arc('1', '2', ['tu'], ['to'])
f.add_arc('2', '3', ['si'], ['ast'])
f.add_arc('1', '2', ['de'], ['te'])
f.add_arc('2', '3', ['lu'], ['le'])
f.add_arc('1', '2', ['mai'], ['mi'])
f.add_arc('2', '3', ['ke'], ['cro'])
f.add_arc('3', '4', ['feng'], ['phone'])
f.add_arc('1', '2', ['sang'], ['heal'])
f.add_arc('2', '3', ['na'], ['th'])
f.add_arc('1', '2', ['makebei'], ['mug'])
f.add_arc('1', '2', ['ma'], ['mas'])
f.add_arc('2', '3', ['sha'], ['sa'])
f.add_arc('3', '4', ['ji'], ['ge'])
f.add_arc('1', '2', ['ning'], ['le'])
f.add_arc('2', '3', ['meng'], ['mon'])
f.add_arc('1', '2', ['jia'], ['jac'])
f.add_arc('2', '3', ['ke'], ['ket'])
f.add_arc('1', '2', ['suke'], ['scoo'])
f.add_arc('2', '3', ['da'], ['ter'])
f.add_arc('1', '2', ['xiang'], ['sham'])
f.add_arc('2', '3', ['bo'], ['poo'])
f.add_arc('1', '2', ['shiduo'], ['straw'])
f.add_arc('2', '3', ['pi'], ['ber'])
f.add_arc('3', '4', ['li'], ['ry'])
f.add_arc('1', '3', ['ji'], ['gui'])
f.add_arc('3', '4', ['ta'], ['tar'])
f.add_arc('1', '2', ['ha'], ['ho'])
f.add_arc('2', '3', ['ni'], ['ney'])
f.add_arc('1', '2', ['lei'], ['la'])
f.add_arc('2', '3', ['she'], ['ser'])
f.add_arc('1', '2', ['ni'], ['ny'])
f.add_arc('2', '3', ['long'], ['lon'])
f.add_arc('1', '2', ['di'], ['ta'])
f.add_arc('2', '3', ['shi'], ['xi'])
f.add_arc('1', '2', ['zhi'], ['che'])
f.add_arc('2', '3', ['shi'], ['ese'])
f.add_arc('1', '2', ['yu'], ['yo'])
f.add_arc('2', '3', ['jia'], ['ga'])
f.add_arc('1', '4', ['ka'], ['ca'])
f.add_arc('4', '5', ['lu'], ['lo'])
f.add_arc('5', '5', ['li'], ['rie'])

# Final/accepting state(s)
f.set_final('2')
f.set_final('3')
f.set_final('4')
f.set_final('5')

# recognize function defined in ChinglishFST
inp = "yu jia"
outp = "yo ga"

if f.recognize(inp, outp):
    print(inp + " --> " + outp + "  " + " accept")
else: 
    print(inp + " --> " + outp + "  " + " reject")
   
# outputs file to print all mappings 
f.write_mappings_to_file('Chinglish-trans.dat')

# constructs fst in window 
def fst_construct():
    disp = FSTDisplay(f)
    pass

window = tk.Tk()

button = tk.Button(window, text='FST Construct', command=fst_construct)
button.pack()

window.mainloop()